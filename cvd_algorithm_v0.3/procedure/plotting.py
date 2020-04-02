import matplotlib.pyplot as plt

def get_data_from_file_intensity(file):
    f = open(file, "r")
    lines = f.readlines()
    data = {'wave':[], 'intensity':[]}
    for line in lines:
        x = float(line.split()[0])
        y = float(line.split()[1])
        data['wave'].append(x)
        data['intensity'].append(y)
    return data

data = get_data_from_file_intensity("resume_hsl.txt")
plt.figure(1)
plt.plot(data['wave'],data['intensity'], '.b')
plt.xlabel('hue')
plt.ylabel('intensity')
plt.title('Color Modificado')
plt.show()