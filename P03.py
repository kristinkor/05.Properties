# 3.  The data represents is from a real estate management company. The company makes
# 3% of the cost (cost="33838"). What is the total cost?

import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_commission():
    cost = 0
    for child in root:
        dict = child.attrib
        cost += float(dict["cost"]) * 0.03

    return cost


if __name__ == "__main__":
    print(get_commission())
