# 4.  Count the number of houses that make more 15% (.15) see [percentage="0.12"]
import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_properties_by_percentage():
    count = 0
    for child in root:
        dict = child.attrib
        property_percentage = float(dict["percentage"])
        if property_percentage > .15:
            count += 1
    return count


if __name__ == "__main__":
    print(get_properties_by_percentage())
