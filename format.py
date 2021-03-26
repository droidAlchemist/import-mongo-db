import json

new_data = []

# Loading or Opening the json file
with open('universities.json') as sfile:
    file_data = json.load(sfile)

    for item in file_data:
        # print(item)
        new_item = {}
        new_item["name"] = item.get("name")
        new_item["website"] = item.get("web_pages")[0]
        print(new_item)
        new_data.append(new_item)

json_object = json.dumps(new_data, indent=4)

# Writing to sample.json
with open("universities_formatted.json", "w") as outfile:
    outfile.write(json_object)
