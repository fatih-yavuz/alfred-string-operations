class WriteHandler:
    def should_handle(self, content):
        return False

    def handle(self, content):
        return content
