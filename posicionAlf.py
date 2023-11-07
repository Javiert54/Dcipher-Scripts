abc="abcdefghijklmnopqrstuvwxyz"
txt ="6 12 1 7 16 1 20 9 14 5 20 5 14 5 7 18 15"
txtArr=[]

txtArr=txt.split(" ")
sol=""
for number in txtArr:
    sol+=abc[int(number)-1]
    print(abc[int(number)-1])
print(sol)