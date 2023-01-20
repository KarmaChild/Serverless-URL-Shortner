import URLShortener as shortener
import json


def lambda_handler(event, context):
    body = event["url"]
    new_url = shortener.shorten_url(event["url"])

    statusCode = 200
    return {
        "statusCode": statusCode,
        "body": new_url,
        "headers": {
            "Content-Type": "application/json"
        }
    }