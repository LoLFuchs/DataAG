
isTrue = []
isFalse = []

with open("C:\Users\domin\OneDrive\Desktop\wichtig\Programieren\VCS\Dataag\wert.txt", "r") as file:
    wert = str(file.read())

# Hier kannst du den gelesenen Wert in Datei B verwenden
print("Der gelesene Wert lautet:", str(wert))