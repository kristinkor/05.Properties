# 7. In class: Display all the data where net income is greater than 5000
import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_data_gt5000():
    data = []
    for child in root:

        dict = child.attrib
        if float(child.text) > 5000:
            data.append(dict)
            dict["income"] = child.text

    return data


if __name__ == "__main__":

    for data in get_data_gt5000():
        print(data)
