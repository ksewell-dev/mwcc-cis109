import argparse
from cryptlib import encrypt, decrypt

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Command-Line Tool")
    
    # Mutually exclusive group prevents user from passing both -e and -d
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", type=int, help="Shift value to encrypt the message")
    group.add_argument("-d", type=int, help="Shift value to decrypt the message")
    
    # Message argument
    parser.add_argument("-m", type=str, required=True, help="The message to process")
    
    args = parser.parse_args()
    
    if args.e is not None:
        output = encrypt(args.m, args.e)
        print("Encrypted:", output)
    elif args.d is not None:
        output = decrypt(args.m, args.d)
        print("Decrypted:", output)

if __name__ == "__main__":
    main()