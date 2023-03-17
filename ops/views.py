from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse

from ops.scripts.OP import operate


class OPS(generics.GenericAPIView):
  def get(self,req):
    return HttpResponse("ms_running",status=200)
  def post(self,req):
    data = req.data
    res = []
    for client in data["clients"]:
      res.append(operate(client))
    return Response({"message":"OK", "data":res})