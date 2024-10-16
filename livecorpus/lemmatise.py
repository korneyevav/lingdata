timecodesetc = """""".split('\n')

mystem = """""".split('\n')

toimport = ""

for i in range(0, len(timecodesetc)):
    toimport += timecodesetc[i] + '\t' + mystem[i] + "\n"

with open("elanimport.txt", "w") as file:
    file.write(toimport)
