from urllib.parse import unquote

import util


@util.eval
def _(content):
    return unquote(content)