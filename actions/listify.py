import util


@util.eval
def _(content):
    content = content.split('\n')
    return [line.strip() for line in content]
