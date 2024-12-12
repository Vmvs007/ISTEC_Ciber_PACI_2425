palavras = ["maçã", "banana", "laranja", "maçã", "laranja", "laranja"]

dicionario={}

for palavra in palavras:
    if (palavra not in dicionario):
        dicionario[palavra]=1
    else:
        dicionario[palavra]+=1

print(dicionario)