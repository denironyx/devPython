## Classes
Object-oriented programming is one of the most effective approaches to writing software.
In object-oriented programming you write classes that represent real-world things
and situations, and you create objects based on these classes. When you write a class, you define the general behavior that a whole category of objects can have.

When you create individual objects from the class, each object is automatically
equipped with the general behavior; you can then give each object
whatever unique traits you desire. You’ll be amazed how well real-world
situations can be modeled with object-oriented programming. Making an object from a class is called `instantiation`, and you work with instances of a class.

Understanding object-oriented programming will help you see the
world as a programmer does. It’ll help you really know your code, not
just what’s happening line by line, but also the bigger concepts behind it.
Knowing the logic behind classes will train you to think logically so you can
write programs that effectively address almost any problem you encounter.

Classes also make life easier for you and the other programmers you’ll
work with as you take on increasingly complex challenges. When you and
other programmers write code based on the same kind of logic, you’ll be
able to understand each other’s work. Your programs will make sense to
many collaborators, allowing everyone to accomplish more.

#### Creating and Using a class
You can model almost anything using classes. Let’s start by writing a simple
class, Dog, that represents a dog—not one dog in particular, but any dog. What do we know about most pet dogs? Well, they all have a name and age.
We also know that most dogs sit and roll over. Those two pieces of information
(name and age) and those two behaviors (sit and roll over) will go
in our Dog class because they’re common to most dogs. This class will tell
Python how to make an object representing a dog. After our class is written,
we’ll use it to make individual instances, each of which represents one specific
dog.

###### The __init__() Method
A function that’s part of a class is a method. Everything you learned about
functions applies to methods as well; the only practical difference for now is
the way we’ll call methods. The __init__() method at w is a special method
that Python runs automatically whenever we create a new instance based
on the Dog class. This method has two leading underscores and two trailing
underscores, a convention that helps prevent Python’s default method
names from conflicting with your method names. Make sure to use two
underscores on each side of __init__(). If you use just one on each side, the
method won’t be called automatically when you use your class, which can
result in errors that are difficult to identify.

#### Working with Classes and Instances
You can use classes to represent many real-world situations. Once you write a class, you'll spend most of your time working with instances created from that class. One of the first tasks you'll want to do is modify the attributes associated with a particular instance. You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

#### Incrementing an Attribute’s Value Through a Method
Sometimes you’ll want to increment an attribute’s value by a certain
amount rather than set an entirely new value. Say we buy a used car and
put 100 miles on it between the time we buy it and the time we register it.
Here’s a method that allows us to pass this incremental amount and add
that value to the odometer reading:
```chapter9/car.py```

You can use methods like this to control how users of your program update values
such as an odometer reading, but anyone with access to the program can set the odometer
reading to any value by accessing the attribute directly. Effective security takes
extreme attention to detail in addition to basic checks like those shown here.

### Inheritance
You don't alwaays have to start from scratch when writing a class. If the class
you’re writing is a specialized version of another class you wrote, you can
use inheritance. When one class inherits from another, it takes on the attributes
and methods of the first class. The original class is called the parent
class, and the new class is the child class. The child class can inherit any
or all of the attributes and methods of its parent class, but it’s also free to
define new attributes and methods of its own.

#### The __init__() Method for a Child Class
When you’re writing a new class based on an existing class, you’ll often
want to call the `__init__()` method from the parent class. This will initialize
any attributes that were defined in the parent `__init__()` method and make
them available in the child class.

```chapter9/electric_car.py```

There’s no limit to how much you can specialize the `ElectricCar` class.
You can add as many attributes and methods as you need to model an electric
car to whatever degree of accuracy you need. An attribute or method
that could belong to any car, rather than one that’s specific to an electric
car, should be added to the Car class instead of the `ElectricCar` class.

#### Overriding Methods from the Parent Class
You can override any method from the parent class that doesn’t fit what
you’re trying to model with the child class. To do this, you define a method
in the child class with the same name as the method you want to override in
the parent class. Python will disregard the parent class method and only
pay attention to the method you define in the child class.
Say the class `Car` had a method called `fill_gas_tank()`. This method is
meaningless for an all-electric vehicle, so you might want to override this
method.

#### Instances as Attributes
