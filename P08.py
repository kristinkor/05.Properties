# 8.In class: Display all the data where state is DC,NY,NJ and KY
import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_data_by_states():
    data = []
    for child in root:
        dict = child.attrib
        if (dict["state"]) == "NY" or (dict["state"]) == "DC" or (dict["state"]) == "NJ" or (dict["state"]) == "KY":
            data.append(dict)
            dict["income"] = child.text

    return data


if __name__ == "__main__":
    for data in get_data_by_states():
        print(data)
