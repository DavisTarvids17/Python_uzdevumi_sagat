"""
Izmantojot map() funkciju izveidot no diviem sarakstiem saliktnei.


"""
saraksts1 = [1, 2, 3, 4, 5]
saraksts2= ['a', 'b', 'c', 'd', 'e']

saliktenis = list(map(lambda x, y: str(x) + y, saraksts1, saraksts2))

print(saliktenis)