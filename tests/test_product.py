
from src.product import Product


class TestProduct:
    def test_product_initialization(self):
        product = Product("Смартфон", "Мощный смартфон", 29999.99, 10)
        assert product.name == "Смартфон"
        assert product.description == "Мощный смартфон"
        assert product.price == 29999.99
        assert product.quantity == 10

    def test_price_setter_positive(self):
        product = Product("Ноутбук", "Игровой", 50000, 5)
        product.price = 45000
        assert product.price == 45000

    def test_price_setter_negative(self, capsys):
        product = Product("Мышь", "Беспроводная", 1000, 20)
        product.price = -500
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 1000  # цена не изменилась

    def test_price_setter_zero(self, capsys):
        product = Product("Клавиатура", "Механическая", 3000, 15)
        product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 3000

    def test_new_product_method(self):
        product_data = {
            "name": "Наушники",
            "description": "Беспроводные",
            "price": 2500,
            "quantity": 30,
        }
        product = Product.new_product(product_data)
        assert product.name == "Наушники"
        assert product.description == "Беспроводные"
        assert product.price == 2500
        assert product.quantity == 30
