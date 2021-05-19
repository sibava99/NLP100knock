def cipher(s):
    ret = [] 
    for c in s:
        if c.islower:
            ret.append(219 - ord(c))
        else:
            ret.append(ord(c))
    return ret

def re_cipher(l):
    ret = ''
    for i in l:
        ret += chr(219 -i)
    return ret

print(cipher('abc'))
print(re_cipher(cipher('abc')))