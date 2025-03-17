Default 
# ----- EXAMPLE -----
def net_price(list_price, discount=0, tax=0.05):
   return list_price * (1 - discount) * (1 - tax)

# print(net_price(500))
# print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))

# ----- EXERCISE -----
import time

def count(end, start=0): 
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

# count(10)
# count(30, 15)

# keyword arguments = arguments prefixed with the names of parameters
#                                        order of the arguments doesn’t matter
#                                        helps with readability

# ----- EXAMPLE 1 -----
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="John", first="James")

# ----- EXAMPLE 2 -----
for number in range(1, 11):
    print(number, end=" ")

print("1", "2", "3", "4", "5", sep="-")

# ----- EXERCISE -----
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)
