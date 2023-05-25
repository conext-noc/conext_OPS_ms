from ops.helpers.devices import devices
from ops.scripts.ssh import ssh
from ops.helpers.decoder import decoder


def operate(data):
    client = {}
    operation = (
        "activate"
        if "R" in data["action"].upper()
        else ("deactivate" if "S" in data["action"].upper() else "")
    )
    resultedAction = (
        "Activo"
        if "R" in data["action"].upper()
        else ("Suspendido" if "S" in data["action"].upper() else "")
    )

    oltOptions = ["1", "2", "3"]
    if data["olt"] in oltOptions:
        ip = devices[f"OLT{data['olt']}"]
        (comm, command, quit_ssh) = ssh(ip)
        decoder(comm)
        command(f"interface gpon {data['frame']}/{data['slot']}")
        command(f"ont {operation} {data['port']} {data['onu_id']}")
        command("quit")
        quit_ssh()
        client["contract"] = data["contract"]
        client["olt"] = data["olt"]
        client["action"] = data["action"]
        client["state"] = resultedAction
        return client
