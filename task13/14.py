from ipaddress import ip_network

for A in range(255, -1, -1):
    result = True
    net = ip_network(f'95.247.{A}.131/255.255.252.0', False)
    for host in net:
        str_host = f'{int(host):0>32b}'
        if str_host[:16].count('1') < str_host[16:].count('1'):
            result = False
            break
    if result:
        print(A)
        break
