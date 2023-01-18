# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]
# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

data=[12,'sadf',5643,'girl',3456,45,'happy','new year']
digits=list(filter(lambda x:type(x)==int,data))
stroki=list(filter(lambda x:type(x)==str,data))

print(digits)
print(stroki)
