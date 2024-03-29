from time import sleep
import paramiko
from ops.helpers.request import db_request
from ops.helpers.definitions import endpoints


def ssh(ip):
    count = 0
    delay = 0.85
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    comm = None
    cont = True
    creds = db_request(endpoints["get_creds"], {})

    # Handling multiple SSH sessions
    while cont and count <= 2:
        try:
            username = creds["data"][count]["user_name"]
            password = creds["data"][count]["password"]
            port = 22
            conn.connect(ip, port, username, password)
            comm = conn.invoke_shell()
            cont = False
        except paramiko.ssh_exception.AuthenticationException:
            cont = True
            count += 1
            continue
        break

    def enter():
        comm.send(" \n")
        comm.send(" \n")
        sleep(delay)

    def command(cmd):
        print(cmd)
        comm.send(cmd)
        sleep(delay)
        enter()

    def quit_ssh():
        conn.close()

    command("enable")
    command("config")
    return (command, quit_ssh)
