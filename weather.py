import requests
import json
import click
import restapi_ctl
from clickaliasedgroup import ClickAliasedGroup


@click.group(cls=ClickAliasedGroup)
def main():
    pass


@main.command('weather')
def weather():
    lat = "41.91"
    lon = "-87.64"
    api_key = restapi_ctl.get_api_key('weather')
    weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&&appid={api_key}&units=imperial"
    res = requests.get(weather)
    j = json.loads(res.content)
    o = json.dumps(j, indent=2)
    print(o)


@main.command('forecast')
def forecast():
    lat = "41.91"
    lon = "-87.64"
    api_key = restapi_ctl.get_api_key('weather')
    forecast = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    res = requests.get(forecast)
    j = json.loads(res.content)
    o = json.dumps(j, indent=2)
    print(o)


if __name__ == '__main__':
    main()
