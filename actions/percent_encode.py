from urllib.parse import quote

import util


@util.eval
def _(content):
    return quote(content)
