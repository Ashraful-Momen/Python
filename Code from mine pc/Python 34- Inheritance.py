#Phone : Super class, Parent class , Base class,
#xiaomi: Sub Class , chile class , Derive class

class Phone:
    def call(self):
         print("You can call")

    def sms(self):
        print("You can massage")


class Xiaomi(Phone):
    def photo(self):
        print("You can take photo")


obj= Xiaomi()
obj.call()
obj.sms()
obj.photo()

print(issubclass(Xiaomi,Phone))
print(issubclass(Phone,Xiaomi))