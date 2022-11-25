import requests
import click
import restapi_ctl
from clickaliasedgroup import ClickAliasedGroup

@click.group(cls=ClickAliasedGroup)
def main():
    pass

@main.command('get')
@click.argument('categories')
def get(categories):
    country = "us"
    lang = "en"
    api_key = restapi_ctl.get_api_key('news')
    url = f"https://api.thenewsapi.com/v1/news/top?api_token={api_key}&locale={country}&categories={categories}"
    print(url)
    headlines = requests.get(url)
    print(headlines.status_code)
    for i in headlines.json()['data']:
        print(i['title'])
        print(i['url'])
        print()

if __name__ == '__main__':
    main()