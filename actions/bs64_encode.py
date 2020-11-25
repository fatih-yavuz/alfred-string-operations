import base64

import util


@util.eval
def _(content):
    return base64.b64encode(content.encode('utf-8'))