with open("Denemee.txt", encoding="utf-8") as f_in:
    lines = (line.split('\n') for line in f_in)
    lines = list(line for line in lines if line)

print (lines)