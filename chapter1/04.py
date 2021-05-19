word_list = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".replace('.','').split()
num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
#elemental_list = [''] * len(word_list)
element_dict = {}

for i in range(0,len(word_list)):
    if i+1 in num_list:
        #elemental_list[i] = word_list[i][0]
        element_dict[word_list[i][0]] = i
    else:
        #elemental_list[i] = word_list[i][0:2]
        element_dict[word_list[i][0:2]] = i
        
print(element_dict)