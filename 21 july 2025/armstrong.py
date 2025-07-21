num = input("Enter a number:")

length=len(num)

arr = []

for i in num:
    p= int(i)**length
    arr.append(p)
    
print("🎇 The Array is ,")
for i in arr:
    print(">", i)

s= sum(arr)
print("The Sum of the Array is : ",s)

tar = int(num)

if s == tar:
    print("Number you entered is Armstrong")
else:
    print("Number you entered is not armstrong")