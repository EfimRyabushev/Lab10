data = open('en-ru.txt', 'r')
lines = data.readlines()
lines = list (map (lambda x: x.rstrip(), lines))
lines = list (map (lambda x: x.split('-'), lines))
lines.pop()
dictionary = dict(lines)
data = open('input.txt', 'r')
lines = data.read()
lines = lines.replace('.', ' ')
lines = lines.replace('!', ' ')
lines = lines.replace('?', ' ')
lines = lines.replace(',',' ')
lines = lines.split()
for i in range(len(lines)):
    
    if lines[i].lower() in dictionary:
       lines[i] = dictionary[lines[i].lower()]
output = open('output.txt', 'w')
output.write(str (lines))
data.close()
output.close()
