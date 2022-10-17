from collections import OrderedDict

class PlayfairCipher:
    """Playfair Cipher Encryption"""
    def __init__(self, key, message):
        self.key = [i for i in key.upper()]
        self.matrix = []
        self.pairs = []
        self.encode(message)


    def create_matrix(self):
        # Remove duplicates from key
        result = list(OrderedDict.fromkeys(self.key))

        # Remove I and J from key
        for i in range(len(result)):
            if result[i] == "I" or result[i] == "J":
                result[i] = "I/J"

        k = l = 0
        
        alphabets = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I/J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]

        for char in result:
            alphabets.remove(char)

        # Create 5x5 matrix
        for i in range(5):
            temp = []
            for j in range(5):
                if k > len(result) - 1:
                    temp.append(alphabets[l])
                    l += 1
                else:
                    temp.append(result[k])
                    k += 1
            self.matrix.append(temp)

    def __print_matrix(self):
        """Prints the matrix in a 5x5 format."""
        for i in range(5):
            for j in range(5):
                print(self.matrix[i][j], end=" ")
            print()

    def format_message(self, message):
        """Formats the message into pairs of characters."""
        message = message.upper().replace(" ", "")
        i = 0
        # Add X if two consecutive characters are same and Add X at the end if last character is alone
        while i < len(message):
            if i + 1 < len(message):
                if message[i] != message[i + 1]:
                    self.pairs.append(message[i] + message[i + 1])
                    i += 2
                else:
                    self.pairs.append(message[i] + "X")
                    i += 1
            else:
                self.pairs.append(message[i] + "X")
                i += 1

    def encode(self, message):
        """Encodes the message using Playfair Cipher."""
        self.create_matrix()
        self.format_message(message)
        self.__print_matrix()
        print("\n"+ self.pairs + "\n")
        solutions = []
        
        # Find the index of the characters in the matrix
        # If the characters are in the same row, replace them with the characters to their immediate right respectively
        # If the characters are in the same column, replace them with the characters immediately below respectively
        # If the characters are not on the same row or column, replace them with the characters on the same row respectively but at the other pair of corners of the rectangle defined by the original pair.
        for strings in self.pairs:
            index1 = self.__find_in_list_of_list(self.matrix, strings[0])
            index2 = self.__find_in_list_of_list(self.matrix, strings[1])

            if index1[0] == index2[0]:
                solutions.append(
                    self.matrix[index1[0]][(index1[1] + 1) % 5]
                    + self.matrix[index2[0]][(index2[1] + 1) % 5]
                )
            elif index1[1] == index2[1]:
                solutions.append(
                    self.matrix[(index1[0] + 1) % 5][index1[1]]
                    + self.matrix[(index2[0] + 1) % 5][index2[1]]
                )
            else:
                solutions.append(
                    self.matrix[index1[0]][index2[1]]
                    + self.matrix[index2[0]][index1[1]]
                )

        print(solutions)

    def __find_in_list_of_list(self, mylist, char):
        """Returns the index of the first occurrence of char in mylist."""
        for sub_list in mylist:
            if char == "I" or char == "J":
                if "I/J" in sub_list:
                    return (mylist.index(sub_list), sub_list.index("I/J"))
            if char in sub_list:
                return (mylist.index(sub_list), sub_list.index(char))