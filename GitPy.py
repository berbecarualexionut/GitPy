import requests as req
import json
import threading
import logging
import os
from StreamDispatcher import StreamDispatcher

logger = logging.getLogger('app')


class Github:
    def __init__(self, owner, repo, resources):
        self.owner = owner
        self.repo = repo
        self.resources = resources

        self.entrypoints = {}
        self.streams = []

        # get repository lists for resources
        self.commits = []
        self.pulls = []
        self.releases = []

        # call additional config from json file
        self.init_conf()

        # variable that checks if the directory structure is built
        self.built_directories = False

    def init_conf(self):
        """
        Read config file and get possible endpoints, makes requests urls easier to access
        :return:
        """
        # read conf file
        with open('config.json') as conf:
            config = json.load(conf)
            endpoints = config['endpoints']
            for resource, url in endpoints[0].items():
                # store entrypoints in class for easy access to url
                self.entrypoints[resource] = config["github_entrypoint"] + url
        for resource in self.resources:
            # initialise class properties based on demanded resources
            property_list = self.get_repo_info(resource)
            setattr(self, resource, property_list)
        return

    def read(self):
        if not self.built_directories:
            self.build_directories()
        if len(self.streams) == 0:
            self.init_streams()
        for stream in self.streams:
            if stream.opened:
                stream.write_shard()

    def init_streams(self):
        for repo in self.repo:
            for resource in self.resources:
                param_list = getattr(self, resource)
                for item in param_list:
                    # generate url for request
                    url = self.entrypoints[resource].format(self.owner, repo)
                    url += '/' + item
                    file_path = os.path.join(self.owner, repo, resource, item) + '.json'
                    # make GET request to GITHUB API, in order to get chunks from request use it as a stream
                    # store stream for later content manipulation
                    logger.info('Start stream for url : {}'.format(url))
                    self.streams.append(StreamDispatcher(url, file_path))

    def get_repo_info(self, resource):
        """
        Generator that will return all commits, pulls or releases for every repo passed in the command line
        """
        for repo in self.repo:
            logger.debug('Get {} for owner: {} repository: {}'.format(resource, self.owner, repo))
            url = self.entrypoints[resource].format(self.owner, repo)
            response = req.get(url)
            # extract json response from api
            decoded_resp = json.loads(response.content)
            if len(decoded_resp) == 0:
                logger.info('No {} for repository: {}'.format(resource, repo))
            else:
                for item in decoded_resp:
                    if resource == 'commits':
                        yield item['sha']
                    elif resource == 'releases':
                        yield item['tag_name']
                    else:
                        yield item['id']

    def build_directories(self):
        """
        Generate directories structure where streams will write content from requests
        Example of directory structure: berbecarualexionut/GitPy/commits/{sha}
        """
        logger.info('Generating directory structure')
        owner_directory = self.owner
        repo_directory = self.repo
        resources_directory = self.resources
        # TODO: rethink how to generate directories
        for repo in repo_directory:
            for resource in resources_directory:
                director = os.path.join(owner_directory, repo, resource)
                os.makedirs(director,exist_ok=True)
        self.built_directories = True

