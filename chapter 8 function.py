# chapter 8 function
magicians = ["Merlin", "Houdini", "David Copperfield"]

# Print each magician
for magician in magicians:
    print(magician)

def show_magicians(magicians):
    """Add 'the great' to each magician's name and print."""
    for magician in magicians:
        print("The Great " + magician)

show_magicians(magicians)


def order_sandwich(toppings):
    """Accept orders for a sandwich with three toppings and describe each topping."""
    print("Your sandwich toppings are:")
    for topping in toppings:
        describe_topping(topping)

def describe_topping(topping):
    """Describe each topping."""
    descriptions = {
        "lettuce": "Crisp and fresh green leaves.",
        "tomato": "Juicy and flavorful red fruit.",
        "cheese": "Creamy and savory dairy product.",
        # Add more toppings and descriptions as needed
    }

    if topping.lower() in descriptions:
        print("- " + topping.capitalize() + ": " + descriptions[topping.lower()])
    else:
        print("- " + topping.capitalize() + ": Description not available.")

# Example order
customer_order = ["lettuce", "tomato", "cheese"]
order_sandwich(customer_order)
