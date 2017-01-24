from urllib.request import urlopen
import shutil, os

BASE_URL = 'https://raw.githubusercontent.com/'
RESOURCES = [ {
    "name": "_flex-box_mixins.scss",
    "url": BASE_URL + "mastastealth/sass-flex-mixin/master/_flexbox.scss"
}, {
    "name": "_media-query_mixins.scss",
    "url": BASE_URL + "paranoida/sass-mediaqueries/master/_media-queries.scss"
}, {
    "name": "_general_mixins.scss",
    "url": BASE_URL + "SwankSwashbucklers/some-sassy-mixins/master/mixins.scss"
} ]

def populate_resource(resource_name, resource_url):
    try:
        with urlopen(resource_url) as response, open(resource_name, 'wb') as f:
            shutil.copyfileobj(response, f)
        print("Successfully populated '{}'".format(resource_name))
    except Exception as e:
        message = "Could not populate resource"
        if (os.path.isfile(resource_name)):
            message = "Unable to update resource"
        message += ": {}\n  from url: {}\nException: {}"
        print(message.format(message, resource_name, resource_url, e))


print("Updating external sass resources")
for resource in RESOURCES:
    populate_resource(resource['name'], resource['url'])
