class Fruit(object):
    """A class that makes various tasty fruits."""

    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible.")
        else:
            print("Don't eat me! I am super poisonous.")


lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

'''
class Animal(object):
    def __init__(self,name):
        self.name=name
'''


class Animal(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age


zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print(zebra.name, zebra.age, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_alive)
print(panda.name, panda.age, panda.is_alive)


class Animal(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Add your method here!
    def description(self):
        print(self.name)
        print(self.age)


hippo = Animal('yang', 7)
hippo.description()


class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if product not in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart.")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")

    def show_item(self):
        print(self.items_in_cart)


my_cart = ShoppingCart("yangjin")
my_cart.add_item("apple", 6)
my_cart.add_item("balano", 3)
my_cart.add_item("water", 2)
my_cart.remove_item("balano")
my_cart.show_item()


class Customer(object):
    """Produces objects that represent customers."""

    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print("I'm a string that stands in for the contents of your shopping cart!")


class ReturningCustomer(Customer):
    """For customers of the repeat variety."""

    def display_order_history(self):
        print("I'm a string that stands in for your order history!")


monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()


class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00


class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        self.hours = hours
        return super(PartTimeEmployee, self).calculate_wage(hours)


milton = PartTimeEmployee('yangjin')
print(milton.full_time_wage(10))


class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())
