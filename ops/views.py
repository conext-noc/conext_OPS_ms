import json
import os
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse, StreamingHttpResponse
from dotenv import load_dotenv
from ops.scripts.OX import client_operate


load_dotenv()


class OPS(generics.GenericAPIView):
    def data_generator(self, data):
        for client in data["clients"]:
            res = client_operate(
                client
            )  # You can adjust the number of iterations as needed
            data = {"message": "OK", "error": False, "data": [res]}
            yield json.dumps(data) + "\n"

    def get(self, _):
        return HttpResponse("ms_running", status=200)

    def post(self, req):
        if req.META["HTTP_CONEXT_KEY"] == os.environ["CONEXT_KEY"]:
            data = req.data
            response = StreamingHttpResponse(
                self.data_generator(data), content_type="application/json"
            )
            return response

        return HttpResponse("Bad Request to server", status=500)


class OPSDashboard(generics.GenericAPIView):
    def post(self, req):
        data = req.data
        if data["API_KEY"] == os.environ["API_KEY"]:
            res = []
            for client in data["clients"]:
                res.append(client_operate(client))
            return Response({"message": "OK", "error": False, "data": res})

        return HttpResponse("Bad Request to server", status=500)
