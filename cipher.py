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


if __name__ == "__main__":
    print("Caesar Cipher - Encrypt/Decrypt")
    
    shift = get_shift()
    cipher = CaesarCipher(shift=shift)
    print(f"Shift Key set to: {shift}")
    
    while True:
        print("\n--- Menu ---")
        print("(E) Encode")
        print("(D) Decode")
        print("(Q) Quit")
        choice = input("Select option: ").upper()
        
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice == 'E':
            text = input("Enter text to encode: ")
            if text:
                print(f"Encoded: {cipher.encode(text)}")
        elif choice == 'D':
            text = input("Enter text to decode: ")
            if text:
                print(f"Decoded: {cipher.decode(text)}")
        else:
            print("Invalid choice. Try again.")
