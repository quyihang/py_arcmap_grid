import re


def read(str):
    f = open(str)
    o = f.readlines()
    pts = []
    for line in o:
        coords = line.split(',')
        pt = [float(re.findall(r"\d+\.?\d*", coords[2])[0]), float(coords[1]), coords[3]]
        pts.append(pt)
    return pts

def divide(ptarr, str):
    out = []
    for pt in ptarr:
        if str == pt[2]:
            out.append([pt[0], pt[1]])
    return out

def divide(ptarr, s, e):
