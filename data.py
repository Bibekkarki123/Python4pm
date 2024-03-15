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

data = [
    [
        {
            'name':"ram",
            'age': 20
        },
        {
            'name':"sita",
            'age': 20
        }
    ],
    [
        {
            'name':"hari",
            'age': 20
        },
        {
            'name':"gita",
            'age': 20
        }
    ]
]
print(data[0][0]['name'],data[0][0]['age'])
print(data[0][1]['name'],data[0][1]['age'])
print(data[1][0]['name'],data[1][0]['age'])
print(data[1][1]['name'],data[1][1]['age'])

del data[0][0]['age']
del data[0][1]['age']
del data[1][0]['age']
del data[1][1]['age']
print(data)