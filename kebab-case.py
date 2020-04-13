import util

content = util.read_from_clipboard()
content = util.convert_to_kebab_case(content)
util.write_to_clipboard(content)
