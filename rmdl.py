import util


@util.eval
def _(content):
    return util.remove_duplicate_lines(content)
