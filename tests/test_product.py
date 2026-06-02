import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category


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

    def test_str_method(self):
        product = Product("Телефон", "Смартфон", 30000, 5)
        assert str(product) == "Телефон, 30000 руб. Остаток: 5 шт."

    def test_add_method(self):
        product1 = Product("Товар1", "Описание1", 100, 10)
        product2 = Product("Товар2", "Описание2", 200, 2)
        result = product1 + product2
        assert result == 100 * 10 + 200 * 2

    def test_add_method_wrong_type(self):
        product = Product("Телефон", "Смартфон", 30000, 5)
        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
            product + 100
def test_smartphone_inheritance():
    """Тест: Smartphone является наследником Product"""
    phone = Smartphone("TestPhone", "desc", 10000, 5, "proc", "model", 128, "red")
    assert isinstance(phone, Product) is True


def test_lawn_grass_inheritance():
    """Тест: LawnGrass является наследником Product"""
    grass = LawnGrass("TestGrass", "desc", 1000, 10, "Russia", 7, "green")
    assert isinstance(grass, Product) is True


def test_product_price_getter():
    """Тест геттера цены"""
    product = Product("Test", "desc", 5000, 3)
    assert product.price == 5000


def test_product_price_setter():
    """Тест сеттера цены (неотрицательная цена)"""
    product = Product("Test", "desc", 5000, 3)
    product.price = 7000
    assert product.price == 7000


def test_category_products_getter():
    """Тест геттера продуктов категории"""
    product = Product("Test", "desc", 100, 1)
    category = Category("TestCat", "desc", [product])
    # Проверяем, что в строковом выводе есть название продукта
    assert "Test" in category.products

