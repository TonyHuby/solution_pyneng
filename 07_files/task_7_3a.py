# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#from pprint import pprint
my_template = '{:<7}{:<18}{:<8}'

srcfile = 'CAM_table.txt'

result = []
with open(srcfile) as src:
    for line in src:
        if line.split() and line.split()[0].isdigit():
            vlan, mac, _, intf = line.split()
            vlan = int(vlan)
            vlan_line = [vlan, mac, intf]
            result.append(vlan_line)

result.sort()
for lst in result:
    vlan, mac, intf = lst
    print(my_template.format(vlan, mac, intf))