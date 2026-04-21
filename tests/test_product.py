from src.product import Product


class TestProduct:
    def test_product_initialization(self):
        product = Product("Смартфон", "Мощный смартфон", 29999.99, 10)
        assert product.name == "Смартфон"
        assert product.description == "Мощный смартфон"
        assert product.price == 29999.99
        assert product.quantity == 10
