#!/usr/bin/python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary: dict, filename):
        root = ET.Element("data")
        tree = ET.ElementTree(root)
        for key, value in dictionary.items():
            elem = ET.SubElement(root, key)
            elem.text = value
        ET.indent(tree, "  ")
        tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        deserial: dict = {}
        for child in root:
            deserial[str(child.tag)] =str(child.text)
        return deserial