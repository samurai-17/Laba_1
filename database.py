import json
from PublicTransport import PublicTransport
from Bus import Bus
from Tram import Tram
from metro import Metro


def save_to_json(filename, transport_list):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([transport.to_dict() for transport in transport_list], f, ensure_ascii=False, indent=4)


def load_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        transport_list = []
        for item in data:
            if item["type"] == "Bus":
                transport_list.append(Bus.from_dict(item))
            elif item["type"] == "Tram":
                transport_list.append(Tram.from_dict(item))
            elif item["type"] == "Metro":
                transport_list.append(Metro.from_dict(item))
            else:
                transport_list.append(PublicTransport.from_dict(item))
        return transport_list
