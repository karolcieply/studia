import os
class piramid():
    def __init__(self):
        with open('slownik.txt') as f:
            self.words = f.read().split("\n")
        self.singleLetterWords = ["a", "i", "o", "u", "z", "w"]
        self.results = []

    def filterTable(self, words, oldWord):
        return [word for word in words if len(word) == len(oldWord)-1 and
                [letter for letter in range(len(oldWord)) if sorted(word) ==
                 sorted(oldWord)[:letter]+sorted(oldWord)[letter+1:]] and
                [letter for letter in word if letter in self.singleLetterWords]]

    def recursion(self, words):
        for word in words:
            if len(word) == 2:  # "Łapanie" końca ciągu
                self.results.append(self.filterTable(self.singleLetterWords,
                                                     word)[0])  # Dodawanie jednoliterowych 
                self.results.append(word)
                return True
            else:
                if not (x := self.filterTable(self.words, word)):
                    self.results = []  # Czyszczenie wyników jeżeli nie uda się znaleźć pełnego ciągu słów
                if self.recursion(x):
                    self.results.append(word)
                    return True

    def createSite(self):
        self.results.reverse()
        with open('result.html', 'w') as r:
            r.write("<body>\n\t<table>")
            for word in self.results:
                r.write(f"\n\t\t<tr><th>{word}</th></tr>")
            r.write("\n\t</table>\n</body>")


def main():
    Piramid = piramid()
    userInput = input("Podaj słowo:")
    if not Piramid.recursion([userInput]):
        print("Nie znaleziono ciągu słów")
        if os.path.exists("result.html"):
            os.remove("result.html")
    else:
        Piramid.createSite()


if __name__ == "__main__":
    main()
