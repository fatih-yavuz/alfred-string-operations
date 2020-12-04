import html

import util


@util.eval
def _(content):
    return html.unescape(content)
