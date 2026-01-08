import random
import string

letters=string.ascii_letters

l=""
counter=0
while l !="w":
    l=random.choice(letters)
    print(f"la lettre choise est {l}")
    counter+=1

    print(f"le nombre de tirage effectuée est {counter}")
