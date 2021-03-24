
import requests
from requests.models import Response

def get_hero_intelligence(hero_names):
    intel = {}
    must_intel = 0
    name_must = ''
    for name in hero_names:
        resp: Response = requests.get('https://superheroapi.com/api/2619421814940190/search/' + name)
        if resp.ok:
            intelligence = 0
            result = resp.json().get('results')
            if result:
                for dict in result:
                    powerstats = dict['powerstats']
                    if powerstats['intelligence'] != 'null':
                        if int(powerstats['intelligence']) > intelligence:
                            intelligence = int(powerstats['intelligence'])
                intel[name] = intelligence
    for key in intel:
        if int(intel[key]) > must_intel:
            must_intel = intel[key]
            name_must = key
    return name_must

print(get_hero_intelligence(['Hulk', 'Captain America', 'Thanos']))