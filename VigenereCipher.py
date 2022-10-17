class VigenereCipher:
    def __init__(self, key):
        self.key = key.lower()

    def compress(self, plaintext):
        plaintext = plaintext.lower()
        compressed_text = ""
        for char in plaintext:
            if char.isalpha():
                compressed_text += char
        return compressed_text

    def expandKey(self, plaintext):
        no_of_repeats = len(plaintext) // len(self.key) + 1
        expanded_key = (self.key * no_of_repeats)[: len(plaintext)]
        return expanded_key

    def encode(self, message):
        compressed_msg = self.compress(message)
        key_expanded = self.expandKey(message)
        cipher_text = ""
        count = 1
        for i in range(len(compressed_msg)):
            x = (ord(compressed_msg[i]) - 97 + ord(key_expanded[i]) - 97) % 26
            x += ord("a")
            cipher_text += chr(x)
            if count % 5 == 0:
                cipher_text += " "
            count += 1

        return cipher_text

    def decode(self, message):
        cipher_text = self.compress(message)
        key_expanded = self.expandKey(message)

        original_text = ""

        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) - ord(key_expanded[i]) + 26) % 26
            x += ord("a")
            original_text += chr(x)

        return original_text
