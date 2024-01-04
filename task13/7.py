from ipaddress import ip_network

net = ip_network('131.25.181.6/21', False)
k = 0
for ad in net:
    if '5' in hex(int(ad)):
        k += 1
print(k)