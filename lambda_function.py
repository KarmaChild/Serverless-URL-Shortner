import URLShortener as shortener

new_url = shortener.shorten_url("new_url.com")

def lambda_handler(event, context):
    return new_url