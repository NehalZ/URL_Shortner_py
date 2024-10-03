import requests

def shorten_url(url):
    api_url = f'http://tinyurl.com/api-create.php?url={url}'
    response = requests.get(api_url)
    return response.text
url = "https://www.example.com/very/long/url"
shortened_url = shorten_url(url)
print(f"Original URL: {url}")
print(f"Shortened URL: {shortened_url}")