from ipaddress import ip_network

for i in range(31, 1, -1):
    net_1 = ip_network(f'154.63.206.129/{i}', False)
    net_2 = ip_network(f'154.63.100.75/{i}', False)
    if net_1 == net_2:
        break
k = 0
for host in net_1:
    if bin(int(host))[2:].count('1') % 7 == 0:
        k += 1
print(k)