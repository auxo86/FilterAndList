lista = [(1, '明旭'), (2, '慧枚'), (3, '桂香'), (4, '詠馨'), (5, '至誠'), (6, '姵君'), (7, '小雅'), (8, '薇雅'), (9, '鈺螢'), (10, '小馮'), (11, '孟慧'), (12, '雨潔'), (13, '淑慧'), (14, '翠妹'), (15, '明旭')]
i =  0

print(list(filter(lambda a: a[1] == '明旭', lista)))


#lista = [6,5,4,3,2,1,6,5,4,3,2,1]
#print(list(filter(lambda a: a[1] == 2, enumerate(lista))))