# Script creates a Hashmap object

class Hash:
    # The maximum elements, m, in the Hashmap is defined when the class is instantiated
    def __init__(self, m):
        self.array = [0]*m
        self.size = 0
        self.max = m

    # ___Hash Functions___
    # The modulos ensure that the numbers don't exceed a certain range
    
    # The first hash function bitwise or's every letter in the given string and squares it
    def convertA(self, string, conv=0):
        for s in string:
            conv = (conv ^ (ord(s)-97))**2 % 1000000
        return conv
    
    # The second hash function bitwise or's the square of every letter in the given string
    def convertB(self, string, conv=0):
        for s in string:
            conv = (conv ^ ord(s)**2) % 1000000
        return conv

    # hash_function will produce the hash for the given string using double hashing
    def hash_function(self, user_name, i):
        A = (self.convertA(user_name) + i*self.convertB(user_name)) % self.max
        # 0 is treated as a empty position, therefore the hash function should not return 0
        if (A == 0):
            return 1
        return A


    # ___Hashmap Methods___

    # Generates a unique hash for a string
    def generate(self, user_name):
        if (self.size < self.max):
            for i in range(self.max):
                A = self.hash_function(user_name, i)
                if (self.array [A] == 0 or self.array [A] == -1):
                    self.array [A] = user_name
                    self.size += 1
                    return A
                elif (self.array [A] == user_name):
                    print("ERROR: Duplicate user input")
                    return -1
        print("ERROR: Hash full")
        return -1

    # Deletes the hash for a string
    def delete(self, user_name):
        if (self.size > 0):
            for i in range(self.max):
                A = self.hash_function(user_name, i)
                if (self.array [A] == 0 or self.array [A] == -1):
                    print("ERROR: user not found")
                    return -1
                elif (self.array [A] == user_name):
                    self.array [A] = -1
                    self.size -= 1
                    return 0
        print("ERROR: Hash empty")
        return -1

    # Searches for the hash of a string
    def search(self, user_name):
        for i in range(self.max):
            A = self.hash_function(user_name, i)
            if (self.array [A] == 0):
                print("ERROR: user not found")
                return -1
            elif (self.array [A] == user_name):
                break
        if (i < self.max):
            return A
        print("ERROR: user not found")
        return -1

    # Prints the entire Hashmap
    def print_hash(self):
        print(self.array)

