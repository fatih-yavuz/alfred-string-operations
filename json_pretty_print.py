import util

@util.eval
def _(content):
    return util.json_pretty_print(content)
