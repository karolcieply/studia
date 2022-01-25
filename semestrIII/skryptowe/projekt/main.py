import time
import json


class piramid:
    def __init__(self):
        with open("slownik.txt") as f:
            self.words = f.read().split("\n")
        self.singleLetterWords = ["a", "i", "o", "u", "z", "w"]
        self.results = {}
        self.resultsTemp = []

    def filterTable(self, words, oldWord):
        return [
            word
            for word in words
            if len(word) == len(oldWord) - 1
            and [
                letter
                for letter in range(len(oldWord))
                if sorted(word)
                == sorted(oldWord)[:letter] + sorted(oldWord)[letter + 1:]
            ]
            and [letter for letter in word if letter in self.singleLetterWords]
        ]

    def recursion(self, words):
        for word in words:
            if len(word) == 2:
                self.resultsTemp.append(
                    self.filterTable(self.singleLetterWords, word)[0]
                )
                self.resultsTemp.append(word)
                return True
            elif self.recursion(self.filterTable(self.words, word)):
                self.resultsTemp.append(word)
                return True


def main():
    Piramid = piramid()
    with open("input.txt") as f:
        input = f.read().splitlines()
    for word in input:
        startTime = time.time()
        if not Piramid.recursion([word]):
            Piramid.results[word] = {
                "result": ["Nie znaleziono"],
                "time": round(time.time() - startTime, 5),
            }
        else:
            Piramid.results[word] = {
                "result": Piramid.resultsTemp,
                "time": round(time.time() - startTime, 5),
            }
            Piramid.resultsTemp = []
    with open("output/result.txt", "w") as f:
        f.write(json.dumps(Piramid.results))


if __name__ == "__main__":
    main()
