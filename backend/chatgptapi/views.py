from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from .services.chatgpt import hoge


class RequestChatGPTView(APIView):
    def get(self, request, format=None):
        # ビジネスロジックを呼ぶだけにする
        msg = hoge()
        return Response({"message": msg}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        request_data = request.data
        return Response(
            {"message": request_data["message"]}, status=status.HTTP_201_CREATED
        )
