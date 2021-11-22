import json
import os
import re

f_logs = os.path.join(os.path.dirname(__file__), 'nginx_logs.txt')
with open(f_logs, 'r', encoding='utf-8') as logs:
    with open('result.txt', 'w', encoding='utf-8') as result:
        pattern = re.compile(
            r'(?P<IP>^.*[^-])\s.+(?P<Date>\d{2}.\w+.\d{4}.\d{2}.\d{2}.\d{2}\s.\d{4}).+\s.(\w{3,4})\s(.\w+.\w+)\s\w+.\d+.\d+.\s(\d+)\s(\d+)')
        for line in logs.readlines():
            find_item = pattern.findall(line)
            result.write(str(find_item)+'\n')
