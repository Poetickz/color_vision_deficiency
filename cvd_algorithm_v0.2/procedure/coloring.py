import math
from colormath.color_objects import sRGBColor, XYZColor
from colormath.color_conversions import convert_color

"""
--------------------------------------------------
              Files
--------------------------------------------------
"""
def get_data_from_file(file):
    f = open(file, "r")
    lines = f.readlines()
    data = {}
    for line in lines:
        x = float(line.split()[1])
        y = float(line.split()[2])
        z = float(line.split()[3])
        data[int(line.split()[0])] = (x,y,z)
    return data

def get_data_from_file_intensity(file):
    f = open(file, "r")
    lines = f.readlines()
    data = {}
    for line in lines:
        x = int(line.split()[0])
        y = float(line.split()[1])
        data[x] = y
    return data

"""
--------------------------------------------------
              FORMAT
--------------------------------------------------
"""
def get_rgb_tuple(wave, data_cie):
    tuple_rgb = raw_tuple(wave, data_cie)
    return tuple_rgb

def id_format(tuple_rgb):
    return ('{:03d}'.format(tuple_rgb[0]),'{:03d}'.format(tuple_rgb[1]),'{:03d}'.format(tuple_rgb[2]) )


def tuple_to_rgbid(rgb_tuple):
    return ''.join(rgb_tuple)

def raw_tuple(wave, data_cie):
    return spectral_to_rgb(wave, data_cie)

"""
--------------------------------------------------
              TRANSFORMATION
--------------------------------------------------
"""
def spectral_to_rgb(wave, data_cie):

    x = data_cie[wave][0]
    y = data_cie[wave][1]
    z = data_cie[wave][2]
    total = x+y+z

    x1 = y/total
    y1 = y/total
    z1 = z/total

    xyz = XYZColor(x1, y1, z1)
    rgb = convert_color(xyz, sRGBColor).get_upscaled_value_tuple()
    return (rgb)

"""
--------------------------------------------------
              MAIN
--------------------------------------------------
"""

data_cie = get_data_from_file("cie_1964.txt")

data_intensity = get_data_from_file_intensity("refactored_data.txt")

f = open("rgb_ids.txt","w+")
f2 = open("full_rgb.txt","w+")
aux = (0,0,0)
for wave, intensity in data_intensity.items():
    rgb = get_rgb_tuple(wave, data_cie)
    if (aux != rgb):
        aux = rgb
        print(rgb)
        f.write('0.'+str(tuple_to_rgbid(id_format(rgb)))+"\t"+str(intensity)+"\n")
        f2.write(str(rgb[0])+" "+str(rgb[1])+" "+str(rgb[2])+" "+str(intensity)+"\n")
f.close()
f2.close()