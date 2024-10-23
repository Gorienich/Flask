class Decoder:
    def __init__(self, shift=3):
        self.shift = shift

    def decode(self, text):
        # Simple Caesar Cipher decoding (reverse the shift)
        decoded_chars = [chr((ord(char) - self.shift - 65) % 26 + 65) if char.isalpha() else char for char in text.upper()]
        return ''.join(decoded_chars)
