import util

@util.eval
def _(content):
    return util.json_prettify(content)
