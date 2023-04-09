class MySingleton(type):
    a = None

    def __call__(cls):
        if cls.a == None:
            # Если еще не создан ни один экземпляр класса:
            cls.a = super().__call__()
            return cls.a
        return cls.a


class MyClass(metaclass=MySingleton):
    def method1(self):
        pass

    def method2(self):
        print('небольшая проблема')


# Создание нескольких экземпляров класса и проверка их на идентичность
obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
print('obj_1 is obj_2 — ', obj_1 is obj_2)
print('obj_1 is obj_3 — ', obj_1 is obj_3)
