#1026	Carrega ou não Carrega?
def soma_bits():
    

    vai_um = 0
    res_soma = list()
    
    for pos in range(len(a)-1, -1, -1):
        
        
        if(a[pos] == "0" and b[pos] == "0"):
              vai_um = 0
              res_soma.append("0")
                
        elif((a[pos] == "1" and b[pos] == "0") or (a[pos] == "0" and b[pos] == "1")):
              res_soma.append("1")
             
        else:
              res_soma.append("0")



    return res_soma



def binarioToDecimal(a):
  decimal = 0
  for count, item in enumerate(a):
    decimal += 2**count * int(item)

  return decimal

while True:
  try:
    a = int(input(""))
    b = int(input(""))


    a = str(format(a, "b"))
    b = str(format(b, "b"))

    if len(a) > len(b):
      t = len(a) - len(b)
      b = t * '0' + b
    elif len(b) > len(a):
      t = len(b) - len(a)
      a = t * '0' + a
    
    print(a, b)



    soma = ''.join(soma_bits())

    print(binarioToDecimal(soma))

  except EOFError:
    break
