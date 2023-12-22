from ipaddress import ip_network

k = 0
for host in ip_network('117.32.0.0/255.224.0.0', False).hosts():
    if len(set(str(host).split('.'))) == 3:
        k += 1
print(k)