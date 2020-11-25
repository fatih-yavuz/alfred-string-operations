import util
from handlers.write_handler import WriteHandler


class ListHandler(WriteHandler):
    def should_handle(self, content):
        return type(content) is list

    def handle(self, content):
        return util.json_prettify(content)
