
def sequencia(i,j):
  maior = 1
  for n in range(i,j + 1):
      iteração = 1
      while n != 1:
          if n % 2 == 0:
              n = n /2
              iteração += 1
          else:
              n = n * 3  + 1
              iteração += 1
      if iteração > maior:
          maior = iteração
  return print("{} {} {}" .format(i , j , maior))


while True:
  try:
    i, j = input("").split()
    i, j = int (i),int(j)
    sequencia(i,j)
  except EOFError:
    break
 



  # x = 0
  # y = 1
  # i = entrance[x]
  # j = entrance[y]

  # for m in entrance:
  #   maior = 0
  #   if y <= len(entrance):
  #     i = entrance[x]
  #     j = entrance[y]
  #     for n in range(i,j + 1):
  #         iteração = 1
  #         while n != 1:
  #             if n % 2 == 0:
  #                 n = n /2
  #                 iteração += 1
  #             else:
  #                 n = n * 3  + 1
  #                 iteração += 1
  #         if iteração > maior:
  #             maior = iteração
  #     print(f"{i} {j} {maior}")

  #     y += 2
  #     x += 2



  # while True:
  # try:
  #   a, b = input("").split()
  #   print("teste")
  # except EOFError:
  #   break
  # maior = 1
  # respostas = []
  # for n in range(i,j + 1):
  #     iteração = 1
  #     while n != 1:
  #         if n % 2 == 0:
  #             n = n /2
  #             iteração += 1
  #         else:
  #             n = n * 3  + 1
  #             iteração += 1
  #     if iteração > maior:
  #         maior = iteração
  # print("{} {} {}" .format(i , j , maior))
