from handlers.write_handler import WriteHandler


class ByteHandler(WriteHandler):
    def should_handle(self, content):
        return type(content) is bytes

    def handle(self, content):
        return str(content.decode('utf-8'))
