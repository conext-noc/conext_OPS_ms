from rest_framework.response import Response
from rest_framework import status,generics

# from .scripts.OLT import olt

class SimpleCRUD(generics.GenericAPIView):
  def get(self,req):
    print(req)
    data = {"message":"hello"}
    return Response({"message":"GET METHOD", "data":data})
  def post(self,req):
    # olt(req.data)
    return Response({"message":"POST METHOD", "data":req.data})