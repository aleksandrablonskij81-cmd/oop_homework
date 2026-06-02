class PrintMixin:
    """Миксин для вывода информации о созданном объекте"""

    def __init__(self, *args, **kwargs):
        """При создании объекта печатает информацию о классе и параметрах"""
        class_name = self.__class__.__name__
        # Формируем строку параметров для вывода
        params = ", ".join([repr(arg) for arg in args] + [f"{k}={repr(v)}" for k, v in kwargs.items()])
        print(f"Создан объект {class_name}({params})")
        # Не вызываем super().__init__, чтобы не передавать аргументы дальше
