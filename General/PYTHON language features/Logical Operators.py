# Demonstration of Logical Operators


# Beispielvariable :
a = 15  

print((a > 10) and (a < 20))  # Gibt True zurück, da beide Bedingungen erfüllt sind
print((a > 10) or (a > 20))   # Gibt True zurück, da mindestens eine Bedingung erfüllt ist
print(not((a > 10) and (a < 20)))  # Gibt False zurück, da die ursprüngliche Bedingung True ist und durch "not" negiert wird

# Benutzereingabe für "C" und "D"
C = input("Enter the value of C: ")
print("The value of C is " + str(C))  # Korrektur: "format(C)" ist hier nicht nötig, "str()" reicht aus

D = input("Enter the value of D: ")
print("The value of D is " + str(D))  # Gleiches Problem wie oben, daher korrigiert

# Identitätsprüfung: "is" sollte nicht für Wertevergleich genutzt werden!
# In Python vergleicht "is" die Objektidentität, nicht den Wert.
print('Output is true because c and d values are identical:', C == D)  # Korrektur: "==" statt "is"

# Vergleich von Zeichenketten
A = 'java'
B = 'php'
print('Output is true because a and b values do not match:', A != B)  # Korrektur: "is not" ist nicht korrekt für Wertvergleiche

A1 = 'java'
B1 = 'java'
print('Output is false because a1 and b1 values match:', A1 == B1)  # Korrektur: "==" statt "is not"