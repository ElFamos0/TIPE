'''
Malo DAMIEN MP Fabert
Sujet de type : cryptographie (RSA et fonction de hashage)
'''
import random

def generecle(tailleenbit=1024):
    #p = 23
    #q = 19   
    #On génère nos deux nombre premiers.
    p = grandnombrepremier(tailleenbit)
    q = grandnombrepremier(tailleenbit)
    print("p = ", p)
    print("q = ",q)
    n = p*q
    phiN = (p-1)*(q-1)
    #choisir e
    # e est premier avec phiN
    while True:
        e = random.randrange(2 ** (tailleenbit - 1), 2 ** tailleenbit - 1)
        if(coprem(e,phiN)):
            break
    d = inversemodule(e,phiN)
    print("e = ",e)
    print("phiN = ",phiN)
    print("d = ",d)
    print("n = ",n)
    return e,d,n
    
def inversemodule(e,phiN):
    pgcd, x, y = euclideetendu(e,phiN)
    
    if x < 0:
        x += phiN
    return x
    
def euclideetendu(a,b): #cf algo euclide étendue sur wikipédia 
    r = b 
    rr = a
    u = 0
    uu = 1 
    v = 0
    vv = 1 
    while r != 0:
        q = rr//r
        rr, r = r, rr - q*r
        uu, u = u, uu - q*u
        vv, v = v, vv - q*v
    
    return rr, uu, vv

    
def coprem(p,q):
    #On retourne True si le pgcd vaut 1
    while q:
        p, q = q, p%q
    return p == 1


def estpremier(nombre):
    
    if nombre < 2:
        return False
    petitpremiers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    if  nombre in petitpremiers:        
        return True
    for premier in petitpremiers:
        if nombre % premier == 0:
                return False       #si un des premiers divise notre liste
    return True #si le nombre passe tout les tests on a de grandes chances qu'il soit premier
    
def cryptage(msg,e,n):
    crypte = ""
    for c in msg:
        m = ord(c)
        crypte += str(pow(m,e,n)) + " " #afin de pouvoir plus simplement diviser quand on voudra déchiffrer
    return crypte

def cryptage2(msg,e,n):
    n = len(msg)
    listecryptage = []
    listecrypte=[]
    listecrypteRSA=[]
    for i in range(n//10):
        listecryptage.append(msg[i*10:(i+1)*10])
    listecryptage.append(msg[n-n%10:n])
    print(listecryptage)
    for item in listecryptage:
        somme = 0
        for indices in range(len(item)):
            somme += ord(item[indices])*2**(8*(9-indices))
        listecrypte.append(somme)
    for item in listecrypte:
        listecrypteRSA.append(pow(item,e,n))
    return listecrypteRSA
    

def cryptage3(msg,e,n):
    l = [x for x in bytes(msg, encoding="utf8")]
    listecryptage=[]
    for i in range(len(l)//3):
        listecryptage.append(l[i*3:(i+1)*3])
    listecryptage.append(l[len(l)-len(l)%3:len(l)])
    
    
    crypte = []
    listecrypteRSA = []
    
    for item in listecryptage:
        somme = 0
        for i in range(0,len(item)):
            somme += (item[i])*2**(8*(2-i))
        crypte.append(somme)
    for item in crypte:
        listecrypteRSA.append(pow(item,e,n))
        
    print(listecryptage)
    print(crypte)
    print(listecrypteRSA)
    return listecrypteRSA

        
    
def decryptage3(crypte,d,n):
    decrypte = []
    msg = ''
    for item in crypte:
        decrypte.append(pow(item,d,n))
    for item in decrypte:
        l = []
        for i in range(3):
            element = item//(2**((2-i)*8))
            l.append(element)
            item = item%(2**((2-i)*8))
        print(l)
        msg += str(bytes(l),encoding="utf-8")
        

def decryptage(crypte,d,n):
    global a, b, c
    msg = ""
    crypte2 = crypte.split()
    for c in crypte2:
        m = int(c)
        msg += chr(pow(m,d,n))
    return msg
    
# def decryptage2(crypte,d,n): #Mauvaise tentatve 
#     decrypte = []
#     for item in crypte:
#         decrypte.append(pow(item,d,n)
#     for item in decrypte:
#         for i in range(10):
#             lettre = chr(item//2**(10-i))
#             decrypte += lettre
#             item -= (item//2**(10-i)) * 2**(10-i)
#     return decrypte
        
def grandnombrepremier(tailleenbit=1024): #mettre une taille de 1024 bit si pas de taille de clé donnée
    while True:
        nombre = random.randrange(2**(tailleenbit-1),(2**tailleenbit)-1) #permet d'avoir un nombre entre 308 et 309 chiffres
        if (estpremier(nombre)):
            return nombre

if __name__ == '__main__':
    tailleenbit = int(input("Taille de votre clé : "))
    e,d,n = generecle(tailleenbit)
    msg = "bonjour je suis malo"

    crypt = cryptage3(msg,e, n)
    print(crypt)
    dec = decryptage3(crypt,d, n)
    print(dec)

