import requests
import json
import boto3
import os
from base64 import b64decode
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# 環境変数の値を代入
BACKLOG_API_URL = os.environ.get("BACKLOG_API_URL")
SLACK_URL = os.environ.get("SLACK_URL")
BACKLOG_SEARCH_URL = os.environ.get("BACKLOG_SEARCH_URL")
PROJECT_ID = os.environ.get("PROJECT_IDL")
ASIGNEE_ID = os.environ.get("ASIGNEE_ID")

def lambda_handler(event, context):
    # apikeyはLambda側で代入する変数なので関数内で代入はしない
    backlog_apikey = apikey
    backlog_api_url = BACKLOG_API_URL
    backlog_search_url = BACKLOG_SEARCH_URL
    slack_url = SLACK_URL

    # APIキー復号化
    ENCRYPTED = os.environ['apikey']
    # Decrypt code should run once and variables stored outside of the function
    # handler so that these are decrypted once per container
    DECRYPTED = boto3.client('kms').decrypt(
        CiphertextBlob=b64decode(ENCRYPTED),
        EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
    )['Plaintext'].decode('utf-8')

    # 検索フィルタ
    payload_check = {
        'apiKey': backlog_apikey,
        'projectId[]': PROJECT_ID, # 所属プロジェクトのID
        'statusId[]': ['1', '2'], #（0:すべて, 1:未対応, 2:処理中, 3:処理済み, 4:完了）
        'assigneeId[]': ASIGNEE_ID # 担当者のID
    }

    # チケット検索
    search_issues = requests.get(backlog_api_url, params=payload_check)

    # slack通知用の関数
    def slack_message(msg):
        requests.post(slack_url, data=json.dumps(msg))

    # slack通知内容
    info_msg = {
        "channel": "backlog-notification"
        "text":f"未完了の<{backlog_search_url}|タスク>があります。",
        "username":"Backlog Task Checker",
        "icon_emoji":":books:"
    }

    # チケットを検索し、該当するチケットが存在する場合は、slack通知
    try:
        get_issue = search_issues.json()[0]['issueKey']
        slack_message(info_msg)

    except IndexError:
        pass