#!/usr/bin/env python3
import os, sys, shutil

old_name = "zpui_example"

def replace_in_file(path, from_s, to_s):
    with open(path, 'r') as f:
        s = f.read()
    s = s.replace(from_s, to_s)
    with open(path, 'w') as f:
        f.write(s)

if len(sys.argv) < 2:
    print("Please supply the new name (i.e. rename.py zpui_my_best_app_ever)")
    sys.exit(1)

new_name = sys.argv[1]
if "-" in new_name:
    new_name = new_name.replace("-", "_")
    print("name not allowed to contain '-' (special symbol in Python), changing to {}".format(new_name))

if not new_name.startswith("zpui_"):
    print("name has to start with 'zpui_' (got: {})".format(repr(new_name)))
    sys.exit(1)

replace_in_file("pyproject.toml", old_name, new_name)
old_name_dash = old_name.replace("zpui_", "zpui-")
new_name_dash = new_name.replace("zpui_", "zpui-")
replace_in_file("pyproject.toml", old_name_dash, new_name_dash)
shutil.move("src/"+old_name, "src/"+new_name)
replace_in_file("src/{}/__init__.py".format(new_name), old_name, new_name)
