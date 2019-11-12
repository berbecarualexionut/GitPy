from GitPy import Github
import os
import sys
import logging
import argparse

logging.basicConfig(filename='app.log  ', filemode='a+', format='%(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('app')


def parse_arguments():
    arguments = argparse.ArgumentParser()
    arguments.add_argument('-owner', type=str, required=True, help='Specify the owner of the repository, usage : -owner berbecarualexionut')
    arguments.add_argument('-repo',  nargs="+", required=True, help='Specify the name of the repository, usage: -repo GitPy')
    arguments.add_argument('-resources', nargs="+", required=True, help='Specify what operations you want to execute, usage: -resources commits pulls')

    return arguments.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    github = Github(args.owner, args.repo, args.resources)
    data = github.read()
    while data is not None:
        data = github.read()

