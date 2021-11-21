import os
import inspect
import json


def create_folder(x):
    if not os.path.exists(x):
        os.mkdir(x)


def build_tree(root, data):
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            create_folder(path)
            build_tree(path, d[1])


full_path = os.path.dirname(inspect.getfile(inspect.currentframe()))
with open(os.path.join(full_path, 'config.json'), 'r', encoding='utf-8') as f:
    folder = json.load(f)
    build_tree(full_path, folder)
