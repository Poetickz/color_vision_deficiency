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
    data = {'r':[],'g':[],'b':[]}
    for line in lines:
        x = (line.split()[0])
        y = (line.split()[1])
        z = (line.split()[2])
        data['r'].append(x)
        data['g'].append(y)
        data['b'].append(z)
    return data

colores = get_data_from_file('colors_special.txt')

f= open("colores_js.txt","w+")

cont = 0
for r,g,b in zip(colores['r'], colores['g'], colores['b']):
    f.write("["+str(r)+","+str(g)+","+str(b)+"]"+','+"\n")
    cont += 1
print(cont)
print(len(colores['r']))
f.close()