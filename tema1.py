l1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]  # o lista data
l2 = l1.copy()
l2.sort()  # lista l1 ordonata crescator
print(l2)
l2.reverse()  # lista l2 ordonata descrescator
print(l2)
print(l1[::2])  # afisez numerele din l1 cu indici pari
print(l1[1::2])  # afisez numerele din l1 cu indici impari
print(l1[::3]) # afisez numerele din l1 cu indici multipli de 3