class StringUtility:
    def __init__(self, string):
        self.str = string

    def __str__(self):
        return self.str

    def vowels(self):
        return str(len([i for i in self.str if i in "aeiouAEIOU"])) if len([i for i in self.str if i in "aeiouAEIOU"]) < 5 else "many"

    def bothEnds(self):
        return "" if len(self.str) <= 2 else self.str[:2] + self.str[-2:]

    def fixStart(self):
        return self.str if len(self.str) <= 1 else self.str[0] + self.str[1:].replace(self.str[0], "*")

    def asciiSum(self):
        return sum([ord(i) for i in self.str])

    def cipher(self):
        return "".join(i if not i.isalpha() else chr((ord(i) - 65 + len(self.str)) % 26 + 65) if i.isupper() else chr((ord(i) - 97 + len(self.str)) % 26 + 97) for i in self.str)
