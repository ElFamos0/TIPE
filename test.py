msg = "boujour je suis malo damien"
n = len(msg)
listecryptage = []
listecrypte=[]
somme = 0 

for i in range(n//10):
    listecryptage.append(msg[i*10:(i+1)*10])
listecryptage.append(msg[n-n%10:n])
print(listecryptage)
for item in listecryptage:
    somme = 0
    for indices in range(len(item)):
        somme += ord(item[indices])*2**(8*(9-indices))
    listecrypte.append(somme)
print(listecrypte)

    

bytes('Malo', encoding="utf8")
Out[64]: b'Malo'

In [65]: b = bytes('Malo', encoding="utf8")

In [66]: for x in b: print(x)
    ...: 
77
97
108
111

In [67]: bytes('Malo', encoding="utf8")
Out[67]: b'Malo'

In [68]: bytes('Mélo', encoding="utf8")
Out[68]: b'M\xc3\xa9lo'

In [69]: b = bytes('Mélo', encoding="utf8")

In [70]: for x in b: print(x)
    ...: 
77
195
169
108
111

In [71]: list(bytes('Mélo', encoding="utf8"))
Out[71]: [77, 195, 169, 108, 111]

In [72]: [x for x in bytes('Mélo', encoding="utf8"]
  File "<ipython-input-72-2033157b1c45>", line 1
    [x for x in bytes('Mélo', encoding="utf8"]
                                             ^
SyntaxError: invalid syntax


In [73]: [x for x in bytes('Mélo', encoding="utf8")]
Out[73]: [77, 195, 169, 108, 111]

In [74]: [bin(x) for x in bytes('Mélo', encoding="utf8")]
Out[74]: ['0b1001101', '0b11000011', '0b10101001', '0b1101100', '0b1101111']

In [75]: [bin(x)[2:] for x in bytes('Mélo', encoding="utf8")]
Out[75]: ['1001101', '11000011', '10101001', '1101100', '1101111']

In [76]: ".".join([bin(x)[2:] for x in bytes('Mélo', encoding="utf8")])
Out[76]: '1001101.11000011.10101001.1101100.1101111'

In [77]: b = bytes('Mélo', encoding="utf8")

In [78]: b
Out[78]: b'M\xc3\xa9lo'

In [79]: [65,66,67,68]
Out[79]: [65, 66, 67, 68]

In [80]: bytes([65,66,67,68])
Out[80]: b'ABCD'

In [81]: b = bytes([65,66,67,68])

In [82]: b = bytes('Mélo', encoding="utf8")

In [83]: [bin(x) for x in bytes('Mélo', encoding="utf8")]
Out[83]: ['0b1001101', '0b11000011', '0b10101001', '0b1101100', '0b1101111']

In [84]: [x for x in bytes('Mélo', encoding="utf8"]
  File "<ipython-input-84-2033157b1c45>", line 1
    [x for x in bytes('Mélo', encoding="utf8"]
                                             ^
SyntaxError: invalid syntax


In [85]: [x for x in bytes('Mélo', encoding="utf8")]
Out[85]: [77, 195, 169, 108, 111]

In [86]: l = [x for x in bytes('Mélo', encoding="utf8")]

In [87]: l
Out[87]: [77, 195, 169, 108, 111]

In [88]: bytes(l)
Out[88]: b'M\xc3\xa9lo'

In [89]: string(bytes(l), encoding="utf8")
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-89-ad30c04d1ff1> in <module>()
----> 1 string(bytes(l), encoding="utf8")

NameError: name 'string' is not defined

In [90]: str(bytes(l), encoding="utf8")
Out[90]: 'Mélo'

In [91]: 