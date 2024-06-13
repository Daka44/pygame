f = open('score', 'w')
f.write('10')
f.close()

f = open('score', 'r')
s = f.readline()
print(s)
f.close()
