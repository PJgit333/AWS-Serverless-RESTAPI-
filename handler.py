# handler.py

def hello(event, context):
    body = {
        "message": "Hello, Serverless World!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

