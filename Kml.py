#encoding=utf-8
import xml.etree.ElementTree as ET

tree = ET.parse('static/doc.kml')
root = tree.getroot()
root = root.iter('{http://www.opengis.net/kml/2.2}Placemark')
locations = []
name = ''
coord = ''
desc = ''
url = ''
ICON_MAPPING = {
    "Γρ": "office.png",
    "Eurobank": "euro.png",
    "Αττικής": "attica.png",
    "Πειρ": "piraeus.png",
    "Alpha": "alpha.png",
    "Θεσσαλίας": "thessaly.jpg",
    "Εθνική": "national.png",
    "EΘνική": "national.png",
    "ΕΛ.ΤΑ.": "post.png",
}


def logo(name):
    for key,value in ICON_MAPPING.iteritems():
        if key.decode("utf-8") in name:
            return value
    return ""


for child in root:
    for node in child.getiterator():
        if node.tag == '{http://www.opengis.net/kml/2.2}name':
            name = node.text
        if node.tag == '{http://www.opengis.net/kml/2.2}coordinates':
            coord = node.text
        if node.tag == '{http://www.opengis.net/kml/2.2}description':
            desc = node.text
        icon = logo(name)
    locations.append({'coordinates': coord, 'icon': icon, 'name': name, 'description': desc})

loc = open('locations.txt', 'w')
loc.write("[\n")
for i in locations:
    newline = "\t[" + i['coordinates']+ " , " + i['icon'] + " , " + i['name'] + " , " + i['description'] + "]\n"
    loc.write(newline.encode("utf-8"))
    print i['coordinates']+ " , " + i['icon'] + " , " + i['name'] + " , " + i['description']
loc.write("],")
loc.close()
