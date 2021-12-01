# 11. In class: Display the total for all the net income made from all the states
import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_total_income():
    total_income = 0
    for child in root:
        total_income += float(child.text)

    return total_income


if __name__ == "__main__":
    print(get_total_income())
