#ให้ 1 = ส้ม, 2 = แอปเปิ้ล, 3 = กีวี่ และเหรียญ a = 1, d = 2, b = 5, c = 10
fruit=[]
coin=[]
def fruitJuice(fruit):
    orange = fruit.count(1) * 13
    apple = fruit.count(2) * 15
    kiwi = fruit.count(3) * 22
    price = orange+apple+kiwi
    return price
def money(coin):
    one = coin.count('a')*1
    two = coin.count('d')*2
    five = coin.count('b')*5
    ten =coin.count('c')*10
    money = one+two+five+ten
    change = money-price
    moneyType = [10,5,2,1]
    for  i in moneyType:
        if change >= i:
            print("เหรียญ",i,"จำนวน",int(change/i))
            change = change%i

price = fruitJuice([1,1,3,2])
money(['c','c','c','c','c','c','c'])