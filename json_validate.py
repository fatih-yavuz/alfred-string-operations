import json

import util


@util.eval
def _(content):
    json.loads(content)
    return 'true'
