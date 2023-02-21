from rest_framework.response import Response
from rest_framework import status,generics
from dotenv import load_dotenv
import os
import json

from ops.scripts.OP import operate

load_dotenv()

TOKEN = os.environ["TOKEN"]

class OPS(generics.GenericAPIView):
  def post(self,req):
    resultedClients = []
    body = json.loads(req.body)
    if body["api_key"] == TOKEN:
        clients = body["clients"]
        for client in clients:
            res = operate(client["olt"], client["action"], client)
            resultedClients.append(res)
        return Response({"message":"OK", "data": resultedClients})
    return Response({"message":"invalid api_key", "data": "ERR"})