randomWords = ("aprender", 'programar', 'linguagem', 'python', 'curso', 'gratis',
               'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vowels = 'aeiou'

for w in randomWords:
    print("\n"+w, end=' -> ')
    for letter in range(0, len(w)):
        if w[letter] in vowels:
            print(w[letter], end=' ')
