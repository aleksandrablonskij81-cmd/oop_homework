import pytest
from src.category import Category
from src.product import Product


class TestCategory:
    def test_category_initialization(self):
        products = [
            Product("Телефон", "Смартфон", 30000, 5),
            Product("Чехол", "Защитный", 1000, 15),
        ]
        category = Category("Электроника", "Все гаджеты", products)
        assert category.name == "Электроника"
        assert category.description == "Все гаджеты"

    def test_category_count_increment(self):
        initial_count = Category.category_count
        Category("Книги", "Художественная", [])
        assert Category.category_count == initial_count + 1

    def test_product_count_increment(self):
        initial_count = Category.product_count
        products = [Product("Книга", "Роман", 500, 10)]
        Category("Книги", "Литература", products)
        assert Category.product_count == initial_count + 1

    def test_add_product(self):
        category = Category("Игрушки", "Детские", [])
        product = Product("Кукла", "Игрушка", 1500, 5)
        initial_count = Category.product_count
        category.add_product(product)
        assert Category.product_count == initial_count + 1

    def test_products_getter(self):
        product1 = Product("Телефон", "Смартфон", 30000, 5)
        product2 = Product("Чехол", "Защитный", 1000, 15)
        category = Category("Электроника", "Гаджеты", [product1, product2])
        result = category.products
        assert "Телефон, 30000 руб. Остаток: 5 шт." in result
        assert "Чехол, 1000 руб. Остаток: 15 шт." in result

    def test_str_method(self):
        products = [
            Product("Телефон", "Смартфон", 30000, 5),
            Product("Чехол", "Защитный", 1000, 15)
        ]
        category = Category("Электроника", "Гаджеты", products)
        assert str(category) == "Электроника, количество продуктов: 20 шт."

    def test_middle_price(self):
        """Тест: средний ценник товаров в категории"""
        product1 = Product("Товар1", "Описание", 100, 1)
        product2 = Product("Товар2", "Описание", 200, 1)
        category = Category("Тест", "Описание", [product1, product2])
        assert category.middle_price() == 150

    def test_middle_price_empty(self):
        """Тест: средний ценник пустой категории возвращает 0"""
        category = Category("Тест", "Описание", [])
        assert category.middle_price() == 0
