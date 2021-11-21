import os
import shutil
import inspect


def create_static(x):
    for root, dirs, files in os.walk(x):
        if dirs == ['tamplates']:
            full_path = os.path.join(x, 'static')
            copy_d = os.path.join(root, dirs[0])
            # dirs_exist_ok корректно работает вроде как начиная с Python 3.8
            shutil.copytree(copy_d, full_path, dirs_exist_ok=True)


path = os.path.dirname(inspect.getfile(inspect.currentframe()))
full_path = os.path.join(path, 'project')

create_static(full_path)
