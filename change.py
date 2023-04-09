import json

with open("old_data.json", "r", encoding="UTF-8") as IF:
    data = json.load(IF)

new_data = {}

for faculcy in data:

    try:
        new_data[faculcy]
    except:
        new_data[faculcy] = {}

    for course in data[faculcy]:

        try:
            new_data[faculcy][course]
        except:
            new_data[faculcy][course] = []

        for group_name in data[faculcy][course]:

            new_data[faculcy][course].append(group_name)

with open("data.json", "w", encoding="UTF-8") as OF:
    json.dump(new_data, OF, ensure_ascii=False, indent=4, sort_keys=False)
