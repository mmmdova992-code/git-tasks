#task 16
y=int(input("Enter the number"))
if y<0 or y>100:
    print("No result")
else:
    result="pass" if y>51 else "fail"
    print(result)

#task 17
ot=int(input())
m=input("membership(yes or no):")
if ot<0 or (membership!=yes and membership!=no):
   print("delivery is rejected")
else:
    df=0 if ot>=50 or m=="yes" else 5
    print(df)

#task 18
day = int(input('enter the day:'))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("weekend")
    case 7:
        print("weekend")
    case _:
        print("invalid day")

#task 19
code=input("enter the code")
quantity=int(input("enter quantity"))
if quantity<1 or quantity>10:
    print("Invalid quantity")
else:
    match code:
        case "T":
            name="T"
            price=2
        case "C":
            name="Coffee" 
            price=4
        case "J":
            name="Juice"
            price=3
        case _:
            name="None"
            price=0
e=quantity*price
t="Large order" if e>=20 else "Regular order"
print(quantity,e,code,t)