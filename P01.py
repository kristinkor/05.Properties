# 1.  How many houses cost more than 124,000?

import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_properties_by_cost():
    count = 0
    for child in root:
        dict = child.attrib
        property_cost = float(dict["cost"])
        if property_cost > 124_000:
            count += 1
    return count


if __name__ == "__main__":
    print(get_properties_by_cost())
