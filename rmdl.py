import util

try:
    content = util.read_from_clipboard()
    content = util.remove_duplicate_lines(content)
    util.write_to_clipboard(content)
except:
    pass
