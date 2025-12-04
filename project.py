import requests

class Product:
    URL = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"

    def __init__(self):
        self._data = self._fetch_data()
        
        user_input = int(input("""how would you like to proceed?
            1. Enter 1 to check the brand
            2 .Enter 2 to check the price
            3 .Enter 3 to check the category            
            """))
        
        if user_input == 1:
            print("brand: " , self.brand())
        elif user_input == 2:
            print("price: ", self.price())
        else:
            print("category:" , self.category())
    

    def _fetch_data(self):
        response = requests.get(self.URL)
        response = response.json()
        return response["data"]

    def brand(self):
        return self._data.get("brand")
    
    def price(self):
        return self._data.get("price")

    def category(self):
        return self._data.get("category")

prod = Product()

print(prod.price())

