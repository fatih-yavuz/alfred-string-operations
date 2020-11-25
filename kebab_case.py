import util


@util.eval
def _(content):
    return util.convert_to_kebab_case(content)
