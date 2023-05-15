import re
import string 
import random

alphabet = list(string.ascii_lowercase) 


matrice_init = [] #array init
matrice_trans = [[0] * len(alphabet) for letter in alphabet] #matrice transition 0 

nb= len(open('liste.de.mots.francais.frgut.txt').readlines())

        
for n in range(len(alphabet)):

        matrice_init.append(len(re.findall('^'+alphabet[n], ''.join(str(line) for line in open('liste.de.mots.francais.frgut.txt')), re.M)) / nb)  # geration de la matrice init
        
for n  in range(len(alphabet)):
    
    nbc = len(re.findall(alphabet[n],''.join(str(line) for line in open('liste.de.mots.francais.frgut.txt'))))
    
    for i in range(len(alphabet)):
        
        comb = alphabet[n] + alphabet[i] # combinaison des deux lettres letter et la lettre a i dans l alphabet

        matrice_trans[n][i] = len(re.findall(comb,''.join(str(line) for line in open('liste.de.mots.francais.frgut.txt')))) / nbc # geration de la matrice transition

for n in range (30):
    mot=[]
    lettre_precedente = random.choices(alphabet, weights = matrice_init, k = 1)
    mot.append(lettre_precedente)

    for i in range(6):
        lettre_precedente = random.choices(alphabet, weights = matrice_trans[alphabet.index(lettre_precedente[0])], k = 1)
        mot.append(lettre_precedente)

    print(''.join(str(letter) for letter in mot))


print(' '.join('{0:.6f}'.format(item) for item in matrice_init)) #print de la matrice de init
print('\n')
print('\n'.join([' '.join(['{0:.3f}'.format(item) for item in row]) for row in matrice_trans])) #print de la matrice de transition
print('\n')
