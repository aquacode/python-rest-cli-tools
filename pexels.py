from pexelsapi.pexels import Pexels
import requests
import json
import click
import restapi_ctl
from clickaliasedgroup import ClickAliasedGroup


@click.group(cls=ClickAliasedGroup)
def main():
    pass


@main.command('photos')
@click.argument('query')
def photos(query):
    api_key = restapi_ctl.get_api_key('pexels')
    pexels = Pexels(api_key)
    photos = pexels.search_photos(query=query, page=1, per_page=5)
    print(photos.response_code)
    for photo in photos['photos']:
        val = pexels.get_photo(photo['id'])
        print(val)
        response = requests.get(val['src']['original'])
        open(query.replace(' ', '-') + '-' + str(val['id']) + '.jpg', 'wb').write(response.content)


if __name__ == '__main__':
    main()
