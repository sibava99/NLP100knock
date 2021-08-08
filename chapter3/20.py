import json

dict = {}
uk_txt = ""
with open('jawiki-country.json') as f:
    for l in f:
        dict = json.loads(l)
        if (dict["title"] == "イギリス"):
            uk_txt = dict["text"]
            break
    print(uk_txt)
