# encoding=utf-8
import xmltodict

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


def get_icon(placemark):
    for key, value in ICON_MAPPING.iteritems():
        if key.decode("utf-8") in placemark["name"]:
            return value
    return ""


def run(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    content = xmltodict.parse(content)
    loc = open('locations.txt', 'w')
    loc.write("[\n")
    for placemark in content["kml"]["Document"]["Folder"]["Placemark"]:
        coordinates = placemark.get("Camera") or placemark.get("LookAt")
        print "[%s, %s, '%s', '%s', '%s']," % (
        coordinates["latitude"], coordinates["longitude"], get_icon(placemark), placemark["name"],
        placemark["description"])
        newline = "[%s, %s, '%s', '%s', '%s']," % (
        coordinates["latitude"], coordinates["longitude"], get_icon(placemark), placemark["name"],
        placemark["description"])
        loc.write(newline.encode("utf-8")+"\n")
    loc.write("],")
    loc.close()



if __name__ == "__main__":
    run('static/doc.kml')
