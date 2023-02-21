from ops.scripts.ssh import ssh
from ops.helpers.mapper import OLT

def operate(olt, action, client):
    ip = OLT[olt]
    (_, command, quit) = ssh(ip)
    operation = "activate" if "R" in action else ("deactivate" if "S" in action else "")
    result = "activo" if "R" in action else ("suspendido" if "S" in action else "")
    processedClients = []
    FRAME = str(client["frame"])
    SLOT = str(client["slot"])
    PORT = str(client["port"])
    ID = str(client["onu_id"])
    command(f"interface gpon {FRAME}/{SLOT}")
    command(f"ont {operation} {PORT} {ID}")
    command(f"display ont info {PORT} {ID}")
    command("q")
    obj = client.copy()
    obj["status"] = result 
    processedClients.append(obj)
    quit()
    return processedClients
