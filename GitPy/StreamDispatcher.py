import requests
import logging

logger = logging.getLogger('app')


class StreamDispatcher:
    def __init__(self, url, file):
        self.url = url
        self.file = file

        self.stream = None
        self.opened = None
        self.shard = None

        self.open_stream()

    def open_stream(self):
        logger.info('Opening stream for url: {}'.format(self.url))
        self.stream = requests.get(self.url, stream=True)
        self.opened = True
        # get 1024 bytes from requests
        self.shard = self.stream.iter_content(chunk_size=1024)

    def write_shard(self):
        with open(self.file, 'ab') as f:
            try:
                shard = next(self.shard)
                if shard:
                    logger.info('Writing shard to {}'.format(self.file))
                    f.write(shard)
                    f.flush()
            except StopIteration:
                self.opened = False
                self.stream.close()
