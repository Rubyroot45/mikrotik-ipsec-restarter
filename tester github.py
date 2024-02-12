import ping3
import paramiko
import time 
import logging

# Set up logging
logging.basicConfig(filename='ipsec_switch.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ip_availability(ip):
    return ping3.ping(ip)


def restart_ipsec(ssh_client):
    command = "/ip ipsec peer disable [/ip ipsec peer find];/ip ipsec peer enable [/ip ipsec peer find]"
    ssh_client.exec_command(command)

ip_addresses = ['192.168.1.1', '192.168.2.1']  


ip_translation_table = {
    '192.168.1.1': '1.1.1.1',
    '192.168.2.1': '2.2.2.2'
    

}

username='your_login'
password = 'your_password'
port=your_port


while True:
    for ip in ip_addresses:
        if not check_ip_availability(ip):
            print(f"{ip} {ip_translation_table[ip]}")
            try:
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(ip_translation_table[ip],port=port,password=password,username=username,allow_agent=False,look_for_keys=False)
                restart_ipsec(ssh_client)
                print(f"IPsec {ip_translation_table[ip]} ")
            except Exception as e:
                print(f"{ip_translation_table[ip]}: {e}")
        else:
            print(f"{ip}")
    time.sleep(3) 
