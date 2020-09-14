import compileall
import hashlib
import os
import shutil


def is_py_in_dir(path):
    for i in os.listdir(path):
        if i.endswith(".py"):
            return True
    return False


all_list = ["."]
the_list = []
for the_dir in os.listdir():
    if os.path.isdir(the_dir):
        if is_py_in_dir(the_dir):
            the_list.append(the_dir)

while len(the_list) != 0:
    the_dir = the_list.pop()
    for li in os.listdir(the_dir):
        if os.path.isdir(the_dir + os.sep + li):
            if is_py_in_dir(the_dir + os.sep + li):
                the_list.append(the_dir + os.sep + li)
    all_list.append(the_dir)

to_path = "dist"
to_path_update = "dist_update"

if to_path_update in os.listdir():
    shutil.rmtree("dist_update")

os.mkdir(to_path_update)

if to_path not in os.listdir():
    os.mkdir(to_path)

for the_dir in all_list:
    compileall.compile_dir(the_dir, maxlevels=0, legacy=True, optimize=2)

# for the_dir in all_list:
#     os.system(f"python -O -m compileall {the_dir} -b")

for the_dir in all_list:
    if the_dir == ".":
        for i in os.listdir():
            if i.endswith(".pyc"):
                if os.path.exists(to_path + os.sep + i):
                    with open(i, 'rb') as fp:
                        data = fp.read()
                    file1_md5 = hashlib.md5(data).hexdigest()
                    with open(to_path + os.sep + i, 'rb') as fp:
                        data = fp.read()
                    file2_md5 = hashlib.md5(data).hexdigest()
                    if file1_md5 != file2_md5:
                        shutil.copy(i, to_path + os.sep + i)
                        shutil.copy(i, to_path_update + os.sep + i)
                    # else:
                    #     os.remove(i)
                else:
                    shutil.copy(i, to_path + os.sep + i)
                    shutil.copy(i, to_path_update + os.sep + i)
    else:
        os.mkdir(to_path_update + os.sep + the_dir)
        if not os.path.exists(to_path + os.sep + the_dir):
            os.mkdir(to_path + os.sep + the_dir)
        for i in os.listdir(the_dir):
            if i.endswith(".pyc"):
                if os.path.exists(to_path + os.sep + the_dir + os.sep + i):
                    with open(the_dir + os.sep + i, 'rb') as fp:
                        data = fp.read()
                    file1_md5 = hashlib.md5(data).hexdigest()
                    with open(to_path + os.sep + the_dir + os.sep + i, 'rb') as fp:
                        data = fp.read()
                    file2_md5 = hashlib.md5(data).hexdigest()
                    if file1_md5 != file2_md5:
                        shutil.copy(the_dir + os.sep + i, to_path + os.sep + the_dir + os.sep + i)
                        shutil.copy(the_dir + os.sep + i, to_path_update + os.sep + the_dir + os.sep + i)
                    # else:
                    #     os.remove(the_dir + os.sep + i)
                else:
                    shutil.copy(the_dir + os.sep + i, to_path + os.sep + the_dir + os.sep + i)
                    shutil.copy(the_dir + os.sep + i, to_path_update + os.sep + the_dir + os.sep + i)
