data = [{
    "name" : "prashanth",
    "age" : "54"
},
{
    "name" : "Kareem",
    "age" : "54"
}]

def extract_name(details):
    name_1 = details[0]["name"]
    name_2 = details[1]["name"]
    return[name_1, name_2]

def extract_age(details):
    age_1 = details[0]["age"]
    age_2 = details[1]["age"]
    return[age_1, age_2]

names = extract_name(data)
print(names)

ages = extract_age(data)
print(ages)