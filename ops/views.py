import json
import os
from rest_framework import generics
from django.http import HttpResponse, StreamingHttpResponse
from dotenv import load_dotenv
from ops.scripts.OX import client_operate


load_dotenv()


def data_generator(data):
    for client in data["clients"]:
        res = client_operate(client)
        data = {"message": "OK", "error": False, "data": [res]}
        yield json.dumps(data) + "\n"


class OPS(generics.GenericAPIView):
    def get(self, _):
        return HttpResponse("ms_running", status=200)

    def post(self, req):
        if req.META["HTTP_CONEXT_KEY"] == os.environ["CONEXT_KEY"]:
            data = req.data
            response = StreamingHttpResponse(
                data_generator(data), content_type="application/json"
            )
            return response

        return HttpResponse("Bad Request to server", status=500)


class OPSDashboard(generics.GenericAPIView):
    def post(self, req):
        data = req.data
        if data["API_KEY"] == os.environ["API_KEY"]:
            response = StreamingHttpResponse(
                data_generator(data), content_type="application/json"
            )
            return response
        return HttpResponse("Bad Request to server", status=500)
