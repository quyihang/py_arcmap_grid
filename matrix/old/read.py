import re


def read(str):
    f = open(str)
    o = f.readlines()
    pts = []
    for line in o:
        coords = line.split(',')
        pt = [float(re.findall(r"\d+\.?\d*", coords[2])[0]), float(coords[1])]
        pts.append(pt)
    return pts