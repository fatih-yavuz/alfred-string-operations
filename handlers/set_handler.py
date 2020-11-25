import util
from handlers.write_handler import WriteHandler


class SetHandler(WriteHandler):
    def should_handle(self, content):
        return type(content) is set

    def handle(self, content):
        return util.json_prettify(content)
