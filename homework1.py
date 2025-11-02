a=float(input())
b=float(input())
print("მიმატება",a+b)
print("გამოკლება",a-b)
print("გამრავლება", a*b)
print("გაყოფა", a/b)
print("მთელზე გაყოფა", a//b)
print("ნაშთი", a%b)
print("ახარისხება", a**b)


d1=float(input("პირველი დიაგონალი: "))
d2=float(input("მეორე დიაგონალი: "))
S=d1*d2/2
print("რომბის ფართობი:", S)

metre=float(input("მეტრი:"))
print("სანტიმეტრი", metre*100)
print("დეციმეტრი", metre*10)
print("მილი", metre/1609.34)
print("მილიმეტრი", metre*1000)


b=float(input("სიმაღლე: "))
h=float(input("ფუძე: "))
S=b*h/2
print("სამკუთხედის ფართობი",S)



number=int(input("ორნიშნა რიცხვი:"))
ateuli=number//10
erteuli=number%10
sum=ateuli+erteuli
print("ჯამი", sum)