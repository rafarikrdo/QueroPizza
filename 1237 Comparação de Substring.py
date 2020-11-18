from difflib import SequenceMatcher
while True:
    try:
        primeiraSequencia = input()
        segundaSequencia = input()
        substring = SequenceMatcher(None, primeiraSequencia, segundaSequencia)
        maiorSubstring= substring.find_longest_match(0, len(primeiraSequencia), 0, len(segundaSequencia))
        print(maiorSubstring.size)
    except EOFError:
        break