napples=int(input())
nbananas=int(input())
noranges=int(input())
cost_apple=15
cost_banana=4
cost_oranges=5
amount=700
totalamount=15*napples+4*nbananas+5*noranges
if(totalamount<amount):
    print("not cheated")
else:
    print("cheated")