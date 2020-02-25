import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import colorsys


def get_data_from_file(file):
    """
    This function gets the data set from a file.

    INPUTS
    file -> the path of the file (string)

    OUTPUT
    data -> a hash/dictonary with all data (wave & intensity)
    """
    f = open(file, "r")
    lines = f.readlines()
    data = {'wave':[], 'intensity':[]}
    for line in lines:
        x = float(line.split()[0])
        y = float(line.split()[1])
        data['wave'].append(x)
        data['intensity'].append(y)
    return data

def wavelength_to_rgb(wavelength, gamma=0.8):

    '''This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    '''

    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return rgb_int_to_float((int(R), int(G), int(B)))

def rgb_int_to_float(rgb_int):
    return (float(rgb_int[0]/255.00000), float(rgb_int[1]/255.00000),  float(rgb_int[2]/255.00000))



data_set = get_data_from_file('data.txt')
n = len(data_set['wave'])
colors = []
for i in data_set['wave']:
    colors.append(wavelength_to_rgb(i))

new_colors = []

for c,d in zip(colors, data_set['intensity']):
    if d > 0:
        new_colors.append((c[0]*d, c[1]*(d), c[2]*(d)))
    else:
        new_colors.append((0, 0, 0))



normales = LinearSegmentedColormap.from_list(
    'Originales', colors, n)

cambiados = LinearSegmentedColormap.from_list(
    'Cambiados', new_colors, n)
matrix = np.random.random((10, 10))

# plot the matrix as an image with an appropriate colormap
plt.figure(1)
plt.imshow(matrix.T, aspect='auto', cmap=normales)
plt.axis('off')

plt.figure(2)
plt.imshow(matrix.T, aspect='auto', cmap=cambiados)
plt.axis('off')

plt.figure(3)
green = []
red = []
blue = []
for i in colors:
    red.append(i[0])
for i in colors:
    blue.append(i[2])
for i in colors:
    green.append(i[1])
plt.plot(data_set['wave'],green, '-.g')
plt.plot(data_set['wave'],blue, '-.b')
plt.plot(data_set['wave'],red, '-.r' )
plt.xlabel('wavelength')
plt.title('Color Natural')


plt.figure(4)
green = []
red = []
blue = []
for i in new_colors:
    red.append(i[0])
for i in new_colors:
    blue.append(i[2])
for i in new_colors:
    green.append(i[1])
plt.plot(data_set['wave'],green, '-.g')
plt.plot(data_set['wave'],blue, '-.b')
plt.plot(data_set['wave'],red, '-.r' )
plt.xlabel('wavelength')
plt.title('Color Modificado')


plt.figure(5)
plt.plot(data_set['wave'],data_set['intensity'], '-.', label='result')
plt.legend(loc='upper left')
plt.xlabel('wavelength')
plt.ylabel('intensity')
plt.title('Intensidad de luz vs onda ')



plt.show()