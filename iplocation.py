import requests
import json
import click
import restapi_ctl
from clickaliasedgroup import ClickAliasedGroup


@click.group(cls=ClickAliasedGroup)
def main():
    pass


@main.command('get')
@click.argument('ip')
def get(ip):
    api_key = restapi_ctl.get_api_key('location')
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address={ip}"
    response = requests.get(url)
    j = json.loads(response.content)
    o = json.dumps(j, indent=2)
    print(o)


if __name__ == '__main__':
    main()
