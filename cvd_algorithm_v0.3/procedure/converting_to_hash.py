
def get_hsl_from_file(file):
    f = open(file, "r")
    lines = f.readlines()
    data = { }
    for line in lines:
        x = int(line.split()[0])
        y = float(line.split()[1])
        data[x] = y
    return data

f = open("hash_hsl.txt","w+")
data = get_hsl_from_file("resume_hsl.txt")

cont = 0

for hue, intensity_array in data.items():
    if (cont == 10):
        f.write("\n")
        cont = 0
    f.write(str(hue)+":"+str(intensity_array)+", ")
    cont += 1

f.close()