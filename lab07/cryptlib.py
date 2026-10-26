"""
Custom Caesar Cipher Encryption Library
"""

def encrypt(message, shift):
    result = ""
    
    for char in message:
        code = ord(char)
        
        # Check if uppercase letter (ASCII 65 to 90)
        if 65 <= code <= 90:
            new_code = (code - 65 + shift) % 26 + 65
            result = result + chr(new_code)
            
        # Check if lowercase letter (ASCII 97 to 122)
        elif 97 <= code <= 122:
            new_code = (code - 97 + shift) % 26 + 97
            result = result + chr(new_code)
            
        else:
            # Leave spaces, numbers, and punctuation unchanged
            result = result + char
            
    return result

def decrypt(message, shift):
    """
    Decrypts the message by calling encrypt with a negative shift.
    """
    return encrypt(message, -shift)