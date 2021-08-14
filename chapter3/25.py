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
    pat = r'\{\{基礎情報 国\n(\|\s*.*? = .*?\n)*\}\}'
    print(re.findall(pat,uk_txt))