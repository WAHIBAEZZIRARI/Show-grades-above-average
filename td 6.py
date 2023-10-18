notes = []
n = int(input("Entrez le nombre de notes : "))
total = 0

for _ in range(n):
    note = float(input("Entrez une note : "))
    notes.append(note)
    total += note

moyenne = total / n

print("Les notes supérieures à la moyenne sont :")
for note in notes:
    if note > moyenne:
        print(note)
