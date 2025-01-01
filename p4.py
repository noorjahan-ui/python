numbers=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    num=int(input("enter element{i+1}:"))
    numbers.append(num)
    odd_numbers=[num for num in numbers if num % 2!=0]
    print("orginal list:",numbers)
    print("list after removing even numbers:",odd_numbers)