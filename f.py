import json

MapInfo = None
nombrearchivo = 'Assets\Levels\Level1\Level1a.json'
with open(nombrearchivo) as info:
    MapInfo = json.load(info)
info.close()
print(MapInfo['layers'][12]['objects'][0]['visible'])
MapInfo['layers'][12]['objects'][1]['visible'] = True

a_file = open('Assets\Levels\Level1\Level1a.json', 'w')
json.dump(MapInfo, a_file,indent=4)
a_file.close()

nombrearchivo2 = 'Assets\Levels\Level1\Level1a.json'
with open(nombrearchivo2) as info:
    MapInfo = json.load(info)
    print(MapInfo['layers'][12]['objects'][0]['visible'])
info.close()


