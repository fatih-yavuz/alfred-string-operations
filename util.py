import json
import os
import random
import re
import time

from handlers.byte_handler import ByteHandler
from handlers.list_handler import ListHandler
from handlers.set_handler import SetHandler

write_handlers = [
    ByteHandler(),
    ListHandler(),
    SetHandler()
]


def generate_random_filepath():
    return "/tmp/" + str(time.time()) + "-" + str(random.randrange(0, 99999, 1))


def write_clipboard_to_file():
    filepath = generate_random_filepath()
    os.system("pbpaste > " + filepath)
    return filepath


def read_from_clipboard():
    filepath = write_clipboard_to_file()
    f = open(filepath, "r")
    content = f.read()
    f.close()
    return content


def trim_lines(content):
    content = content.split("\n")
    content = [line.strip() for line in content if line.strip()]
    return "\n".join(content)


def sort_lines(content):
    content = content.split("\n")
    content = [line.strip() for line in content if line.strip()]
    content.sort()
    return "\n".join(content)


def deduplicate_lines(content):
    content = content.split("\n")
    content = set(content)
    content = list(content)
    return "\n".join(content)


def remove_duplicate_lines(content):
    return sort_lines(deduplicate_lines(trim_lines(content)))


def write_to_clipboard(content):
    for handler in write_handlers:
        if handler.should_handle(content):
            content = handler.handle(content)
            break

    filepath = generate_random_filepath()
    f = open(filepath, "w")
    f.write(content)
    f.close()
    os.system("cat " + filepath + " | pbcopy")


def convert_to_kebab_case(string):
    string = string.lower().strip()
    string = re.sub(r'\s+', '-', string)
    return string


def is_debug():
    return os.environ['DEBUG'] == 'true'


def debug(msg):
    if is_debug():
        print(msg)


def silent(func):
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            debug(e)
            return 'false'

    return handler


def json_prettify(content):
    if type(content) is not str:
        content = json.dumps(content)
    parsed = json.loads(content)
    return json.dumps(parsed, indent=4, sort_keys=True)


eval = lambda f: silent(write_to_clipboard(f(content=read_from_clipboard())))
