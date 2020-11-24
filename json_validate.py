import json

import util

try:
    content = util.read_from_clipboard()
    parsed = json.loads(content)
except:
    util.write_to_clipboard('false')
