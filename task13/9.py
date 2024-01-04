from ipaddress import ip_network

for i in range(20, 33):
    net1 = ip_network(f'180.32.131.214/{i}', False)
    net2 = ip_network(f'180.32.131.202/{i}', False)
    if net1 == net2:
        print(net1.num_addresses)