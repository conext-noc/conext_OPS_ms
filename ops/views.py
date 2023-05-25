import os
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse
from dotenv import load_dotenv
from ops.scripts.OP import operate

load_dotenv()


class OPS(generics.GenericAPIView):
    def get(self, _):
        return HttpResponse("ms_running", status=200)

    def post(self, req):
        if req.META["HTTP_CONEXT_KEY"] == os.environ["CONEXT_KEY"]:
            data = req.data
            res = []
            for client in data["clients"]:
                res.append(operate(client))
            return Response({"message": "OK", "error": False, "data": res})

        return HttpResponse("Bad Request to server", status=400)
