from pprint import pprint


class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')


class Shop:

    def __init__(self, __file_name='products.txt'):
        self.file_name = __file_name

    def get_products(self):
        file = open(self.file_name, 'r+', encoding='cp1252')
        read_file: str = file.read()
        file.close()
        return read_file

    def add(self, *products):
        file = open(self.file_name, "a+", encoding='cp1252')
        read_file1 = file.read()
        for i in products:
            if i is not read_file1:
                file.write(f'\n{i} - new file')
            else:
                file.write(f'\n{i} - old file\n')
        file.close()
        return file


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
