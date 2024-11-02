class lzw:
    
    def __init__(self,compressed):
        self.string = compressed
    def compression(self):
        nextcharindex=1
        current=self.string[0]
        next=''
        if len(self.string)>1:
            next=self.string[1]
        compressedlist = []
        compressed = {
                '\0': 0, '\x01': 1, '\x02': 2, '\x03': 3, '\x04': 4, '\x05': 5, '\x06': 6, '\x07': 7,
                '\x08': 8, '\t': 9, '\n': 10, '\x0b': 11, '\x0c': 12, '\r': 13, '\x0e': 14, '\x0f': 15,
                '\x10': 16, '\x11': 17, '\x12': 18, '\x13': 19, '\x14': 20, '\x15': 21, '\x16': 22, '\x17': 23,
                '\x18': 24, '\x19': 25, '\x1a': 26, '\x1b': 27, '\x1c': 28, '\x1d': 29, '\x1e': 30, '\x1f': 31,
                ' ': 32, '!': 33, '"': 34, '#': 35, '$': 36, '%': 37, '&': 38, "'": 39, '(': 40, ')': 41,
                '*': 42, '+': 43, ',': 44, '-': 45, '.': 46, '/': 47, '0': 48, '1': 49, '2': 50, '3': 51,
                '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, ':': 58, ';': 59, '<': 60, '=': 61,
                '>': 62, '?': 63, '@': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71,
                'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81,
                'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, '[': 91,
                '\\': 92, ']': 93, '^': 94, '_': 95, '`': 96, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101,
                'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110,
                'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119,
                'x': 120, 'y': 121, 'z': 122, '{': 123, '|': 124, '}': 125, '~': 126, '\x7f': 127
            }
        if(len(self.string)==1):
            compressedlist.append(compressed[self.string[0]])
            return compressedlist
        last_index=128
        while nextcharindex<len(self.string):
            currentcheck = current+next
            if currentcheck in compressed:
                current = currentcheck
            else:
                compressedlist.append(compressed[current])
                compressed[currentcheck]=last_index
                last_index+=1
                current=next
            nextcharindex+=1
            if nextcharindex>= len(self.string):
                break
            next = self.string[nextcharindex]
        compressedlist.append(compressed[current])
        self.compressedData =  compressedlist
        return compressedlist
    def decompressing(self):
        encodedpatterns = [
            '\0', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07',
            '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f',
            '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17',
            '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f',
            ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
            '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
            '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f'
        ]
        decodedList=self.compressedData
        # current-1 = decodedList[0]
        outputString = encodedpatterns[decodedList[0]]
        for i in range(1,len(decodedList)):
            current = decodedList[i]
            if current<len(encodedpatterns):
                outputString += encodedpatterns[current]
                firstchar=encodedpatterns[current][0]
                encodedpatterns.append(encodedpatterns[decodedList[i-1]]+firstchar)
            elif current == len(encodedpatterns):
                encodedcase = encodedpatterns[decodedList[i-1]]+encodedpatterns[decodedList[i-1]][0]
                encodedpatterns.append(encodedcase)
                outputString+=encodedcase
        return outputString


print("enter a string: ")
inputString=input()
lzw_class = lzw(inputString)
print(lzw_class.compression())
print(lzw_class.decompressing())