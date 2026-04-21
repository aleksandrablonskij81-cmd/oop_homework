import pytest
from src.product import Product
from src.category import Category


class TestCategory:
    def test_category_initialization(self):
        products = [
            Product("Телефон", "Смартфон", 30000, 5),
            Product("Чехол", "Защитный чехол", 1000, 15)
        ]
        category = Category("Электроника", "Все гаджеты", products)

        assert category.name == "Электроника"
        assert category.description == "Все гаджеты"
        assert len(category.products) == 2

    def test_category_count_increment(self):
        initial_count = Category.category_count
        category = Category("Книги", "Художественная литература", [])
        assert Category.category_count == initial_count + 1

    def test_product_count_increment(self):
        initial_count = Category.product_count
        products = [
            Product("Книга", "Роман", 500, 10),
            Product("Журнал", "Глянцевый", 300, 20)
        ]
        category = Category("Книги", "Литература", products)
        assert Category.product_count == initial_count + 2