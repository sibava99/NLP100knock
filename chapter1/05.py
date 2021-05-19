s = 'I am an NLPer'
w_list = s.split()
cons = s.replace(' ','')

c_bigram = [] 
w_bigram = []

for i in range(len(cons)):
    c_bigram.append(cons[i:i+2])

for i in range(len(w_list)-1):
    w_bigram.append(str(w_list[i]) + str(w_list[i+1]))

print(c_bigram)
print(w_bigram)