name = "Okunade Israel Oluwasegun" ##string

age = 23 ##int

height = 6.2 ##float

status_Active = True #Boolean

## we can convert data types in 2 ways: Explicit i.e int() and Implicit ways
# Python occasionally converts types automatically (e.g., adding an int to a float results in a float), 
# but relying on this can lead to subtle bugs.

initial_price = "350000" # our price here is actually a string type
final_price = "500000"

total = int(initial_price) + int(final_price)

print(f"Total Price: ${total}")

