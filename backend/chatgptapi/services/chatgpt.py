# bizlogic
from django.conf import settings
from googletrans import Translator
import openai

openai.api_key = settings.API_KEY
translator = Translator()

def createPrompt(request):
    requestData = request.data
    appOverview = requestData["prompt"]["appOverview"]
    programmingLanguage = requestData["prompt"]["programmingLanguage"]
    useDatabase = requestData["prompt"]["useDatabase"]
    useCloud = requestData["prompt"]["useCloud"]
    # 作りたいアプリ概要がない場合、処理終了
    if not appOverview:
        return ""

    # system
    systemPrompt1 = " 「作りたいアプリの概要：」で指定されたアプリを作成するのに必要な「プログラム言語：」に指定された言語のフレームワーク名を挙げてください。\n"
    systemPrompt2 = " 「プログラム言語：」に言語が指定されていない場合はおすすめ言語のフレームワーク名を挙げてください。 \n"
    systemPrompt3 = "もし、フレームワークが複数あるなら、最大3つまで教えてください。各フレームワークの「開発環境」を簡潔に教えてください。\n"
    systemPrompt4 = "また、質問にDB使用有無、クラウド使用有無が「有り」となっていた場合のみ、「有り」となっているものとの連携を考慮したライブラリを紹介してください。\n"
    systemPromptTemplate = "回答は＜テンプレート＞の内容に沿って返却してください。\n ＜テンプレート＞ \n フレームワーク名： \n  開発環境： \n"
    systemPromptEhd = "それ以外の回答はしないでください。\n 「作りたいアプリの概要：」で回答できない質問を指定された場合は、「アプリが不明です。」と返答してください。 \n 「プログラム言語：」に存在しない言語を質問されたら「存在しない言語です。入力内容を確認してください。」と回答してください。\n"
    # user
    promptAppOverview = "作りたいアプリの概要：" + appOverview + "\n"
    promptProgrammingLanguage = "プログラム言語：" + programmingLanguage + "\n"
    promptUseDatabase = "DB使用有無：有り" if useDatabase == "true" else ""
    promptUseCloud = "クラウド使用有無：有り" if useCloud == "true" else ""
    # 質問を投げる
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": translator.translate(systemPrompt1 + systemPrompt2 + systemPrompt3 + systemPrompt4 + systemPromptTemplate + systemPromptEhd, dest='en').text
            },
            {
                "role": "user",
                "content": translator.translate(promptAppOverview + promptProgrammingLanguage + promptUseDatabase + promptUseCloud, dest='en').text
            },
        ],
        n           = 1,                # 返答数
        temperature = 0,                # 出力する単語のランダム性（0から2の範囲） 0であれば毎回返答内容固定
    )
    # print("回答：" + res["choices"][0]["message"]["content"])
    # print("回答(翻訳)：" + translator.translate(res["choices"][0]["message"]["content"], dest='ja').text)
    # print(res['usage'])
    return translator.translate(res["choices"][0]["message"]["content"], dest='ja').text;

def hoge():
    return "DRF Response OK"
