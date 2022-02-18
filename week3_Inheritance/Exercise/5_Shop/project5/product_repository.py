class ProductRepository():
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name: str):
        product = [product for product in self.products if product_name == product.name]
        if product:
            return product[0]

    def remove(self, product_name):
        product = ProductRepository.find(self, product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join([f"{item.name}: {item.quantity}" for item in self.products])

