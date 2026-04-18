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


if __name__ == "__main__":
    cipher = CaesarCipher(shift=3)
    text = "running"
    encoded = cipher.encode(text)
    print(f"Original: {text}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {cipher.decode(encoded)}")

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
    shift = get_shift()
    cipher = CaesarCipher(shift=shift)
    
    text = input("Enter text to encode: ")
    encoded = cipher.encode(text)
    print(f"Encoded: {encoded}")
    
    decoded = cipher.decode(encoded)
    print(f"Decoded: {decoded}")

