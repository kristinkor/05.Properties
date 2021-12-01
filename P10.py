# 10. In class: Display the total for all the net income made in NY,CT, and NJ
import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_data_by_states_income():
    ny_income = 0
    ct_income = 0
    nj_income = 0
    for child in root:
        dict = child.attrib
        if (dict["state"]) == "NY":
            ny_income += float(child.text)
        if (dict["state"]) == "CT":
            ct_income += float(child.text)
        if (dict["state"]) == "NJ":
            nj_income += float(child.text)

    return ny_income + ct_income + nj_income


if __name__ == "__main__":
    print(get_data_by_states_income())
