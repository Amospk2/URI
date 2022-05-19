#	Criptografia

qtd_problemas = int(input(""))

problemas = []

for i in range(qtd_problemas):
  problemas.append(input(""))




def trata_string(string):
  lista = []

  for letra in string:
    lista.append(letra)


  for count, item in enumerate(lista):
    lettle_replace = chr(ord(item)+3)
    if item.isalpha():
      lista[count] = lettle_replace

  lista.reverse()
  tamanho = int(len(string)/2)

  while(tamanho < len(lista)):
    lettle_replace = chr(ord(lista[tamanho])-1)
    lista[tamanho] = lettle_replace
    tamanho+=1

  return ''.join(lista)


for palavra in problemas:
  print(trata_string(palavra))
