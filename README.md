# GitPy
GitPy is a python library that gets data from Github API and stores it into files

## Usage

The Github class will take three arguments:owner(String), repo(List of Strings), resources(List of Strings)
```python
from GitPy import Github

github = Github('berbecarualexionut', 'GitPy', 'commits')

data = github.read()

while data is not None:
    data = github.read()
```
OR

you can call main.py with arguments like this:

python main.py -owner berbecarualexionut -repo GitPy -resources commits pulls

## StreamDispatcher

Because resulting json can have a bigger size, we can use streams to download shards from the resulting GET request.
Default size of shards is 1024 bytes.

## Methods

Read method: GitPy has a read method that takes no arguments(read()), based on operations specified it will read from a StreamDispatcher
and write corresponding bytes in file.

## Supported operations

GitPy currently supports following resource download:
commits, pulls and releases

## Directory structure

StreamDispatcher will write bytes to file for each iteration, the script will 
generate a directory structure like: {owner}/{repo}/{commits}/{sha}.json

## Requirements
This package requires requests lib, you can install it in your venv with:
pip install requests
 