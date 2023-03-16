from rest_framework.response import Response
from rest_framework import generics

from ops.scripts.OP import operate


class OPS(generics.GenericAPIView):
  def get(self,req):
    return Response({"message":"MS_RUNNING"})
  def post(self,req):
    data = req.data
    res = []
    for client in data["clients"]:
      res.append(operate(client))
    return Response({"message":"OK", "data":res})