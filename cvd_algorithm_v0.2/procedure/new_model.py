import matplotlib.pyplot as plt
import collections


def get_data_from_file(file):
    f = open(file, "r")
    lines = f.readlines()
    data = {}
    for line in lines:
        x = float(line.split()[0])
        y = float(line.split()[1])
        data[x]=y
    return data

intensity_rgb = get_data_from_file("rgb_ids.txt")

intensity_rgb = collections.OrderedDict(sorted(intensity_rgb.items()))
rgb_a = []
intensity_a=[]

for rgb, intensity in intensity_rgb.items():
    rgb_a.append(rgb)
    intensity_a.append(intensity)

plt.figure(5)
plt.plot(rgb_a,intensity_a, '-', label='result')
plt.xlabel('rgb id')
plt.ylabel('intensity')
plt.title('Intensidad de luz vs RGB ')
plt.show()