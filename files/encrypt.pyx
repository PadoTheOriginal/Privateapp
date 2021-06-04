from re import search
from random import choice

class encryption:

    dict1 = {"#": ["~", "6", "7", "8", "9", "z", "^", "á"],
             "~": ["t", "y", "u", "i", "o", "p", "[", "õ"],
             "*": [")", "h", "j", "b", "k", "l", "$", "ã"],
             "!": ["x", "c", "v", "n", "m", " ", "(", "í"],
             "$": ["*", "!", "@", "%", "/", "\\", "'","ã"],
             "@": ["+", "-", "_", "?", "]", ":", ";", "ê"],
             "?": [".", ",", "|", "¦", "¿", "&", "}", "ô"],
             "%": ["=", "<", ">", "s", "d", "f", "#", "ó"],
             "¿": ["3", "4", "5", "q", "w", "e", "r", "é"],
             "^": ["a", "1", "2", "0", "g", '"', "{", "ç"]
             }
    
    dict2 = {"$": ["~", "6", "7", "4", "5", "q", "w", "á"],
             "^": ["t", "y", "u", "i", "/", "\\", "'","ã"],
             "!": ["n", "m", " ", "(", "k", "l", "$", "ã"],
             "*": ["x", "c", "v", ")", "h", "j", "b", "í"],
             "#": ["*", "9", "z", "^", "e", "p", "[", "õ"],
             "%": ["+", "-", "_", "?", "]", ":", ";", "ê"],
             "?": [".", ",", "|", "¦", "¿", "&", "}", "ô"],
             "@": ["a", "1", "2", "0", "d", "f", "#", "ó"],
             "¿": ["3", "8", "!", "@", "%", "o", "r", "é"],
             "~": ["=", "<", ">", "s", "g", '"', "{", "ç"]
             }
    
    dict3 = {"~": ["~", "_", "?", "]", "9", "z", "^", "á"],
             "#": ["m", " ", "(", "i", "o", "p", "[", "õ"],
             "!": [")", "h", "j", "b", "k", "l", "$", "ã"],
             "$": ["x", "c", "v", "n", "t", "y", "u", "í"],
             "*": ["*", "!", "@", "%", "/", '"', "{", "ç"],
             "@": ["+", "-", "6", "7", "8", ":", ";", "ê"],
             "%": [".", ",", "2", "0", "g", "&", "}", "ô"],
             "?": ["s", "d", "f", "#", "w", "e", "r", "ó"],
             "^": ["3", "4", "5", "q", "=", "<", ">", "é"],
             "¿": ["a", "1", "|", "¦", "¿", "\\", "'","ã"]
             }

    def binary(self, str text):
        return format(ord(text), "b")

    def notBinary(self, str text):
        return chr(int(text, 2))

    def encrypt(self, str text):
        dicts = [self.dict1, self.dict2, self.dict3]
        self.dicty = choice(dicts)


        cdef int i, i2, n

        for n, d in enumerate(dicts):
            if d == self.dicty:
                self.guider = "§%s," % n

        self.output = ""
        self.char = [l for l in text]
        self.char2 = [l for l in text]

        for key, values in self.dicty.items():
            for i, char in enumerate(values):
                for i2, char2 in enumerate(self.char):
                    if char.lower() == char2.lower():

                        if char != char2:
                            toAdd = f"↑{key}{i}"
                            self.char[i2] = toAdd
                        else:
                            toAdd = f"{key}{i}"
                            self.char[i2] = toAdd

        i = 0
        for c1, c2 in zip(self.char, self.char2):
            if c1 == c2:
                toAdd = "&" + self.binary(self.char[i])
                self.char[i] = toAdd
            
            i += 1

        self.output = "%s%s" % (self.guider, ",".join(self.char))

        return self.output

    def decrypt(self, str text):
        dicts = [self.dict1, self.dict2, self.dict3]
        self.guider = text[0:3]
        text = text.replace(self.guider, "")
        self.guider = int(self.guider[1])
        self.dicty = dicts[self.guider]
        self.output = ""
        self.char = []
        self.char2 = []
        if search(",", text):
            self.char = text.split(',')
            self.char2 = text.split(",")
        else:
            self.char.append(text)
            self.char2.append(text)

        cdef int i
        for i, char in enumerate(self.char):
            if search("↑", char) and not search("&", char):
                self.char[i] = char.replace("↑", "")
                self.char[i] = self.dicty[char[1]][int(char[2])].upper()

            elif not search("&", char):
                self.char[i] = self.dicty[char[0]][int(char[1])]


        i = 0
        for c1, c2 in zip(self.char, self.char2):
            if c1 == c2:
                toAdd = self.notBinary(self.char[i].replace("&", ""))
                self.char[i] = toAdd

            i += 1

        self.output = "".join(self.char)

        return self.output


if __name__ == "__main__":
    from time import time
    from statistics import mean
    e = encryption()
    while True:
        Input = input("INPUT:")
        times = []
        for i in range(1, 101):
            start = time()
            encrypted = e.encrypt(Input)
            end = time()
            times.append(end - start)
        
        print(mean(times))