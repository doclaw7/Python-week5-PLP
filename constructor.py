
# Adding an inheritance layer to explore polymorphism and encapsulation
class Smartphone:
    def __init__(self, color, brand, model, os):
        self.color = color
        self.brand = brand
        self.model = model
        self.os = os

    # Method to display details
    def display_details(self):
        print(f"Phone Details: {self.color} {self.brand} {self.model} {self.os}")


# Derived class for a specific type of smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, color, brand, model, os, gpu, refresh_rate):
        super().__init__(color, brand, model, os)
        self.__gpu = gpu  # Encapsulated attribute
        self.refresh_rate = refresh_rate

    # Overriding the display_details method to include gaming-specific details
    def display_details(self):
        super().display_details()
        print(f"Gaming Features: GPU: {self.__gpu}, Refresh Rate: {self.refresh_rate}Hz")


# Creating objects of the base and derived classes
phone1 = Smartphone("Red", "Samsung", "S20", "Android")
phone2 = Smartphone("Black", "Apple", "iPhone 12", "iOS")
gaming_phone = GamingSmartphone("Black", "Asus", "ROG Phone 5", "Android", "Adreno 660", 144)

# Displaying details of each phone

phone1.display_details()
phone2.display_details()
gaming_phone.display_details()