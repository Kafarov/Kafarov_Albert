src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_src = [i for j, i in zip(src, src[1:]) if i > j]
print(new_src)