n = int(input())
p = int(input())

sell_m = 0
sell_p = 0
if n > 15 :
    sell_m = 2000
elif n > 5 :
    sell_m = 500

if n > 20 :
    sell_p = 1/4
elif n > 10 :
    sell_p = 1/10
    
sell_p