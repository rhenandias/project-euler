#Problema 022

#Leitura de Arquivo
f = open('names.txt','r')
data = f.read()
data = data.split(",")
data = [i.replace('"', "") for i in data ]
data = sorted(data)

#Criação do dicionário
letters_dict = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0, 26):
    letters_dict[alphabet[i]] = i+1

#Calcula name score
def score(name):
    score = 0
    for i in name:
        score += letters_dict.get(i)
    return score

#Calcula scores totais
size = len(data)
scores = []
for i in range(size):
    scores.append(score(data[i]) * (i+1))

print sum(scores)