import xml.etree.ElementTree as ET
from PublicTransport import PublicTransport
from Bus import Bus
from Tram import Tram
from metro import Metro


def save_to_xml(filename, transport_list):
    root = ET.Element("TransportList")
    for transport in transport_list:
        root.append(transport.to_xml())
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def load_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    transport_list = []
    for element in root:
        if element.tag == "Bus":
            transport_list.append(Bus.from_xml(element))
        elif element.tag == "Tram":
            transport_list.append(Tram.from_xml(element))
        elif element.tag == "Metro":
            transport_list.append(Metro.from_xml(element))
        else:
            transport_list.append(PublicTransport.from_xml(element))
    return transport_list