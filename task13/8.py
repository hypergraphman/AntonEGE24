from ipaddress import ip_network

for i in range(0, 33):
    net1 = ip_network(f'192.148.56.26/{i}', False)
    net2 = ip_network(f'192.148.56.43/{i}', False)
    if net1 != net2:
        print(i)