class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}."

    def take_photo(self):
        return f"Taking a photo with {self.brand} {self.model}."

class SuperSmartphone(Smartphone):
    def __init__(self, brand, model, storage, camera_quality):
        super().__init__(brand, model, storage)
        self.camera_quality = camera_quality

    def take_photo(self):
        return f"Taking a high-quality photo with {self.camera_quality}MP camera on {self.brand} {self.model}."

# Polymorphism Challenge
class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Animal:
    def move(self):
        return "Moving in an unspecified way."

# Example usage
if __name__ == "__main__":
    smartphone = Smartphone("Apple", "iPhone 14", "128GB")
    print("Smartphone Actions:")
    print(smartphone.make_call("123-456-7890"))
    print(smartphone.take_photo())
    print("\nSuper Smartphone Actions:")

    super_smartphone = SuperSmartphone("Samsung", "Galaxy S21", "256GB", 108)
    print(super_smartphone.take_photo())

    car = Car()
    plane = Plane()
    print(car.move())
    print(plane.move())
