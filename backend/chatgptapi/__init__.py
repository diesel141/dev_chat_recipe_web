import os

#ログファイルのパス
LOG_FILE_PATH = os.path.join('./log', 'backend.log')

# ディレクトリが存在しない場合は作成する
if not os.path.exists(os.path.dirname(LOG_FILE_PATH)):
    os.makedirs(os.path.dirname(LOG_FILE_PATH))
