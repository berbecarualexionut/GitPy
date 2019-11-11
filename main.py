from GitPy import Github
import os
import sys
import logging
import argparse

logging.basicConfig(filename='app.log  ', filemode='a+', format='%(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('app')


def parse_arguments():
    args = argparse.ArgumentParser()
    args.add_argument('-owner', type=str, required=True, help='Specify the owner of the repository')
    args.add_argument('-repo',  nargs="+", required=True, help='Specify the name of the repository')
    args.add_argument('-resources', nargs="+", required=True, help='Specify what operations you want to execute')

    return args.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    a = Github(args.owner, args.repo, args.resources)
    data = a.read()
    while data is not None:
        data = a.read()

