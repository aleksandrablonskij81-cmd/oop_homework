from src.product import Product, Smartphone, LawnGrass
from src.category import Category

if __name__ == '__main__':
    # --- Обычные продукты ---
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("=== Обычные продукты ===")
    print(product1)
    print(product2)
    print(product3)

    # --- Смартфоны (новый класс) ---
    iphone = Smartphone("iPhone 15", "Флагман Apple", 120000.0, 10,
                        "A17 Pro", "15 Pro", 256, "чёрный")
    samsung = Smartphone("Galaxy S24", "Флагман Samsung", 110000.0, 15,
                         "Snapdragon", "S24 Ultra", 512, "фиолетовый")

    print("\n=== Смартфоны ===")
    print(iphone)
    print(samsung)

    # --- Газонная трава (новый класс) ---
    grass = LawnGrass("Райграс", "Для газонов", 1500.0, 50,
                      "Россия", 7, "зелёный")

    print("\n=== Газонная трава ===")
    print(grass)

    # --- Категории ---
    category_phones = Category("Смартфоны", "Смартфоны и аксессуары", [product1, product2, product3])
    category_phones.add_product(iphone)
    category_phones.add_product(samsung)

    print("\n=== Категория 'Смартфоны' ===")
    print(category_phones)
    print(category_phones.products)

    # --- Сложение одинаковых классов (должно работать) ---
    print("\n=== Сложение одинаковых классов ===")
    try:
        total_phones = iphone + samsung
        print(f"Сумма смартфонов: {total_phones} руб.")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # --- Сложение разных классов (должна быть ошибка) ---
    print("\n=== Сложение разных классов (должна быть ошибка) ===")
    try:
        total_mix = iphone + grass
        print(f"Сумма: {total_mix} руб.")
    except TypeError as e:
        print(f"Правильно! Ошибка: {e}")

    # --- Добавление неправильного объекта (должна быть ошибка) ---
    print("\n=== Добавление неправильного объекта в категорию ===")
    try:
        category_phones.add_product("это не товар")
    except TypeError as e:
        print(f"Правильно! Ошибка: {e}")

    print("\n✅ Все проверки пройдены!")