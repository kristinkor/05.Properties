import xml.dom.minidom
from flask import Flask

from P01 import get_properties_by_cost
from P02 import get_income
from P03 import get_commission
from P04 import get_properties_by_percentage
from P05 import get_most_income_id
from P06 import get_least_income_id

app = Flask(__name__)
import xml.etree.cElementTree as ET


@app.route("/properties")
def properties():
    root = ET.Element("questions")
    name = ET.SubElement(root, 'name')
    name.text = "korzhenevsakya, kristina"

    question1 = ET.SubElement(root, "question", no="1")
    question1.text = str(get_properties_by_cost())
    question2 = ET.SubElement(root, "question", no="2")
    question2.text = str(get_income())
    question3 = ET.SubElement(root, "question", no="3")
    question3.text = str(get_commission())
    question4 = ET.SubElement(root, "question", no="4")
    question4.text = str(get_properties_by_percentage())
    question5 = ET.SubElement(root, "question", no="5")
    question5.text = str(get_most_income_id())
    question6 = ET.SubElement(root, "question", no="6")
    question6.text = str(get_least_income_id())

    tree = ET.ElementTree(root)
    tree.write("filename.xml")

    return ET.tostring(root)


if __name__ == "__main__":
    app.run(debug=True, port=9121)
