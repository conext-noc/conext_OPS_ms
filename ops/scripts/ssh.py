import os
from time import sleep
import paramiko
from dotenv import load_dotenv

load_dotenv()



def ssh(ip):
    count = 1
    delay = 1.5
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    comm = None
    keep = True

    # Handling multiple SSH sessions
    while keep and count <= 3:
        try:
            username = os.environ[f"user_{count}"]
            password = os.environ[f"password_{count}"]
            port = os.environ["port"]
            conn.connect(ip, port, username, password)
            comm = conn.invoke_shell()
            keep = False
        except paramiko.ssh_exception.AuthenticationException:
            keep = True
            count += 1
            continue
        break

    def enter():
        comm.send(" \n")
        comm.send(" \n")
        sleep(delay)

    def command(cmd):
        comm.send(cmd)
        sleep(delay)
        enter()

    def quit():
        conn.close()

    command("enable")
    command("config")
    command("scroll 512")

    return (comm, command, quit)