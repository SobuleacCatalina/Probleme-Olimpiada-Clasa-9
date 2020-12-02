"""
La o ferma avicola sunt x pasari. Jumatate din acestea sunt gaini. Numarul ratelor constituie un sfert din numarul gainilor. Celelalte sunt 
gaste. Scrieti un program care citeste de la tastatura numarul total de pasari si afiseaza numarul de gaini, rate si gaste.
"""
t=eval(input("Introdu numarul total de pasari: "))
print("gaini - ",t//2,",rate - ",(t//2)//4,",gaste - ",t-(((t//2)//4)+t//2))