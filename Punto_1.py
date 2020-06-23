#primero los convierte en string 
#luego los une
def punto1():
    return(''.join(y[-1:] for y in [ str(x) for x in [123,456,789]]))
print(punto1())



