"""
Author: Rose McCormack
Version: 2 November 2024
Module: ExamPractice.py
Description: 
        Holiday Season Sales Promotion Policy
    1. Preferred customers who order $1000 or more are entitled 
       to a 5% discount and an additional 5% discount if they use 
       our charge card.
    2. Preferred customers who do not order $1000 or more will 
       receive a $25 bonus coupon.
    3. All other customers will receive a $5 bonus coupon.
"""

def main():
    # Try/Except blocks to handle safer input from the user
    try:
        order = float(input("How much did you order in $? $"))
    except ValueError:
        print("Invalid input for order amount. Please enter a valid number.")
        return
    
    preferred_or_not = input("Are you a preferred customer? Yes or no ").strip().lower()
    charge_card = input("Do you use our charge card? Yes or no ").strip().lower()

    # Conditional block for determining coupons and discounts
    if preferred_or_not == "yes" and order >= 1000:
        if charge_card == "yes":
            order -= order * 0.10  # 10% discount for preferred customers using charge card
            outcome = "10% discount applied"
        else:
            order -= order * 0.05  # 5% discount for preferred customers without charge card
            outcome = "5% discount applied"
    elif preferred_or_not == "yes" and order < 1000:
        outcome = "$25 bonus coupon"
    else:
        outcome = "$5 bonus coupon"

    # Output the result
    print(f"Your preferred status is {preferred_or_not.capitalize()}, " +
          f"your charge card status is {charge_card.capitalize()}, " +
          f"and your order total is ${round(order, 2)}.")
    print(f"Outcome: {outcome}")

if __name__ == "__main__":
    main()
