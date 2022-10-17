from curses.ascii import islower, isupper


class CaeserCipher:
    def __init__(self, shift_value, shift_direction="right"):
        if shift_direction not in ["right", "left"]:
            raise ValueError("Invalid shift direction. It can be either left or right")

        self.shift_value = shift_value
        self.shift_direction = shift_direction

    def encrypt(self, plain_message):
        if self.shift_direction == "right":
            encrypted_msg = self.__forward_shift(plain_message)
        elif self.shift_direction == "left":
            encrypted_msg = self.__backward_shift(plain_message)
        
        return encrypted_msg
        
    
    def decrypt(self, cipher_text):
        if self.shift_direction == "right":
            decrypted_msg = self.__backward_shift(cipher_text)
        elif self.shift_direction == "left":
            decrypted_msg = self.__forward_shift(cipher_text)
        
        return decrypted_msg



    def __forward_shift(self, msg_string):
        return_str = ""
        for char in msg_string:      
            if islower(char):
                return_str +=  chr(97 + ((ord(char) + self.shift_value - 97) % 26 ))
            elif isupper(char):
                return_str +=  chr(65 + ((ord(char) + self.shift_value - 65) % 26 ))
            else:
                return_str += char
        return return_str

    def __backward_shift(self, msg_string):
        return_str = ""
        for char in msg_string:      
            if islower(char):
                val =   ord(char) - self.shift_value - 97
                if val < 0:
                    val = 26 + val
                return_str += chr(97+val)
            elif isupper(char):
                val =   ord(char) - self.shift_value - 65
                if val < 0:
                    val = 26 + val
                return_str += chr(65+val)
            else:
                return_str += char
        return return_str