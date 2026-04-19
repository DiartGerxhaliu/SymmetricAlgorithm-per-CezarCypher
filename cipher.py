class CaesarCipher:
    def __init__(self, shift=3):
        self.shift = shift % 26

    def encode(self, text):
        encoded = []
        for c in text:
            if 'A' <= c <= 'Z':
                encoded.append(chr((ord(c) - ord('A') + self.shift) % 26 + ord('A')))
            elif 'a' <= c <= 'z':
                encoded.append(chr((ord(c) - ord('a') + self.shift) % 26 + ord('a')))
            else:
                encoded.append(c)
        return ''.join(encoded)

    def decode(self, text):
        decoded = []
        for c in text:
            if 'A' <= c <= 'Z':
                decoded.append(chr((ord(c) - ord('A') - self.shift) % 26 + ord('A')))
            elif 'a' <= c <= 'z':
                decoded.append(chr((ord(c) - ord('a') - self.shift) % 26 + ord('a')))
            else:
                decoded.append(c)
        return ''.join(decoded)


def get_shift():
    while True:
        try:
            return int(input("\nEnter shift key (any number): "))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("Caesar Cipher - Encrypt/Decrypt")
    
    shift = get_shift()
    cipher = CaesarCipher(shift=shift)
    print(f"Shift Key set to: {shift}")
    
    while True:
        choice = input("\n(E)ncode message, (D)ecode message, (K)ey change, or (Q)uit? ").upper()
        
        if choice == 'Q':
            break
        elif choice == 'E':
            msg = input("Enter message to encode: ")
            if msg:
                enc = cipher.encode(msg)
                print(f"Encoded: {enc}")
        elif choice == 'D':
            enc_msg = input("Enter message to decode: ")
            if enc_msg:
                dec = cipher.decode(enc_msg)
                print(f"Decoded: {dec}")
        elif choice == 'K':
            shift = get_shift()
            cipher = CaesarCipher(shift=shift)
            print(f"Shift key changed to: {shift}")
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
