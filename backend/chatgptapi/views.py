from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from .services.chatgpt import createPrompt

class RequestChatGPTView(APIView):
    def post(self, request, format=None):
        return Response(
            {"content": "フレームワーク名：React\n開発環境：Visual Studio Code、WebStorm、Atomなどのさまざまなツールを使用してReactを開発できます。開発環境をセットアップするために、node.jsとnpm（ノードパッケージマネージャー）をインストールする必要があります。"}, status=status.HTTP_200_OK
        )
        # try:
        #     # 質問結果取得
        #     content = createPrompt(request)
            
        #     if not content:
        #         return Response(
        #             {"content": "結果が取得できませんでした。"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        #         )
        #     elif content == "max_len_error":
        #         return Response(
        #             {"content": "入力項目の桁数が上限を超えています。"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        #         )
        #     else:
        #         return Response(
        #             {"content": content}, status=status.HTTP_200_OK
        #         )
        # except Exception as e:
        #     # エラーが発生した場合
        #     return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        