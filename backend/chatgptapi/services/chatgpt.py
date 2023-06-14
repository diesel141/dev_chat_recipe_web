# bizlogic
from django.conf import settings
import openai

openai.api_key = settings.API_KEY

def createPrompt(request):
    requestData = request.data
    appOverview = requestData["prompt"]["appOverview"]
    programmingLanguage = requestData["prompt"]["programmingLanguage"]
    useDatabase = requestData["prompt"]["useDatabase"]
    useCloud = requestData["prompt"]["useCloud"]

    promptAppOverview = "作りたいアプリの概要：" + appOverview + "\n"
    promptProgrammingLanguage = "プログラム言語：" + programmingLanguage + "\n"
    promptUseDatabase = "DB使用有無：有り" if useDatabase == "true" else "DB使用有無：無し"
    promptUseCloud = "クラウド使用有無：有り" if useCloud == "true" else "クラウド使用有無：無し"
    systemPrompt1 = "条件に指定されたアプリを作成する際に、指定されたプログラム言語で人気のあるフレームワークの紹介と解説してください。\n"
    systemPrompt2 = "もし、フレームワークが複数あるなら、最大３つまで教えてください。その際は各フレームワークの利点とと開発環境状況と難易度と登場時期を比較できるようにしてください。\n"
    systemPrompt3 = "また、質問にDB使用有無、クラウド使用有無が「有り」となっていた場合のみ、「有り」となっているものとの連携を考慮したライブラリを紹介してください。\n"

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": systemPrompt1 + systemPrompt2 + systemPrompt3
            },
            {
                "role": "user",
                "content": promptAppOverview + promptProgrammingLanguage + promptUseDatabase + promptUseCloud
            },
        ],
    )

    print("回答：" + res["choices"][0]["message"]["content"])
    print(res['usage'])
    return res["choices"][0]["message"]["content"];

def hoge():
    return "DRF Response OK"
