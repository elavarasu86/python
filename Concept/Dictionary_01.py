#1 - Values()

users: dict = {101:'facebook',102:'Linkedin',103:'X'}
#List of values will be printed  which can be used to iterate.
print(users.values())
#dict_values(['facebook', 'Linkedin', 'X'])

#2 - Keys()
#List of keys will be printed which can be used to iterate.
print(users.keys())
#dict_keys([101, 102, 103])

#3 - Pop()
# Pop allow us to remove a key and its value by passing key in pop function.
users.pop(103)
print(users)
#{101: 'facebook', 102: 'Linkedin'}

#4 - popitem()
#Similar to pop, this function will remove last item in the dictionary.
users.popitem()
print(users)
#{101: 'facebook'}

#5 - Copy()
sample_dict: dict = {0:['a','b'],1:['c','d']}
my_copy: dict =sample_dict.copy()
print(sample_dict)
print(my_copy)
#{0: ['a', 'b'], 1: ['c', 'd']}
#{0: ['a', 'b'], 1: ['c', 'd']}

print(id(sample_dict))
print(id(my_copy))
#1616789549504
#1616789004992
# Below is a shallow copy
my_copy[0][0]='!!!'
print(sample_dict)
print(my_copy)
#{0: ['!!!', 'b'], 1: ['c', 'd']}
#{0: ['!!!', 'b'], 1: ['c', 'd']}


#6 - get()
print(users.get(101))
#facebook
print(users.get(102,'Missing value'))
#Missing value

#7 - setdefault()
print(users.setdefault(101,'missing social media'))
#facebook
print(users.setdefault(999,'Missing social media'))
#Missing social media
print(users)
#{101: 'facebook', 999: 'Missing social media'}

#8 - clear()

users.clear()
print(users)
#{}

#9 - fromkeys()
socialMedia: list[str] =['facebook','Linkedin','X']
users: dict =dict.fromkeys(socialMedia)
print(users)
#{'facebook': None, 'Linkedin': None, 'X': None}
users:dict =dict.fromkeys(socialMedia,'Unknown')
print(users)
#{'facebook': 'Unknown', 'Linkedin': 'Unknown', 'X': 'Unknown'}

#10 - items()

print(users.items())
#dict_items([('facebook', 'Unknown'), ('Linkedin', 'Unknown'), ('X', 'Unknown')])

#11 - update()

users.update({'X':'Twitter'})
print(users)
#{'facebook': 'Unknown', 'Linkedin': 'Unknown', 'X': 'Twitter'}