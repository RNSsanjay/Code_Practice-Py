num = input("Enter a number: ")

def reverse_number(n):
    return n[::-1]

def is_palindrome(n):
    reversed_num = reverse_number(n)
    return n == reversed_num


if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")