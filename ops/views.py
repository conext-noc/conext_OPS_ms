from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse
from dotenv import load_dotenv
import os

load_dotenv()

from ops.scripts.OP import operate

class OPS(generics.GenericAPIView):
  def get(self, req):
    status_code = 200
    response_text = "ms_running"
    return HttpResponse(response_text, status=status_code)
  def post(self,req):
    if req.META['HTTP_CONEXT_KEY'] == os.environ["CONEXT_KEY"]:
      status_code = 200
      data = req.data
      res = []
      for client in data["clients"]:
        res.append(operate(client))
      return Response({"message":"OK", "data":res})
    else:
      return HttpResponse("Bad Request to server", status=400)