# 2.  How much money(income) was made in NY, that net income data is located inside the property tag
# [<property>net income</property>]?
import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_income():
    income = 0
    for child in root:

        dict = child.attrib
        if (dict["state"]) == "NY":
            income += float(child.text)

    return income


if __name__ == "__main__":
    print(get_income())
