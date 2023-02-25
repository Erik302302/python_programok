import string

karakterek = " " + "á" + "ó" + "ü" + "ű" + "ö" + "ő" + "ú" + "é" + string.punctuation + string.digits + string.ascii_letters
karakterek = list(karakterek)
kodolt = 'c', 'z', '|', 'n', 'Z', '5', 'B', 'm', ',', 'w', ']', '#', '&', 'k', 'f', 'é', 'r', 'p', ')', 'W', '6', "'", '-', '`', 'R', 'J', 'j', '0', '8', 'b', 'E', 'g', 'o', '=', 'C', '}', 'F', '9', 'á', 'H', 'ó', 'D', 'I', '~', 'ú', '!', '7', 'q', ':', '(', '+', 'a', 'd', 'ő', '<', 'M', 's', 'h', '2', ';', 'U', 'X', 'A', 'N', '\\', 'O', 'ö', '*', 'Y', '?', '@', '/', 'l', ' ', 'y', 'T', '4', '"', '.', 'P', '_', 'L', 'Q', 'ű', 'ü', 'e', '{', 't', '[', '1', '>', 'v', 'u', 'K', '^', 'x', 'V', '%', '3', 'G', 'S', 'i', '$'
kodolt = list(kodolt)
futas = True

while futas:
    forditas = ""
    valasztas = input("Kódolni (K) vagy fordítani (F) vagy kilépni (ENTER) szeretnél?: ").upper()
    if valasztas == "K":
        szoveg = input("Add meg a kódolandó szöveget: ")
        for kod in szoveg:
            index = karakterek.index(kod)
            forditas += kodolt[index]
        print(f"Eredmény: {forditas}")
    elif valasztas == "F":
        szoveg = input("Add meg a fordítandó szöveget: ")
        for kod in szoveg:
            index = kodolt.index(kod)
            forditas += karakterek[index]
        print(f"Eredmény: {forditas}")
    else:
        futas = False


