#!/usr/bin/python3
"""
add item
"""


from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    ls_t = load_from_json_file(file)
except Exception:
    ls_t = []

for i in range(1, len(argv)):
    ls_t.append(argv[i])
    save_to_json_file(ls_t, file)
