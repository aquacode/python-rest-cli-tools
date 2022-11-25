import requests
import click
import restapi_ctl
from clickaliasedgroup import ClickAliasedGroup


@click.group(cls=ClickAliasedGroup)
def main():
    pass


@main.command('get')
@click.argument('name')
@click.option('--bg_color', default='335eea')
@click.option('--font_color', default='FFFFFF')
@click.option('--image_format', default='png')
@click.option('--is_rounded', default='false')
@click.option('--is_uppercase', default='true')
@click.option('--is_italic', default='false')
@click.option('--is_bold', default='false')
def get(name, bg_color, font_color, image_format, is_rounded, is_uppercase, is_italic, is_bold):
    api_key = restapi_ctl.get_api_key('avatar')
    url = (f"https://avatars.abstractapi.com/v1/?api_key={api_key}"
           f"&name={name}&background_color={bg_color}&font_color={font_color}"
           f"&image_format={image_format}&is_rounded={is_rounded}"
           f"&is_uppercase={is_uppercase}&is_italic={is_italic}&is_bold={is_bold}"
           )
    response = requests.get(url)
    open('avatar.' + image_format, 'wb').write(response.content)


if __name__ == '__main__':
    main()
