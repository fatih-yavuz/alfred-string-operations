import util


@util.eval
def _(content):
    content = content.split('\n')
    return str(set([line.strip() for line in content]))
