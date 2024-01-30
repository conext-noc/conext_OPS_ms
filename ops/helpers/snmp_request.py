from pysnmp.hlapi import *
def snmp_set_request(community, host, oid,fsp_inicial,ont_id,value):
    #1 active 2 deactive
    try:
        new_value = Integer(value)
        iterator = setCmd(
            SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid + f".{fsp_inicial}.{ont_id}"), new_value),
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:
            return {"error:":True,"message":"Error Indication!"}
        elif errorStatus:
            return {"error:":True,"message":"Error Status!"}
        else:
            for varBind in varBinds:
                return {"data":{
                        "error:":False,
                        "message":"Ejecutado Correctamente!!"
                        } 
                        }
    except Exception as e:
        return {
                    "error:":True,
                    "message":"Exception Error!"
                }
        

# snmp_set_request("ConextRoot","181.232.180.7","1.3.6.1.4.1.2011.6.128.1.1.2.46.1.1",161,"4194312960","40","1")
            