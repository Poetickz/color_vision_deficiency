import math
from colormath.color_objects import sRGBColor, HSLColor
from colormath.color_conversions import convert_color
from statistics import mean 


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
    data = {'wave':[], 'intensity':[]}
    for line in lines:
        x = int(line.split()[0])
        y = float(line.split()[1])
        data[x] = y
    return data
  
def get_hsl_from_file(file):
    f = open(file, "r")
    lines = f.readlines()
    data = {}
    aux = 0
    for line in lines:
        x = int(float(line.split()[0]))
        y = float(line.split()[1])
        if(x in data):
            data[x].append(y)
        else:
            data[x] = [y]
    return data
"""
--------------------------------------------------
              FORMAT
--------------------------------------------------
"""
def get_rgb_tuple(wave, data_cie):
    tuple_rgb = spectral_to_rgb(wave, data_cie)
    return tuple_rgb


"""
--------------------------------------------------
              Resume
--------------------------------------------------
"""
def average(lst): 
    return mean(lst) 


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

    x1 = x/total
    y1 = y/total
    z1 = z/total

    xyz = XYZColor(x1, y1, z1)
    print(wave)
    rgb = convert_color(xyz, HSLColor).get_value_tuple()
    print(rgb)
    return (rgb)

"""
--------------------------------------------------
              MAIN
--------------------------------------------------
"""

data_cie = get_data_from_file("cie_1964.txt")

data_intensity = get_data_from_file_intensity("refactored_data.txt")

f = open("hsl_data.txt","w+")
f2 = open("hue_and_intensity.txt","w+")
aux = (0,0,0)
for wave, intensity in data_intensity.items():
    hsl = get_rgb_tuple(wave, data_cie)
    f.write(str(wave)+"\t"+str(hsl)+"\t"+str(intensity)+"\n")
    f2.write(str(hsl[0])+"\t"+str(intensity)+"\n")
f.close()
f2.close()


f = open("resume_hsl.txt","w+")
data = get_hsl_from_file("hue_and_intensity.txt")

for hue, intensity_array in data.items():
    f.write(str(hue)+"\t"+str(mean(intensity_array))+"\n")

f.close()