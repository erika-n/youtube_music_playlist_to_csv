import glob, os
import re
import csv
import pandas as pd



def processFile(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()

    data = []

    dataline = []
    curstr = ""
    for line in lines:
        line = line.strip()
        if line ==  "&":
            curstr = dataline.pop()
            curstr += " & "
            continue
        elif line == ',':
            curstr = dataline.pop()
            curstr += ", "
            continue
        elif len(line) > 0:
            curstr += line
            dataline.append(curstr)
            curstr = ""
        if(re.match(r'\d+\:\d+', line)):

            data.append(dataline)
            if len(dataline) < 4:
                dataline.insert(-1, "")

            if len(dataline) < 4 or len(dataline) > 4:
                print(dataline)
            dataline = []


    df = pd.DataFrame(data, columns=['Title', 'Artist', 'Album', 'Time'])
    csv_file = filename[:-4] + '.csv'
    df.to_csv(csv_file, index=False,encoding='utf-8-sig')


for file in glob.glob("*.txt"):
    print('processing file', file)
    processFile(file)

