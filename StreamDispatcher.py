import requests


class StreamDispatcher:
    def __init__(self, url, file):
        self.url = url
        self.file = file

        self.stream = None
        self.opened = None

        self.open_stream()

    def open_stream(self):
        self.stream = requests.get(self.url, stream=True)
        self.opened = True

    def write_shard(self):
        with open(self.file, 'w+') as f:
            shard = self.stream.iter_content(chunk_size=1024)
            if shard:
                f.write(shard)
                f.flush()
