import os
from collections import namedtuple

def get_exchange_lockal():
    script_dir = os.path.dirname(__file__)
    rel_path = "exchange.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path, 'r') as file:
        line = file.readline()
        print("get money")
        print(line)
        line_p = line.split("|")
        print(line_p)
        rate = namedtuple("Rate", "eur usd date")
        rate.usd = float(line_p[0])
        rate.eur = float(line_p[1])
        rate.date = line_p[2]
    return rate


