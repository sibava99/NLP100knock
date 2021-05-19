str1 = 'paraparaparadise'
str2 = 'paragraphe'
X = []
Y = []

for i in range(len(str1)-1):
    X.append(str1[i:i+2])
for i in range(len(str2)-1):
    Y.append(str2[i:i+2])

sX = set(X)
sY = set(Y)
print(sX | sY)
print(sX - sY)
print(sY - sX)
print(sX & sY)