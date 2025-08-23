student = ['Joseph', 'Lico', 'Misal', 'Herald']

#///ANG NAME RA NIMO I PRINT///
# for name in student: 
#     print (name)

for number, name in enumerate(student, start=1): # ENUMERATE if gusto nimo makita ang numbering sa bawat name ika-pila sa list
    print(f"{number}. {name}")