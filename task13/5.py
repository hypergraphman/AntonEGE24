from ipaddress import ip_network

net = ip_network('131.72.46.6/192.0.0.0', False)
k = 0
for ad in net:
    t = f'{int(ad):b}'[16:]
    if t.count('1') > 4:
        k += 1
print(k)