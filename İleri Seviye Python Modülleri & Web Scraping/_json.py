import json

person_string = '{"name":"talha", "languages":["python","C#"]}'
person_dict = {"name": "talha","languages": ["python","C#"] }


# JSON STRİNG TO DİCT
# result = json.loads(person_string) #loads metodu:JSON formatlı bir metin dizisini (string) alıp, onu karşılık gelen bir Python nesnesine (genellikle bir sözlük veya liste) dönüştürmek için kullanılır.
# result = result["name"] 
# result = result["languages"]

# with open("person.json") as f:
#     data = json.load(f) #load:JSON formatlı veriyi doğrudan bir dosya nesnesinden okumak ve okunan bu veriyi karşılık gelen bir Python nesnesine (genellikle bir sözlük veya liste) dönüştürmek için kullanılır.
#     print(data["name"])
#     print(data["languages"])




# DİCT TO JSON STRİNG
# result = json.dumps(person_dict) #dumps:bir Python nesnesini (örneğin bir sözlük veya liste) alıp, onu JSON formatlı bir metin dizisine (string) serileştirmek için kullanılır.
# print(result)
# print(type(result))

# with open("person.json","w") as f:
#     json.dump(person_dict, f)

person_dict = json.loads(person_string)


result = json.dumps(person_dict, indent= 4, sort_keys= True)
print(person_dict)
print(result)