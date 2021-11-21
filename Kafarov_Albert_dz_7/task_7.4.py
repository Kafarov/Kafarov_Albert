import os

path = os.path.join(os.path.dirname(__file__), 'some_data')
size_dict = {}
for file in os.scandir(path):
    size = os.path.getsize(file)
    key = 10 ** len(str(size))
    if key in size_dict:
        size_dict[key] += 1
    else:
        size_dict[key] = 1

for k in sorted(size_dict.keys()):
    print(k, ':', size_dict[k])
