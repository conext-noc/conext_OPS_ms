import json
import os
import time
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse, StreamingHttpResponse
from dotenv import load_dotenv
from ops.scripts.OX import client_operate


load_dotenv()


class ProgressiveResponseView(generics.GenericAPIView):
    def data_generator(self):
        for i in range(1, 6):  # You can adjust the number of iterations as needed
            data = {"message": f"success {i}", "timestamp": time.time()}
            yield json.dumps(data) + "\n"
            time.sleep(60)  # Simulate some processing time

    def get(self, _):
        response = StreamingHttpResponse(
            self.data_generator(), content_type="application/json"
        )
        return response


class OPS(generics.GenericAPIView):
    def get(self, _):
        return HttpResponse("ms_running", status=200)

    def post(self, req):
        if req.META["HTTP_CONEXT_KEY"] == os.environ["CONEXT_KEY"]:
            data = req.data
            res = []
            for client in data["clients"]:
                res.append(client_operate(client))
            return Response({"message": "OK", "error": False, "data": res})

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
