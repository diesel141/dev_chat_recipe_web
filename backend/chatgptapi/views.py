from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from .services.chatgpt import createPrompt

class RequestChatGPTView(APIView):
    def post(self, request, format=None):
        try:
            # # 質問結果取得
            # content = createPrompt(request)
            
            # if not content:
            #     return Response(
            #         {"content": "結果が取得できませんでした。"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            #     )
            # elif content == "max_len_error":
            #     return Response(
            #         {"content": "入力項目の桁数が上限を超えています。"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            #     )
            # else:
            #     return Response(
            #         {"content": content}, status=status.HTTP_200_OK
            #     )
                return Response(
                    # {"content": "RJCはエンジニアが主役。RJCのエンジニアはお客様の未来のために、スキルを高め続けています。RJCはそんなエンジニアを全力で応援し、エンジニアと共にお客様にハッピーを届けます。"}, status=status.HTTP_200_OK
                    {"content": "フレームワーク名：React\n開発環境：Visual Studio Code、WebStorm、Atomなどのさまざまなツールを使用してReactを開発できます。開発環境をセットアップするために、node.jsとnpm（ノードパッケージマネージャー）をインストールする必要があります。"}, status=status.HTTP_200_OK
                    # {"content": "1981年7月9日に稼動を開始したアーケードゲーム『ドンキーコング』で初登場して以来、非常に多くのゲームソフトに登場している[1]。また、任天堂の看板キャラクターとして、任天堂公式ホームページのアイコンなどのデザインにも採用されている。\n\n\nマリオが主役として登場する「マリオシリーズ」の累計販売本数は、代表的なアクションゲームシリーズ「スーパーマリオシリーズ」のみで全世界4億1300万本以上（2022年3月末時点）に達している[2]。この記録はゲーム業界全体で世界1位であり、他社が版権を有するものを含め、過去数十年間のゲーム産業で誕生したフランチャイズにおいてこの記録を上回るものは存在していない。"}, status=status.HTTP_200_OK
                    # {"content": "Java（ジャバ、ジャヴァ）は、汎用プログラミング言語とソフトウェアプラットフォームの双方を指している総称ブランドである[6]。オラクルおよびその関連会社の登録商標である。1996年にサン・マイクロシステムズによって市場リリースされ、2010年に同社がオラクルに吸収合併された事によりJavaの版権もそちらに移行した。\n\nプログラミング言語Javaは、C++に類似の構文、クラスベースのオブジェクト指向、マルチスレッド、ガベージコレクション、コンポーネントベース、分散コンピューティングといった特徴を持ち、平易性重視のプログラム書式による堅牢性と、仮想マシン上での実行によるセキュリティ性およびプラットフォーム非依存性が理念とされている。Javaプラットフォームは、Javaプログラムの実行環境または、実行環境と開発環境の双方を統合したソフトウェアであり、ビジネスサーバ、モバイル機器、組み込みシステム、スマートカードといった様々なハードウェア環境に対応したソフトウェア形態で提供されている。その中枢技術であるJava仮想マシンは各プラットフォーム環境間の違いを吸収しながら、Javaプログラムの適切な共通動作を実現する機能を備えている[7]。このテクノロジは「write once, run anywhere」と標榜されていた[8]。"}, status=status.HTTP_200_OK
                    # {"content": "STEP1：取引種類を選択して銘柄コードを入力する ユーザーネームとパスワードを入力して、SBI証券のPCサイトにログインしましょう。"}, status=status.HTTP_200_OK
                )
        except Exception as e:
            # エラーが発生した場合
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        