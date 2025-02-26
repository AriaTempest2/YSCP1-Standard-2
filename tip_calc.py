# tip_calculator.py
# A simple tip calculator to compute tip amount and total bill
print("--- WELCOME TO TIP CALCULATOR ---\n")
total = float(input("Enter the total bill amount: "))
tip = float(input("Enter the tip percentage (e.g, 15 for 15 percent): "))

full = tip / 100
bill = total * full
total_bill = total + bill

print("\n--- TIP CALCULATOR SUMMARY ---")
print(f"Bill Amount: {total}")
print(f"Tip Amount: {tip}")
print(f"Total Bill: {total_bill}")
print("Thank you for using the Tip Calculator.")
