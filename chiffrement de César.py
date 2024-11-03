L = list(map(chr, range(65, 91)))
LL = []
resultat = ""
text = input(" entrez le text : ")
d = int(input(" entrez le cle : "))
ch = ''.join(text.split())

for i in text :
    if i !=' ' :
     c = (L.index(i) + d) % 26
     resultat +=L[c]
    else:
        resultat +=" "
dec = ""
for j in resultat :
    if j !=' ' :
     c = (L.index(j) - d) % 26
     dec +=L[c]
    else:
        dec +=" "

print("Texte chiffré :", resultat)
print("\nTexte dechiffré :", dec)
