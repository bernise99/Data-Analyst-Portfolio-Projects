OVERHEAD = 1.00
SHIPPING = 0.5
DISCOUNTED_SHIPPING = 0.25

# Main funtion: calls all three functions and displays output when appropriate    
def main():

    # Local variables that will later on be assigned appropriate values
    price = 0.0
    quantity = 400

    # Calls to print invoice twice
    print_invoice()
    print() # This prints an empty line to seprate the produced output
    print_invoice()
    print()
    
    # Calls to obtain total twice and then use it to produce appropriate output
    price = 4.49
    quantity = 400
    total = calculate_total(price,quantity)
    print("The total cost is $", format(total, ".2f"), " for ", quantity, " grams of tea priced at $", format(price, ".2f"), " per 100 grams.",  sep='')

    price = 8.50
    quantity = 600
    total = calculate_total(price,quantity)
    print("The total cost is $", format(total, ".2f"), " for ", quantity, " grams of tea priced at $", format(price, ".2f"), " per 100 grams.",  sep='')
    print()
    
    # Calls to display two price lists with for different prices
    price = 4.49
    print_price_list(price)
    print()
    
    price = 8.50
    print_price_list(price)
    print()
    
# Gets and validates user input, calculates total, and displays an invoice    
def print_invoice():
    price = 0.0
    quantity = 0
    total = 0.0

    # Obtain and validate input
    print("Welcome to Mike's Tea!")
    price = float(input("Enter today's price for 100 grams: "))

    while price < 0:
           price = float(input("Enter a correct price: "))

    quantity = int(input("How many grams (in a multiple of 100) for this order?: "))
    
    while quantity < 0 or quantity % 100 != 0:
        quantity = int(input("Enter a correct quantity: "))

    # Calculate total
    total = price * (quantity/100) + (quantity/100)*SHIPPING + OVERHEAD

    # Print invoice
    print("Printing invoice...")
    print("Current price (per 100 grams): $", format(price, ',.2f'), sep='')
    print("Ordered quantity (in grams):", quantity)
    print("Total for the order (with shipping): $", format(total, ',.2f'), sep='')


# Calculates and returns total with or without discounted shipping
def calculate_total(price, quantity):
    # Local variables
    total = 0.0

    # Calculate all possible total costs
    total_with_shipping = price * (quantity/100) + (quantity/100)*SHIPPING + OVERHEAD
    total_without_shipping = price * (quantity/100)
    total_with_discounted_shipping = price * (quantity/100) + (quantity/100)*DISCOUNTED_SHIPPING

    # Decide if order qualifies for a discounted shipping and set total accordingly
    if total_without_shipping > 50 and price > 8:
        total = total_with_discounted_shipping
    else:
        total = total_with_shipping
                      
    return total

# Displays a price list for bulk purchases that includes amounts, total and total with a discount
def print_price_list(price):

    # Local variables
    total = 0.0
    total_with_discount = 0.0
    
    # Displays the header for the price list
    print("Welcome to Mike's Tea!")
    print("Price list for bulk purchases at $", format(price, ".2f"), " dollars per 100 grams.", sep='')
    print()
    print("Grams \t", "Cost \t", "With 10% off \t", sep='')
    # Produces and displays the price list 
    for i in range(100, 1100, 100):
        total = price * (i/100)
        total_with_discount = total - total*0.1
        print(i, "\t", "$", format(total, ".2f"), "\t", "$",format(total_with_discount, ".2f"), sep='')

# Call to main()
main()
