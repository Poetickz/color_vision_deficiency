import math
from colormath.color_objects import sRGBColor, XYZColor
from colormath.color_conversions import convert_color

def spectral_to_rgb(wave):
    def xFit1931(wave):
        n1 = (wave-442.0)*(0.0624 if (wave<442.0) else 0.0374)
        n2 = (wave-599.8)*(0.0264 if (wave<599.8) else 0.0323)
        n3 = (wave-501.1)*(0.0490 if (wave<501.1) else 0.0382)
        return 0.362*math.exp(-0.5*n1**2) + 1.056*math.exp(-0.5*n2**2)- 0.065*math.exp(-0.5*n3**2)

    def yFit1931(wave):
        n1 = (wave-568.8)*(0.0213 if (wave<568.8) else 0.0247)
        n2 = (wave-530.9)*(0.0613 if (wave<530.9) else 0.0322)
        return 0.821*math.exp(-0.5*n1**2) + 0.286*math.exp(-0.5*n2**2)

    def zFit1931(wave):
        n1 = (wave-437.0)*(0.0845 if (wave<437.0) else 0.0278)
        n2 = (wave-459.0)*(0.0385 if (wave<459.0) else 0.0725)
        return 1.217*math.exp(-0.5*n1**2) + 0.681*math.exp(-0.5*n2**2)

    x = xFit1931(wave)
    y = yFit1931(wave)
    z = zFit1931(wave)
    xyz = XYZColor(x, y, z)
    rgb = convert_color(xyz, sRGBColor, target_illuminant='d65')

    return rgb

def get_data_from_file(file):
    f = open(file, "r")
    lines = f.readlines()
    data = {}
    for line in lines:
        x = float(line.split()[0])
        y = float(line.split()[1])
        data[x] = y
    return data

def get_rgb_tuple(wave):
    tuple_rgb = spectral_to_rgb(wave).get_upscaled_value_tuple()
    return ('{:03d}'.format(tuple_rgb[0]),'{:03d}'.format(tuple_rgb[1]),'{:03d}'.format(tuple_rgb[2]) )

def tuple_to_rgbid(rgb_tuple):
    return ''.join(rgb_tuple)

data_colors = get_data_from_file('refactored_data.txt')

f = open("rgb_ids.txt","w+")

for wave, intensity in data_colors.items():
    f.write('0.'+tuple_to_rgbid(get_rgb_tuple(wave))+"\t"+str(intensity)+"\n")
f.close()
