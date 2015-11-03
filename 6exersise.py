data = open('en-ru.txt', 'r')
lines = data.readlines()
lines = list (map (lambda x: x.rstrip(), lines))
lines = list (map (lambda x: x.split('-'), lines))
lines.pop()
dictionary = dict(lines)
enru = dict(lines)
data.close()
data = open('ru-en.txt', 'r')
lines = data.readlines()
lines = list (map (lambda x: x.rstrip(), lines))
lines = list (map (lambda x: x.split('-'), lines))
lines.pop()
dictionary = dict(lines)
ruen = dict(lines)
data.close()
for word in enru:
    if enru[word] not in ruen:
       ruen[enru[word]] = word
    elif ruen[enru[word]] != word:
       enru[word] += (', ' + ruen[enru[word]])
       ruen[enru[word]] += (', ' + word)
data.close()
       
