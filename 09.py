s = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
w_list = s.split()
print(w_list)
for i in range(len(w_list)):
    if (len(w_list[i]) > 4):
        w_list[i] = w_list[i][-1] + w_list[i][1:len(w_list[i])-1] + w_list[i][0]
print(' '.join(w_list))
