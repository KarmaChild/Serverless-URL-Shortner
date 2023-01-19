class URLShortener:
    # suppose, we already have 10 billion urls
    total_urls = 10000000000
    # store url to id in order not to have duplicated url with different id
    url_DB = {}

    def shorten_url(self, original_url):
        if original_url in self.url_DB:
            total_urls = self.url_DB[original_url]
            new_short_url = encode(total_urls)
        else:
            # store url2id in order not to have duplicated url with different id in the future
            self.url_DB[original_url] = self.total_urls
            new_short_url = encode(self.total_urls)
            # increase cnt for next url
            self.total_urls += 1

        return "lambda_url.com/" + new_short_url


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
