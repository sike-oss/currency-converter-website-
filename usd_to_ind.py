def usd_to_inr(usd):
    inr = usd * 82.73
    return inr

def eur_to_inr(eur):
    inr2 = eur * 90.12
    return inr2

def aed_to_inr(aed):
    inr3 = aed * 22.49
    return inr3

def gbp_to_inr(gbp):
    inr4 = gbp * 102.34
    return inr4
choice = 0  # Initialize choice
while choice != 5:
 print("WELCOME TO CURRENCY CONVERTER")
print("enter currency to convert to INR\n")




print("1. USD to INR")
print("2. EUR to INR")
print("3. AED to INR")
print("4. GBP to INR")
print("5. Exit  the converter")
choice = int(input("Enter your choice (1-5): "))
if choice == 1:
        usd = float(input("Enter amount in USD: "))
        print(f"{usd} USD is equal to {usd_to_inr(usd)} INR")
elif choice == 2:
        eur = float(input("Enter amount in EUR: "))
        print(f"{eur} EUR is equal to {eur_to_inr(eur)} INR")
elif choice == 3:
        aed = float(input("Enter amount in AED: "))
        print(f"{aed} AED is equal to {aed_to_inr(aed)} INR")        
elif choice == 4:
        gbp = float(input("Enter amount in GBP: "))
        print(f"{gbp} GBP is equal to {gbp_to_inr(gbp)} INR")
elif choice == 5:
        print("Exiting the converter.")
else:
        print("Invalid choice. Please enter a number between 1 and 5.")