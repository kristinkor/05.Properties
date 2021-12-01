# 6.  Which company id made the least net income [<property>net income</property>]?

import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_least_income_id():
    current_income = 0
    min_income = float(root[0].text)
    current_income_id = ""
    min_income_id = ""
    for child in root:
        dict = child.attrib

        current_income = float(child.text)
        current_income_id = child.get("id")
        if current_income < min_income:
            min_income = current_income
            min_income_id = current_income_id
    return min_income_id


if __name__ == "__main__":
    print(get_least_income_id())