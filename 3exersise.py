data = open('input.txt', 'r')
line = data.read()
line =  line.replace('.', ' ')
line = line.replace('!', ' ')
line = line.replace('?', ' ')
line = line.replace(',',' ')
lines = line.split()
dictionary = {}
for words in lines:
    word = words.lower()
    if word in dictionary:
       dictionary[word] += 1
     else:
       dictionary[word] = 1
maximum = max(list(dictionary.values()))
for key in dictionary:
    if dictionary[key] == maximum:
       print ((key, maximum))
