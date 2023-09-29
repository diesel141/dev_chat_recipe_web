from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from .services.chatgpt import hoge
from .services.chatgpt import createPrompt

class RequestChatGPTView(APIView):
    def get(self, request, format=None):
        # ビジネスロジックを呼ぶだけにする
        msg = hoge()
        return Response({"message": msg}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            # 質問結果取得
            content = createPrompt(request)
            
            if not content:
                return Response(
                    {"content": "結果が取得できませんでした。"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            else:
                return Response(
                    {"content": content}, status=status.HTTP_200_OK
                )
        except Exception as e:
            # エラーが発生した場合
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        