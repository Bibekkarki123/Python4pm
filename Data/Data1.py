students = [
    {
        'name':"Ram",
        "country":[
            {
                'name':"Nepal",
                 'capital':"Kathmandu"
            },
            {
                'name':"India",
                 'capital':"Delhi"
            }
        ]
    },
    {
        'name':"Sita",
        "country":[
            {
                'name':"Nepal",
                 'capital':"Pokhara"
            },
            {
                'name':"China",
                 'capital':"Beijing"
            }
        ]
    }
]
print("My name is",students[0]['name'],"permanently living in",students[0]["country"][0]['name'],"on",students[0]["country"][0]['capital']+".")
print("My name is",students[0]['name'],"temporarily living in",students[0]["country"][1]['name'],"on",students[0]["country"][1]['capital']+".")
print("My name is",students[1]['name'],"permanently living in",students[1]["country"][0]['name'],"on",students[1]["country"][0]['capital']+".")
print("My name is",students[1]['name'],"temporarily living in",students[1]["country"][1]['name'],"on",students[1]["country"][1]['capital']+".")

del students[0]['country'][0]['capital']
del students[0]['country'][1]['capital']
del students[1]['country'][0]['capital']
del students[1]['country'][1]['capital']
print(students)

