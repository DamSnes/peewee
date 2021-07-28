class Car:
    model = "Toyota"
    engine = 2


camry = Car()
camry.engine = 3.5
camry.name = "Camry"
delattr(camry, "engine")
print(camry.model, camry.name, camry.engine)
print(camry.__dict__)

supra = Car()
supra.engine = 4
supra.name = "Supra"
print(supra.model, supra.name, supra.engine)
print(supra.__dict__)
print(isinstance(supra, Car))


setattr(Car, "name", "")
Car.name = "Default"
print(Car.__dict__)

