palavra = input('Palavra : ')
palindrome = palavra == palavra[::-1]
print(f'{palavra} é palindrome')
print(palindrome)
