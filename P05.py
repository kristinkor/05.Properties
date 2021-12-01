# 5.  Which company id made the most net income [<property>net income</property>]?

import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_most_income_id():
    max_income = 0
    max_income_id = ""
    for child in root:
        current_income = float(child.text)
        current_income_id = child.get("id")
        if current_income > max_income:
            max_income = current_income
            max_income_id = current_income_id
    return max_income_id


if __name__ == "__main__":
    print(get_most_income_id())
