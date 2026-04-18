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
