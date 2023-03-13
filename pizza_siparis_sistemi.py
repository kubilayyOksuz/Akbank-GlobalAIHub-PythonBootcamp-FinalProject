# Gerekli olan modüllerin eklenmesi
import csv
import datetime

# Menünün ve veritabanının aktif edilmesi
file = open('customer_database.csv', 'a+')
file_writer = csv.writer(file)
menu = open('menu.txt', 'r')

# Sipariş verebilmek için gerekli bilgilerin kullanıcıdan alınması
account = False
while account == False:
        print("Piton Pizza'ya hoş geldiniz! Siparişinizi verdikten 15 dakika sonra hazır olan siparişinizi gelip alabilirsiniz! Pizza alabilmek için öncelikle bilgileriniz gerekiyor.")
        id_number = input("TC kimlik numaranız: ")
        name = input("Adınız: ")
        surname = input("Soyadınız: ")
        account = True

# Menüyü ekrana bastıracak olan main fonksiyonu
def main():
    print(menu.read())
    
if __name__ == '__main__':
    main()

# Pizza üst sınıfının ve miras vereceği fonksiyonların tanımlanması
class Pizza:
    def get_cost(self):
        """Pizza Fiyatı"""
        return self.__class__.PRICE

    def get_description(self):
        """Pizza Açıklaması"""
        return self.__class__.DESC

# Pizza üst sınıfının alt sınıflarının ve fiyatları ile açıklamalarının tanımlanması
class Klasik(Pizza):
    PRICE = 35
    DESC = "Klasik pizzanın içerisinde pizza sosu, mozzarella, sucuk, mantar, zeytin ve mısır bulunmaktadır."

class Margarita(Pizza):
    PRICE = 30
    DESC = "Margarita pizzanın içerisinde pizza sosu, mozzarella, domates ve fesleğen vardır."

class Türk(Pizza):
    PRICE = 45
    DESC = "Türk pizzanın içerisinde pizza sosu, peynir, domates, sucuk, pastırma ve zeytin vardır."

class Sade(Pizza):
    PRICE = 25
    DESC = "Sade pizzanın içerisinde peynir vardır."

class Akdeniz(Pizza):
    PRICE = 35
    DESC = "Akdeniz pizzanın içerisinde pizza sosu, mozzarella, biber, mantar, domates, mısır ve peynir vardır."

class Tavuk(Pizza):
    PRICE = 35
    DESC = "Tavuklu pizzanın içerisinde pizza sosu, mozzarella, tavuk, biber, soğan ve barbekü sos vardır."

# Menüde pizzaların yanında yazan sayılar ile pizza seçebilme işlemi için dictionary oluşturma
pizza_list = {1: Klasik, 2: Margarita, 3: Türk, 4: Sade, 5: Akdeniz, 6: Tavuk}

# Kullanıcıdan pizza seçeneği alma işlemi
pizza_selection = int(input("Hangi pizzayı istersiniz (1-5)? "))

# Pizzanın fiyatının ve açıklamasının gösterilmesi
order = pizza_list[pizza_selection]().get_cost()
description = pizza_list[pizza_selection]().get_description()
print(pizza_list[pizza_selection].__name__, "pizza seçtiniz." + '\n' + description)

# Malzemeler üst sınıfının ve miras vereceği fonksiyonların tanımlanması
class Decorator:
    def get_cost(self):
        global order
        order += self.__class__.PRICE

    def get_description(self):
        return self.__class__.DESC

# Malzemeler üst sınıfının alt sınıflarının ve fiyatları ile açıklamalarının tanımlanması
class Zeytin(Decorator):
    PRICE = 0.8
    DESC = "Zeytin"

class Mantar(Decorator):
    PRICE = 0.75
    DESC = "Mantar"

class Peynir(Decorator):
    PRICE = 1.25
    DESC = "Keçi peyniri"

class Soğan(Decorator):
    PRICE = 1
    DESC = "Soğan"

class Mısır(Decorator):
    PRICE = 0.5
    DESC = "Mısır"

class Sucuk(Decorator):
    PRICE = 2
    DESC = "Sucuk"
    
class Salam(Decorator):
    PRICE = 1.5
    DESC = "Salam"

class Sosis(Decorator):
    PRICE = 1.75
    DESC = "Sosis"

class Biber(Decorator):
    PRICE = 0.6
    DESC = "Yeşil ve kırmızı biber"

class Fesleğen(Decorator):
    PRICE = 0.75
    DESC = "Fesleğen"

class Pepperoni(Decorator):
    PRICE = 1.5
    DESC = "Pepperoni"

# Menüde malzemelerin yanında yazan sayılar ile malzeme seçebilme işlemi için dictionary oluşturma
decorator_dict = {11: Zeytin, 12: Mantar, 13: Peynir, 14: Soğan, 15: Mısır, 16: Sucuk, 17: Salam, 18: Sosis, 19: Biber, 20: Fesleğen, 21: Pepperoni}

# Seçilen malzeme(ler)ni tutacak listenin oluşturulması
selected_decorators = []

# Kullanıcıya ekstra malzeme sorularının sorulması
extra = False
while extra == False:
    ask_for_extra = input("Pizzanın üstüne ekstra malzeme ister misiniz (y/n)? ")
    if ask_for_extra == "n":
        extra = True
    elif ask_for_extra == "y":
        decorator_selection = int(input("Hangi ekstra malzemeyi istersiniz (11-21)? "))
        decorator_dict[decorator_selection]().get_cost()
        decorator_description = decorator_dict[decorator_selection]().get_description()
        print(decorator_description)
        selected_decorators.append(decorator_dict[decorator_selection].__name__)

# Siparişteki ekstra malzemeler ve siparişin toplam fiyatının gösterilmesi
print("Seçtiğiniz ekstra malzemeler:", selected_decorators)
print("Siparişinizin toplam fiyatı:", order)

# Kart bilgilerinin alınması
card_information_filled = False
while card_information_filled == False:
    card_number = input("Kart numaranızı girin: ")
    expiring_date = input("Kartınızın son geçerlilik tarihini arada / ile girin: ")
    cvc = input("Kartınızın güvenlik şifresini girin: ")

    # Gerekli kart kontrollerinin yapılması
    if (len(card_number) != 16) or ('/' not in expiring_date) or (len(cvc) != 3):
        print("Kart bilgilerini hatalı girdiniz. Tekrar deneyin.")
        continue
    else:
        card_information_filled = True
 
# Siparişin tamamlanması
print("Siparişiniz oluşturulmuştur. Yaklaşık 15 dakika sonra gelip alabilirsiniz.")

# Alınan bilgilerin ve sipariş tarihinin veritabanına kaydedilmesi
file_writer.writerow([id_number, name, surname, pizza_list[pizza_selection].__name__, selected_decorators, card_number, expiring_date, cvc, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")])

# Açılan dosyaların kapanması
file.close()
menu.close()