for i in range(1, 11):
    if i %2 == 0:
      print(f"even num:{i}")
    else:
      print(f"odd num:{i}")


num = int(input("enter your number: "))
if num %  2 == 0:
   print("even number")
else:
   print("odd number")



num = int(input("enter your number: "))
if num > 0:
   print("positive number")
elif num < 0:
   print("negative number")
else:
   print("zero")   


a = int(input("enter the number for a: "))
b = int(input("enter the number for b: "))
print(f"add={a+b}")
print(f"sub={a-b}")
print(f"mul={a*b}")
print(f"div={a/b}")


marks = int(input("enter your marks: "))
if marks>=90:
   print("grade A")
elif marks>=80:
   print("grade B")
elif marks>=75:
   print("grade C")
else:
   print("fail")



marks = int(input("enter your marks: "))
if marks >= 90:
   print("the student got grade A")
elif marks >= 80:
   print("the student got grade B")
elif marks >= 70:
   print("the dtudent got grade C")
elif marks >= 60:
   print("the student got the grade D:")
else:
   print("the student is considered as Fail")


