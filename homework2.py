nums=[2,5,7,9,2,54,76,89]
num1=int(input("შეიყვანეთ რიცხვი:"))
if num1 in nums:
    print("რიცხვი არის სიაში")
else:
    print("რიცხვ არ არის სიაში")

num2=int(input("შეიყვანეთ რიცხვი:"))
if num2 in nums:
    print("რიცხვი არის სიაში")
else:
    print("რიცხვი არ არის სიაში")

num1=int(input("შეიყვანეთ რიცხვი "))
if num1%2 == 0:
    print("ლუწი")
else:
    print("კენტი")

st1=(input("შეიყვანეთ ტექსტი: "))
st2=(input("შეიყვანეთ ტექსტი: "))
if st1 == st2 :
    print("same object")
else:
    print("different object")

num_list=[2,12,17,9,32,14,26,39]

num=int(input("შეიყვანეთ რიცხვი"))
if num>num_list[2] and num<num_list[-1]:
 print("more than list elements")
elif num==num_list[5]:
 print("equal")
else:
 print("non of the conditions were meet")

