#Dictionaries is more like a list but then
name = dict()
name['oluwarotimi'] = 2002
name['aduramigba'] = 1992
name['oluwatoyosi'] = 2003

# print(name)

# if 'oluwarotimi' in name :
#     print('true')
# else:
#     print('false')

# age = dict()
# ageInput = int(input('How old are you?  '))
# yearInput = int(input('What year were you born? '))

# age[yearInput] = ageInput

# print(age)

# nameVals = list(name.values())

# print(nameVals)

word = 'bronstosaurus'
d = dict()
for c in word :
    if c not in d :
        d[c] = 1
    else:
        d[c] = d[c] + 1 
print(d)