import re


def read(str):
    f = open(str)
    o = f.readlines()
    pts = []
    for line in o:
        coords = line.split(',')
        pt = [float(re.findall(r"\d+\.?\d*", coords[2])[0]), float(coords[1]), coords[3], coords[0]]
        pts.append(pt)
    return pts

def divide(ptarr, str):
    out = []
    for pt in ptarr:
        if str == pt[2][:-1]:   # delete \n
            out.append(pt)
    return out

def divide_(ptarr, s, e):
    out = []
    for i in range(s, e+1):
        out.append(ptarr[i])
    return out