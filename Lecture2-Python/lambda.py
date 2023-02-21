people = [
    {'name': 'harry', 'house': 'gryffindor'},
    {'name': 'cho', 'house': 'ravenclaw'},
    {'name': 'draco', 'house': 'slytherin'}
]

# be able to sort dicts
# def f(person):
#     return person['name'] 


# people.sort(key=f)

# another alternative using lambda expression into one line
people.sort(key=lambda person: person['name'])

print(people)