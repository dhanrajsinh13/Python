# ---------- DECORATORS ----------
# A decorator in Python is like a "wrapper" for a function.
# It lets you run some extra code before or after the main function runs,
# without changing the original function itself.
# Think of it like putting a gift (your function) inside fancy wrapping paper
# that also includes a free card with a message before the gift is opened.

def choose_store(func):
    # This decorator asks the user which store they want to buy from
    def wrapper(*args, **kwargs):
        print("1. Priyanshi's ice cream")
        print("2. Dhanraj's pizza shop")
        choice = input("Choose store (1 or 2): ")
        # Store name is decided based on choice
        store = "Elisha ice cream" if choice == "1" else "Joe's pizza shop"
        return func(choice, store, *args, **kwargs)

    return wrapper


def choose_flavor(func):
    # This decorator asks what flavor/item the user wants depending on the store
    def wrapper(choice, store, name, *args, **kwargs):
        if choice == "1":  # Ice cream shop
            print("Choose ice cream:")
            print("1. Vanilla")
            print("2. Chocolate")
            flavor_choice = input("Ice cream number (1 or 2): ")
            flavor_name = "vanilla" if flavor_choice == "1" else "chocolate"
        elif choice == "2":  # Pizza shop
            print("Choose pizza:")
            print("1. Pepperoni")
            print("2. Margherita")
            flavor_choice = input("Pizza number (1 or 2): ")
            flavor_name = "Pepperoni" if flavor_choice == "1" else "Margherita"
        else:
            print("Invalid store choice. Please start again.")
            return wrapper(choice, store, name, *args, **kwargs)

        return func(choice, store, flavor_name, name, *args, **kwargs)

    return wrapper


def log_decorator(func):
    # This decorator logs (prints) that we are calling a function
    # and also asks the user for their name
    def wrapper(choice, store, *args, **kwargs):
        print(f'Calling {func.__name__}')
        name = input("What is your name? ")
        return func(choice, store, name, *args, **kwargs)

    return wrapper


# ---------- HELPER FUNCTIONS ----------
# These are normal functions (not decorators) that help handle the order.

def get_toppings(choice):
    # Ask if user wants extra toppings depending on the store type
    extras = []
    if choice == "1":  # Ice cream toppings
        if input("Do you want sprinkles? (y/n): ").lower() == "y":
            extras.append("sprinkles 🎊")
        if input("Do you want fudge? (y/n): ").lower() == "y":
            extras.append("fudge 🍫")
    elif choice == "2":  # Pizza toppings
        if input("Do you want extra cheese? (y/n): ").lower() == "y":
            extras.append("extra cheese 🧀")
        if input("Do you want extra toppings? (y/n): ").lower() == "y":
            extras.append("extra toppings 🍄")
    return extras


def get_ice_cream(flavor_name, extras):
    # Print the extras and final ice cream order
    for item in extras:
        print(f"You added {item}!")
    print(f"Here is your {flavor_name} ice cream 🍦")


def get_pizza(flavor_name, extras):
    # Print the extras and final pizza order
    for item in extras:
        print(f"You added {item}!")
    print(f"Here is your {flavor_name} pizza 🍕")


# ---------- MAIN FUNCTION ----------
# Notice: This function doesn't directly ask store/flavor/name.
# The decorators handle that before this function runs.
@choose_store  # First: Ask store choice
@log_decorator  # Second: Ask name + log function
@choose_flavor  # Third: Ask flavor choice
def get_name(choice, store_name, flavor_name, name):
    extras = get_toppings(choice)  # Ask about toppings

    print(f"\n-------------- {store_name} --------------")
    print(f"\nWelcome to {store_name}!")
    print(f"Hello, {name}!")
    # Show final product based on store type
    if choice == "1":
        get_ice_cream(flavor_name, extras)
    elif choice == "2":
        get_pizza(flavor_name, extras)


# ---------- RUN PROGRAM ----------
get_name()


