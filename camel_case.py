import stringcase
import util


@util.eval
def _(content):
    return stringcase.camelcase(content)
