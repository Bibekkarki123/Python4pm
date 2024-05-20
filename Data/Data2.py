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
