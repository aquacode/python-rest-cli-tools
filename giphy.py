import requests
import json
import click
import restapi_ctl
from clickaliasedgroup import ClickAliasedGroup


@click.group(cls=ClickAliasedGroup)
def main():
    pass


@main.command('get')
@click.argument('query')
def get(query):
    api_key = restapi_ctl.get_api_key('giphy')
    url = "https://api.giphy.com/v1/gifs/search"
    param = {
        "q": query,
        "api_key": api_key,
        "limit": "5"
    }
    resp = requests.get(url, params=param)
    data = json.loads(resp.text)
    result = json.dumps(data, indent=2, sort_keys=True)
    print(result)


if __name__ == '__main__':
    main()
