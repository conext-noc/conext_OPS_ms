
from ops.helpers.devices import devices
from ops.helpers.data_lookup import data_lookup
from ops.scripts.ssh import ssh
from ops.helpers.decoder import decoder

def operate(data):

    operation = "activate" if "R" in data['action'].upper() else (
        "deactivate" if "S" in data['action'].upper() else "")
    resultedAction = "Reactivado" if "R" in data['action'].upper() else (
        "Suspendido" if "S" in data['action'].upper() else "")

    oltOptions = ["1", "2", "3"]
    if data['olt'] in oltOptions:
        ip = devices[f"OLT{data['olt']}"]
        (comm, command, quit) = ssh(ip)
        decoder(comm)
        client,fail = data_lookup(comm,command,data['contract']).values()
        if fail == None and client != None:
          # command(f"interface gpon {client['frame']}/{client['slot']}")
          # command(f"ont {operation} {client['port']} {client['onu_id']}")
          print(client, operation, resultedAction, data)
        quit()
