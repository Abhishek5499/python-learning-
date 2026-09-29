num = [2,3,4,7,3,8]

square= list(map(lambda n:n**2 , num))
# square.sort()
# square1 =sorted(square)

print(square)

# list comprihension

sq = list(n**2 for n in num)

print(sq)