def naive(stringText, stringSearch):
    return [i for i in range(len(stringText)-len(stringSearch)+1)
            if stringText[i:i+len(stringSearch)]==stringSearch]

print(naive("taktakes","tak"))