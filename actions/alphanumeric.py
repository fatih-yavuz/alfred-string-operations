import re

import util


@util.eval
def _(content):
    return re.sub(r'\W+', '', content)
