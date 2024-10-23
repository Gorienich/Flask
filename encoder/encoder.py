class Encoder:
    def __init__(self, shift=3):
        self.shift = shift

    def encode(self, text):
        # Simple Caesar Cipher encoding
        encoded_chars = [chr((ord(char) + self.shift - 65) % 26 + 65) if char.isalpha() else char for char in text.upper()]
        return ''.join(encoded_chars)
