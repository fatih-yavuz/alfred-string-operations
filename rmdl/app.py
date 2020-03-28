import os
import random
import time


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


def remove_duplicate_lines(content):
    content = content.split("\n")
    content = [line.strip() for line in content if line.strip()]
    content = set(content)
    content = list(content)
    content.sort()
    return "\n".join(content)


def write_to_clipboard(content):
    filepath = generate_random_filepath()
    f = open(filepath, "w")
    f.write(content)
    f.close()
    os.system("cat " + filepath + " | pbcopy")


def main():
    content = read_from_clipboard()
    content = remove_duplicate_lines(content)
    write_to_clipboard(content)


main()
