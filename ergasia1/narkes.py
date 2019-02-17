import random

mines = int(input("Vale ton ari8mo ton stylvn grammvn  \n me ti 8es na pai3eis ?.\n\t"))

array = [0] * 100

for i in range(mines):
    j = random.randint(0,99)
    array[j] = 'x'
print(array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7],array[8],array[9],"\n",\
      array[10],array[11],array[12],array[13],array[14],array[15],array[16],array[17],array[18],array[19],"\n",\
      array[20],array[21],array[22],array[23],array[24],array[25],array[26],array[27],array[28],array[29],"\n",\
      array[30],array[31],array[32],array[33],array[34],array[35],array[36],array[37],array[38],array[39],"\n",\
      array[40],array[41],array[42],array[43],array[44],array[45],array[46],array[47],array[48],array[49],"\n",\
      array[50],array[51],array[52],array[53],array[54],array[55],array[56],array[57],array[58],array[59],"\n",\
      array[60],array[61],array[62],array[63],array[64],array[65],array[66],array[67],array[68],array[69],"\n",\
      array[70],array[71],array[72],array[73],array[74],array[75],array[76],array[77],array[78],array[79],"\n",\
      array[80],array[81],array[82],array[83],array[84],array[85],array[86],array[87],array[88],array[89],"\n",\
      array[90],array[91],array[92],array[93],array[94],array[95],array[96],array[97],array[98],array[99],"\n")
NUM = 0
i = 0
while i <= 99:
    if array[i] != 'x':
        if i == 0:
            if array[1] == 'x':
                NUM = NUM + 1
            if array[10] == 'x':
                NUM = NUM + 1
            if array[11] == 'x':
                NUM = NUM + 1
        elif i == 9:
            if array[8] == 'x':
                NUM = NUM + 1
            if array[18] == 'x':
                NUM = NUM + 1
            if array[19] == 'x':
                NUM = NUM + 1
        elif i == 90:
            if array[80] == 'x':
                NUM = NUM + 1
            if array[81] == 'x':
                NUM = NUM + 1
            if array[91] == 'x':
                NUM = NUM + 1
        elif i == 99:
            if array[88] == 'x':
                NUM = NUM + 1
            if array[89] == 'x':
                NUM = NUM + 1
            if array[98] == 'x':
                NUM = NUM + 1
        elif i >= 1 and i <= 8:
            if array[i-1] == 'x':
                NUM = NUM + 1
            if array[i+1] == 'x':
                NUM = NUM + 1
            if array[i+9] == 'x':
                NUM = NUM + 1
            if array[i+10] == 'x':
                NUM = NUM + 1
            if array[i+11] == 'x':
                NUM = NUM + 1
        elif i >= 91 and i <= 98:
            if array[i-11] == 'x':
                NUM = NUM + 1
            if array[i-10] == 'x':
                NUM = NUM + 1
            if array[i-9] == 'x':
                NUM = NUM + 1
            if array[i-1] == 'x':
                NUM = NUM + 1
            if array[i+1] == 'x':
                NUM = NUM + 1
        elif i % 10 == 0:
            if array[i-10] == 'x':
                NUM = NUM + 1
            if array[i-9] == 'x':
                NUM = NUM + 1
            if array[i+1] == 'x':
                NUM = NUM + 1
            if array[i+10] == 'x':
                NUM = NUM + 1
            if array[i+11] == 'x':
                NUM = NUM + 1
        elif (i+1) % 10 == 0:
            if array[i-11] == 'x':
                NUM = NUM + 1
            if array[i-10] == 'x':
                NUM = NUM + 1
            if array[i-1] == 'x':
                NUM = NUM + 1
            if array[i+9] == 'x':
                NUM = NUM + 1
            if array[i+10] == 'x':
                NUM = NUM + 1
        else:
            if array[i-11] == 'x':
                NUM = NUM + 1
            if array[i-10] == 'x':
                NUM = NUM + 1
            if array[i-9] == 'x':
                NUM = NUM + 1
            if array[i-1] == 'x':
                NUM = NUM + 1
            if array[i+1] == 'x':
                NUM = NUM + 1
            if array[i+9] == 'x':
                NUM = NUM + 1
            if array[i+10] == 'x':
                NUM = NUM + 1
            if array[i+11] == 'x':
                NUM = NUM + 1
        array[i] = NUM
    i += 1
    NUM = 0
print(array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7],array[8],array[9],"\n",\
      array[10],array[11],array[12],array[13],array[14],array[15],array[16],array[17],array[18],array[19],"\n",\
      array[20],array[21],array[22],array[23],array[24],array[25],array[26],array[27],array[28],array[29],"\n",\
      array[30],array[31],array[32],array[33],array[34],array[35],array[36],array[37],array[38],array[39],"\n",\
      array[40],array[41],array[42],array[43],array[44],array[45],array[46],array[47],array[48],array[49],"\n",\
      array[50],array[51],array[52],array[53],array[54],array[55],array[56],array[57],array[58],array[59],"\n",\
      array[60],array[61],array[62],array[63],array[64],array[65],array[66],array[67],array[68],array[69],"\n",\
      array[70],array[71],array[72],array[73],array[74],array[75],array[76],array[77],array[78],array[79],"\n",\
      array[80],array[81],array[82],array[83],array[84],array[85],array[86],array[87],array[88],array[89],"\n",\
      array[90],array[91],array[92],array[93],array[94],array[95],array[96],array[97],array[98],array[99])
