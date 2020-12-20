import base64

import util


@util.eval_lines
def _():
    def encode(content):
        return base64.b64encode(content.encode('utf-8')).decode('utf-8')

    return encode
