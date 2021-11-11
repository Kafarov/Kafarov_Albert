src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


unique_src = []
repeated_src = []


for i in src:
    if i in repeated_src:
        continue
    if i in unique_src:
        unique_src.remove(i)
        repeated_src.append(i)
        continue
    unique_src.append(i)
print(unique_src)
