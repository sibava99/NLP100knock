import json
import re
dict = {}
uk_txt = ""
with open('jawiki-country.json') as f:
    for l in f:
        dict = json.loads(l)
        if (dict["title"] == "イギリス"):
            uk_txt = dict["text"]
            break
    pat = r'={2,5}.*={2,5}'
    cat_list = re.findall(pat,uk_txt)
    for l in cat_list:
        level = l.count('=') / 2
        print(l.replace('=',''),int(level))