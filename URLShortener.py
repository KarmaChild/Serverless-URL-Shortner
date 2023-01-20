import boto3

client = boto3.resource('dynamodb')
table = client.Table('Serverless-URL-Shortner')


def shorten_url(original_url):
    dynamodb_get_response = get_dynamodb_item(original_url)

    if "Item" in dynamodb_get_response:
        total_urls = dynamodb_get_response["Item"]["url"]
        # new_short_url = encode(total_urls)
        return total_urls
    else:
        encoded_url = encode(original_url.__hash__())
        new_short_url = "lambda_url.com/" + str(encoded_url)
        # dynamodb_put_response returns status code 200 if success
        dynamodb_put_response = put_dynamodb_item(new_short_url, original_url)

    return [new_short_url, dynamodb_put_response]


def get_dynamodb_item(url):
    response = table.get_item(
        Key={
            'url': f'{url}'
        }
    )

    return response


def put_dynamodb_item(shortened_url, original_url):
    response = table.put_item(
        Item={
            "url": f"{shortened_url}",
            "original_url": f"{original_url}"
        }
    )

    status_code = response['ResponseMetadata']['HTTPStatusCode']

    return status_code


def encode(urls):
    base62_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(base62_characters)
    result = []
    # convert base10 id into base62 id for having alphanumeric shorten url
    while urls > 0:
        hash_value = urls % base
        result.append(base62_characters[hash_value])
        urls = urls // base
    # since ret has reversed order of base62 id, reverse ret before return it
    return "".join(result[::-1])
