import base64

import util


@util.eval_lines
def _():
    def decode(content):
        return base64.b64decode(content).decode('utf-8')

    return decode
