

f_logs = 'Kafarov_Albert_dz_6/nginx_logs.txt'
f_trans = 'Kafarov_Albert_dz_6/logs.txt'

q = []
with open(f_logs, 'r', encoding='utf-8') as logs:
    for el in logs.readlines():
        i = [i for i in el.split()]
        x = i[0], i[5], i[6]
        q.append(x)
print(q)