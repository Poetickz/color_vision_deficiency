from statistics import mean 
import math

def get_data_from_file(file):
    f = open(file, "r")
    lines = f.readlines()
    data = {}
    for line in lines:
        x = float(line.split()[0])
        y = float(line.split()[1])
        data[x]=y
    return data

data = get_data_from_file('data.txt')

avg_data = {}
for wave, intensity in data.items():
    round_wave = math.floor(wave)
    if round_wave in avg_data:
        avg_data[round_wave].append(intensity)
    else:
        avg_data[round_wave] = [intensity]

result = {}
for wave, intensity_list in avg_data.items():
    mean_value = mean(intensity_list)
    result[wave] = 0 if mean_value<0 else mean_value

f= open("refactored_data.txt","w+")

for wave, intensity in result.items():
    f.write(str(wave)+"\t"+str(intensity)+"\n")

f.close()
print(result)