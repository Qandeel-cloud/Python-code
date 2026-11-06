# classes and entities
class person:
    name = "Candle"
    occupation = "engineer"
    networth = "9999999$"

    # self (wo object jis k liye yeah method call kiya ja rha ha)

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = person()
b = person()

a.name = "Qandeel"
a.networth = "w233093894234093$"

b.name = "Fatima"
b.occupation = "Doctor"

a.info()
b.info()

#  so that is the benifit of using classes and objects. we can make many and many objects as much we want in a single class as we make a.person() and b.person()
#  we dont need to specify it for making it s


# print(a.name,a.networth)


