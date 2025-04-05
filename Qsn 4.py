class Dog:
    def make_sound(self):
        return "Woof! Woof!"

class Cat:
    def make_sound(self):
        return "Meow! Meow!"

def process_sound(sound_object):
    print(sound_object.make_sound())

# Example usage
dog = Dog()
cat = Cat()

process_sound(dog)  # Output: Woof! Woof!
process_sound(cat)  # Output: Meow! Meow!
