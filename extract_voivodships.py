import geojson

voivodships = None
with open('polska-wojewodztwa.geojson', 'r') as F:
    voivodships = geojson.loads(F.read())

for district in voivodships.features:
    district_name = district.properties.get('name').lower()
    with open(u'{}.geojson'.format(district_name), 'w') as WF:
        WF.write(geojson.dumps(district.geometry))
