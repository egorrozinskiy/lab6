'''
Задача A
++++++++

В массиве ровно два элемента равны. Найдите эти элементы.

Программа получает на вход число N, в следующей строке заданы N элементов списка через пробел.

Выведите значение совпадающих элементов.

+-------------+-------+
| Ввод        | Вывод |
+=============+=======+
| 6           | 5     |
+-------------+-------+
| 8 3 5 4 5 1 |       |
+-------------+-------+
'''
input=open('input.txt', 'r')
output=open('output.txt', 'w')
N=int(input())
A=list(map(int, input.readline().split()))
for i in range (N):
    A[i]=int(A[i])
A.append(' ')
for i in range(N):
    for j in range(i+1, N):
        if A[i]==A[j]:
            output.write(str(A[i]))
            break
output.close()        
    
