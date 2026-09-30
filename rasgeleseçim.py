import random

print(" RASTGELE SECICI \n")

secenekler = ["dönerci", "ev", "çatı", "yemekhane"]

print("Secenekleriniz:", ", ".join(secenekler)) 

secilen = random.choice(secenekler)

print("\n*** RASTGELE SECILEN:", secilen, "")

input("Cikmak icin ENTER tusuna basin...")
