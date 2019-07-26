import paramiko
import time
import getpass

with open('devices.txt','r') as f :
    device = f.read().splitlines()

ip = list()
for item in device :
    tmp = item.split(':')
    ip.append(tuple(tmp))

for element in ip :
    print("Konfigurasi Router" + str(element[0]))
    username = "fauzi"
    password = getpass.getpass()

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=element[0], username=username, password=password, look_for_keys=False, allow_agent=False)

    print ("Koneksi Sukses", element[0])

    remote_connection = ssh_client.invoke_shell()

    remote_connection.send(?????) #masuk ke konfigurasi terminal
    remote_connection.send(?????) #buat interface loopback0
    remote_connection.send(?????) #masukkan address loopback0
    remote_connection.send(?????) #keluar
    remote_connection.send(?????) #routing eigrp as 10
    remote_connection.send(?????) #default route

    time.sleep(1)
    output = remote_connection.recv(65535)
    print (output.decode())
    ssh_client.close()
