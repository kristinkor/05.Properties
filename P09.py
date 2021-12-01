# 9. In class: Display all the data where the percentage is greater than 15%.
import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_data_by_percentage():
    data = []
    for child in root:
        dict = child.attrib
        property_percentage = float(dict["percentage"])
        if property_percentage > .15:
            data.append(dict)
            dict["income"] = child.text
    return data


if __name__ == "__main__":
    for data in get_data_by_percentage():
        print(data)
