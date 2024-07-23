def caesar_encrypt(message: str, n: int) -> str:
    result = ''
    for char in message:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + n) % 26 + start)
        else:
            shifted_char = char
        result += shifted_char
    return result
    
print(caesar_encrypt("Hello" , 10))