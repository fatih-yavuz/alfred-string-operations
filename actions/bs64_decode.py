import base64

import util


@util.eval
def _(content):
    return base64.b64decode(content).decode('utf-8')
