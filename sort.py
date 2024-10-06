lines = []
with open("USDA_PDP_AnalyticalResults.csv", "r")as file:
    for line in file.readlines()[1:]:
        A = line.split(",")
        lines.append(A)
lines.sort(key=lambda x: (int(x[0][2:4]), int(x[0][4:6]), x[0][:2]))

with open("sortedCSV.csv", "w") as sFile:
    for line in lines:
        sFile.write(",".join(line))
