import json

import util

try:
    content = util.read_from_clipboard()
    parsed = json.loads(content)
    prettied = json.dumps(parsed, indent=4, sort_keys=True)
    util.write_to_clipboard(prettied)
except:
    pass
