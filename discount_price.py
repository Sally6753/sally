def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price, "Discounted"
    else:
        return price, "Not Discounted"

# Original price provided
original_price = 200.00

# Discount percentage provided
discount_percent = 15.00

final_price, status = calculate_discount(original_price, discount_percent)

if status == "Not Discounted":
    print("No discount applied. Final price:", final_price)
else:
    print("Final price after applying a", discount_percent, "% discount:", final_price)
    print("Status of the price:", status)  
    
