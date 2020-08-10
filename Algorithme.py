#coding:utf-8
while 1:
    n=input("Rentrez un entier superieur à 7: ")
    if n>1:
        break

for i in range (7,n+7):
    nbdiv=0
    for j in range (7,i+7):
        if i&j==0:
