from urllib import parse

import util


@util.eval
def _(content):
    parsed = parse.urlsplit(content)
    return util.json_prettify({
        'origin': parsed.netloc,
        'path': parsed.path,
        'query': parse.parse_qs(parsed.query)
    })
