#Define the function for evaluating the price of an item
def price(items_pricing, shopping_cart):
    total_price = 0
    shopping_item_count = {}
    print("Cart : ",shopping_cart) #See for debug
    
    # Count the occurrences of each item
    for i_item in shopping_cart:
        shopping_item_count[i_item] = shopping_item_count.get(i_item, 0) + 1 
        print("Item counts:", shopping_item_count) #See for debug
    
    # Calculate the total price based on pricing rules
    for i_item, count in shopping_item_count.items(): #Evaluate for each item in the shopping cart
        if i_item in items_pricing: #Check if the item is in the dictionart items_pricing
            unit_price, special_price = items_pricing[i_item]
            print(f"Item: {i_item}, Count: {shopping_item_count}, Unit Price: {unit_price}, Special Price: {special_price}") #See for debug

            if special_price: #check if there is an offer as (3,130)
                offer_quantity, offer_price = special_price #Find the quantity needed for the sales and the sales price
                number_of_sales_items = count // offer_quantity 
                remaining_items = count % offer_quantity
                total_price += number_of_sales_items * offer_price + remaining_items * unit_price #Evaluate the total price
            else:
                total_price += count * unit_price #Find the total price without any sale / offer avaiable for the wanted item
    
    return total_price

# Test pricing "list" (it's a dictionary btw)
items_pricing = {
    "A": (50, (3, 130)),
    "B": (30, (2, 45)),
    "C": (20, None),
    "D": (15, None)
}

assert price(items_pricing, "") == 0
assert price(items_pricing, "A") == 50
assert price(items_pricing, "AB") == 80
assert price(items_pricing, "CDBA") == 115
assert price(items_pricing, "AA") == 100
assert price(items_pricing, "AAA") == 130
assert price(items_pricing, "AAAA") == 180
assert price(items_pricing, "AAAAA") == 230
assert price(items_pricing, "AAAAAA") == 260
assert price(items_pricing, "AAAB") == 160
assert price(items_pricing, "AAABB") == 175
assert price(items_pricing, "AAABBD") == 190
assert price(items_pricing, "DABABA") == 190