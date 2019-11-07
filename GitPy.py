import requests
import json

class Github:
    def __init__(self, owner, repo, resources):
        self.owner = owner
        self.repo = repo
        self.resources = resources
        self.config = None

        # call additional config from json file
        self.init_conf()

    def init_conf(self):
        with open('config.json') as conf:
            self.config = json.load(conf)
        return

    def fetch_auth(self):
        resp = requests.get(self.config["git_entrypoint"])
        print(resp.content)
        return
