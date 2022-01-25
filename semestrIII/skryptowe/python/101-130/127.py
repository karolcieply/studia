class Znak:
    def __init__(self, znaki: str):
        self.znak = znaki

    def zamien_wyrazami_od_tylu(self):
        return " ".join(self.znak.split()[::-1])

    def __str__(self):
        return self.znak


ciag = Znak("Ala ma kota")
print(ciag.zamien_wyrazami_od_tylu())
