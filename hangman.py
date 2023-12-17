import random
tries = 10
words = ["elma", "armut", "karpuz", "kavun", "kayısı", "muz", "mandalina", "portakal", "kivi", "üzüm", "çilek", "erik", "kiraz", "şeftali", "nar", "vişne", "ananas", "greyfurt", "limon", "şekerpare", "baklava", "kadayıf", "revani", "kemalpaşa", "ekmekkadayıfı", "künefe", "kazandibi", "sütlaç", "kazandibi", "künefe", "kadayıf", "ekmekkadayıfı", "kemalpaşa", "revani", "kadayıf", "baklava", "şekerpare", "limon", "greyfurt", "ananas", "vişne", "nar", "şeftali", "kiraz", "erik", "çilek", "üzüm", "kivi", "portakal", "mandalina", "muz", "kayısı", "kavun", "karpuz", "armut", "elma"]
chosen = random.choice(words)
found_letters = []
print("Seçilen kelime", len(chosen), "harfli.")
print("Lütfen tek bir harf girin ya da kelimeyi tahmin edin.")
while tries > 0:
    underscores = 0
    for i in range(len(chosen)):
        if chosen[i] in found_letters:
            print(chosen[i], end="")
        else:
            print("_", end="")
            underscores += 1
    print()
    if underscores == 0:
        print("Tebrikler. Kelimeyi buldunuz.")
        exit()
    
    print(tries, "hakkınız var.")
    guess = input("Bir harf ya da kelime giriniz: ")
    guess = guess.strip().lower()
    if len(guess) == 0:
        print("Lütfen tahmin girin.")
        continue
    elif len(guess) == len(chosen):
        if guess == chosen:
            print("Tebrikler! Doğru bildiniz.")
            exit()
        else:
            print("Kelimeyi doğru tahmin edemediniz.")
            tries -= 1
    elif len(guess) == 1:
        if guess in chosen:
            found_letters.append(guess)
            print("Doğru tahmin:", guess)
        else:
            print("Yanlış tahmin ettiniz.")
            tries -= 1
    else:
        print("Lütfen geçerli bir giriş yapın.")
    print("##################################\n\n")
print("Hakkınız kalmadı. Doğru kelime:", chosen)