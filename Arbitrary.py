# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
# * unpacking operator

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f" {kwargs.get('street')}")
        print(f" {kwargs.get('pobox')}")
    else:
        print(f" {kwargs.get('street')}")
    
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Square pants", "III",
               street="123 Fake St.",
               pobox="Po box #100",
               city="Detroit",
               state="MI",
               Zip="54321")