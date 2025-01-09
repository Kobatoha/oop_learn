# Инкапсуляция - внутрянка класса, которая недоступна пользователю. Скрытые данные и методы - напрямую обращаться нельзя

# Наследование классов - каждый дочерний объект имеет все свойства и методы родительского класса

# Полиморфизм - можно единым образом работать с разными типами данных

def oop():
    def lesson_1():
        class Point:
            """Аннотация для описания класса и вызывается по Point.__doc__ или pt.__doc__"""

            color = 'red'  # атрибуты или свойства класса
            circle = 2

        a = Point()  # создание объекта класса
        b = Point()  # создание другого объекта класса

        type(a)  # Покажет, что а = принадлежит классу Point
        print(type(a) is Point)  # Покажет True, т.к. тип объекта класса и есть класс
        isinstance(a, Point)  # Покажет True, т.к. тип объекта класса и есть класс

        Point.circle = 1  # переопределение значения свойства класса Point

        a.color = 'green'   """ Переопределение значения свойства класса Point внутри объекта класса, 
                            т.е. у класса Point.color == 'red', а у a.color == 'green'.
                            После этогоо a.__dict__ уже не будет пустым """

        # Свойства:
        print(Point.__dict__)  # Покажет все атрибуты класса Point
        print(a.__dict__)  # Будет пустым, т.к. а берет атрибуты у родительского класса, а сам остается пустым
        print(Point.__doc__)  # Возвращает документацию класса

        # Функции:
        # Обращение к несуществующему свойству или методу класса вызовет ошибку:
        print(Point.a)  # отдаст значение атрибута, но если "а" - несуществующий атрибут Point то будет ошибка
        getattr(Point, 'a')  # другой способ получить значение атрибута, но если "а" существует, иначе будет ошибка
        getattr(Point, 'a', False)  # другой способ получить значение атрибута, но без ошибки, вместо нее вернет False

        # Проверка атрибута в классе по имени атрибута:
        hasattr(Point, 'prop')  # проверяем, есть ли такой атрибут в классе Point
        hasattr(a, 'circle')  # покажет не только атрибуты объекта, но и атрибуты класса

        # Динамическое добавление нового атрибута класса Point или изменение существующего:
        Point.type_pt = 'disc'  # напрямую
        setattr(Point, 'prop', 1)  # через setattr

        # Удаляет атрибут по имени атрибута:
        del Point.prop  # Удаляет атрибут класса, но если такого атрибута нет - будет ошибка
        delattr(Point, 'pt')  # Другой способ удалить атрибут, при отсутствии атрибута тоже будет ошибка
        del a.circle  # Будет ошибка, т.к. circle присутствует в классе Point, но не определен в объекте
        del a.color  # Удалит значение color в а, т.е. 'green' и значение color вернется к дефолтному 'red'

    def lesson_2():
        class Point:
            color = 'red'  # атрибуты или свойства класса
            circle = 2

            def set_coords(self, x, y):  # self -  ссылка на экземпляр класса
                self.x = x  # добавляет локальные атрибуты в конкретный экземпляр класса
                self.y = y

            def get_coords(self):
                return self.x, self.y

        pt = Point()  # создаем экземпляр класса
        pt.set_coords(1, 2)  # во входные данные для функции автоматически подставляется self
        Point.set_coords(pt, 1, 2)  # то же самое, что и pt.set_coords()
        print(pt.__dict__)  # отдает свойства экземпляра класса, которые созданы методом set_coords()
        print(pt.get_coords())

        pt2 = Point()
        pt2.set_coords(10, 20)

        # Имена методов класса set_coords, get_coords это те же самые атрибуты, только они ведут не на данные,
        # а на функции. Self - это ссылка на конкретный объект класса.

    def lesson_3():
        """ Магические методы класса облагаются двумя подчеркнутыми линиями с обеих сторон __init__, __del__
        Инициализация:
        __init__ и все, что описано в init создается в любом экземпляре класса по-умолчанию
        Финализация:
        __del__ вызывается перед удалением объекта класса, когда на него ничего не ссылается.

        Например, мы создали pt = Point(), а потом переопределили pt = 0.
        Но объект класса Point остался в памяти, хотя его переменная больше на него не ссылается.
        В таком случае происходит удаление объекта. И перед удалением будет вызван метод __del__ """

        class Point:
            color = 'red'  # атрибуты или свойства класса
            circle = 2

            def __init__(self, x=0, y=0):
                print('вызов __init__ для' + str(self))
                self.x = x
                self.y = y

            def __del__(self):
                print('Удаление экземпляра' + str(self))

            def set_coords(self, x, y):  # self -  ссылка на экземпляр класса
                self.x = x  # добавляет локальные атрибуты в конкретный экземпляр класса
                self.y = y

            def get_coords(self):
                return (self.x, self.y)

        alco = Point(1, 3)  # Создаем объект класса, ссылка на объект хранится в alco
        print(alco)  # Объект существует, alco ссылается на экземпляр класса
        print(alco.color)  # Экземпляр класса имеет доступ к атрибутам класса
        alco = 0  # alco теперь ссылается на другой объект и на экземпляр класса нет внешних ссылок
        # вызывается метод __del__ и происходит удаление объекта

    def lesson_4():
        """
        __new__ и singleton
        в __new__(cls) - cls это ссылка на текущий класс(на Point)
        а self ссылается экземпляр класса
        Все классы в python3 наследуются от object, где уже определен магический метод __new__(cls)
        и при создании класса __new__ должен возвращать адрес на создаваемый экземпляр класса,
        который мы берем из скрытого родителя object методом super().__new__(cls)

        т.е. __new__ существует в object, и мы его переопределяем в Point

        Паттерн Singleton - это создание только одного экземпляра класса. При создании экземпляра класса мы проверяем,
        был ли уже создан экземпляр класса, и если нет - создаем его. Если же экземпляр класса уже создан,
        то новая переменная будет ссылаться на уже существующий экземпляр класса
        """

        class DataBase:
            __instance = None  # ссылка на экземпляр класса

            def __new__(cls, *args, **kwargs):
                if cls.__instance is None:  # если ссылки нет
                    cls.__instance = super().__new__(cls)  # то мы создаем ссылку, беря ее у родительского класса object

                return cls.__instance  # возвращаем ссылку на созданный экземпляр класса

            def __del__(self):
                DataBase.__instance = None

            def __init__(self, user, psw, port):
                self.user = user
                self.psw = psw
                self.port = port

            def connect(self):
                print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

            def close(self):
                print('Закрытие соединения с БД')

            def read(self):
                return 'Данные из БД'

            def write(self, data):
                print(f'Запись в БД {data}')

    def lesson_5():
        """
        Декораторы @classmethod и @staticmethod

        @classmethod используется внутри класса, но не принадлежит его экземплярам, работает только с атрибутами класса
        @staticmethod не имеют доступа к атрибутам класса, ни к атрибутам его экземпляров. Такой метод работает
        сам по себе

        Обычные методы класса подразумеваются, что с они будут работать с экземплярами класса и с атрибутами класса

        """

        class Vector:
            MIN_COORD = 0
            MAX_COORD = 100

            """ @classmethod - определяется на уровне класса и работает исключительно с методами класса, и не может 
            обращаться к локальным атрибутам экземпляров класса """

            @classmethod
            def validate(cls, arg):
                return cls.MIN_COORD <= arg <= cls.MAX_COORD

            def __init__(self, x, y):
                self.x, self.y = 0, 0
                if self.validate(x) and self.validate(y):  # Прописывать имя класса внутри класса плохая практика
                    self.x = x
                    self.y = y

            def get_coord(self):
                return self.x, self.y

            @staticmethod  # используются без дополнительных аргументов, только то, что принимает метод, без ссылок
            def norm2(x, y):
                return x * x + y * y

        v = Vector(1, 3)
        Vector.validate(5)  # метод класса вызывается без аргумента cls, потому что он подставляется из коробки
        res = v.get_coord()  # == Vector.get_coord(v)
        print(res)

    def lesson_6():
        """
        Атрибут - public публичное свойство
        _атрибут - protected режим доступа (внутренняя служебная переменная и сигнал его не трогать)
        __атрибут - private режим доступа (служит для обращения только внутри класса)

        Суть инкапсуляции - взаимодействовать с атрибутами класса только через публичные методы

        Приватными могут быть и методы, и атрибуты, и обозначаются __метод и __атрибут

        Для лучшей защиты методов и атрибутов класса, можно использовать модуль accessify
        pip install accessify
        """
        from accessify import private

        class Poind:
            def __init__(self, x=0, y=0):
                self.__x, self.__y = 0, 0
                if self.__check_value(x) and self.__check_value(y):
                    self.__x = x
                    self.__y = y

            @private  # более надежная защита метода, даже через _Poind__check_value не получится обратиться
            @classmethod  # объявляем метод методом класса и вместо ссылки на экземпляр класса даем ссылку на сам класс
            def __check_value(cls, x):  # метод может использоваться только внутри класса и доступа к нему извне нет
                return type(x) in (int, float)  # проверка на то, что значение является числом

            def set_coord(self, x, y):
                if self.__check_value(x) and self.__check_value(y):
                    self.__x = x
                    self.__y = y
                else:
                    raise ValueError('Координаты должны быть числами')

            def get_coord(self):
                return self.__x, self.__y

        pt = Poind(1, 2)
        pt.set_coord(20, 10)  # сеттеры - передавать значения и проверять допустимость значений
        pt.get_coord()  # геттеры - получать значения
        print(dir(pt))  # отобразить все свойства класса от pt
        print(pt._Poind__x)  # плохой пример обращения к скрытым атрибутам
        print(pt._Poind__check_value(5))  # стоит @private из accessify и доступ к методу запрещен

    def lesson_7():
        """
        __setattr__(self, key, value)
        __getattribute(self, item)
        __getattr__(self, item)
        __delattr__(self, item)

        """

        class Point:  # 4 атрибута класса MIN_COORD, MAX_COORD, __init__, set_coord
            MIN_COORD = 100
            MAX_COORD = 0

            def __init__(self, x, y):
                self.x = x
                self.y = y

            def set_coord(self, x, y):
                self.x = x
                self.y = y

            """ Когда мы указываем self - то это всегда ссылка на экземпляр класса и новое значение в переменной 
            записывается в ближайшее пространство имен, т.е. в pt, а в Point значение атрибута остается неизменным.
            Метод для экземпляра класса: 
            def set_bound(self, left):
                self.MIN_COORD = left        
            """

            # Метод класса:
            @classmethod
            def set_bound(cls, left):
                cls.MIN_COORD = left

            # Метод автоматически вызывается, когда идет считывание атрибута через экземпляр класса
            # с помощью этого метода можем управлять обращением к тому или иному атрибуту класса
            def __getattribute__(self, item):  # переопределили магический метод
                if item == 'x':  # если обращаемся к x, то получим ошибку "доступ запрещен"
                    raise ValueError('Доступ запрещен')
                else:  # иначе вернем значение атрибута
                    return object.__getattribute__(self, item)

            # Вызывается каждый раз, когда идет присвоение атрибуту определенного значения
            # Мы можем запретить создавать какой-то атрибут в экземплярах класса
            def __setattr__(self, key, value):
                if key == 'z':
                    raise AttributeError("Недопустимое имя атрибута")
                else:
                    object.__setattr__(self, key, value)

            # Вызывается каждый раз, когда идет обращение к несуществующему атрибуту экземпляра класса
            # Если нам не нужна ошибка при обращении к несуществующему методу, мы можем переопределить его
            # И возвращать что-то другое, например False
            def __getattr__(self, item):
                return False

            # Вызывается каждый раз, когда удаляется определенный атрибут из экземпляра класса
            def __delattr__(self, item):
                print("__delattr__" + item)
                object.__delattr__(self, item)  # строчка, которая именно удаляет атрибут

        pt1 = Point(1, 2)  # создание экземпляра класса Point
        print(pt1.MAX_COORD)  # мы можем обращаться к атрибуту класса из его экземпляра
        pt1.set_bound(-100)  # значение атрибута меняется именно в пространстве имен класса из-за @classmethod
        print(Point.__dict__)
        print(pt1.yy)  # Обращаемся к несуществующему атрибуту и получаем False, тк переопределили __getattr__
        del pt1.x  # Вызывается __delattr__
        print(pt1.__dict__)  # Проверяем, что атрибут действительно удален

    def lesson_8():
        """
        Паттерн "Моносостояние"

        В многопоточном процессе в каждом отдельном потоке создается свой экземпляр класса. Нам нужно, чтобы в каждом
        экземпляре класса существовали единые локальные атрибуты и изменение в одном экземпляре класса так же вызывало
        изменение этого атрибута в других экземплярах класса. Как если бы разные объекты пользовались одним набором
        атрибутов на всех.

        Так как локальный словарь экземпляров класса __dict__ ссылается на общий словарь атрибутов класса, то любое
        изменение при обращении к локальному атрибуту на самом деле идет по ссылке к словарю атрибутов класса и меняет
        значение в нем. А раз каждый экземпляр класса ссылается на один словарь, то изменения происходят в каждом
        экземпляре класса.
        """

        class ThreadData:
            __shared_attrs = {
                'name': 'thread_1',
                'data': {},
                'id': 1
            }

            # Каждый раз, при создании нового экземпляра класса self.__dict__ (что является набором атрибутов экземпляра
            # класса) он будет ссылаться на атрибуты класса self.__shared_attrs
            def __init__(self):
                self.__dict__ = self.__shared_attrs

            # и в итоге каждый экземпляр будет создаваться с одним и тем же набором свойств

        th1 = ThreadData()  # Создаем экземпляр класса
        print(th1.__dict__)  # Проверяем, что локальные атрибуты созданы
        th2 = ThreadData()  # Создаем второй экземпляр класса
        print(th2.__dict__)  # Проверяем, что локальные атрибуты созданы и соответствуют атрибутам th1

        # Локальное пространство имен у обоих экземпляров класса оказывается единым, т.к. id=3 меняется и у th2, и у th1
        # Помимо этого добавление нового атрибута в th1, так же добавляет новый атрибут в th2
        th2.id = 3
        th1.attr_new = 'new_attr'

    def lesson_9():
        """
        Property - декоратор для использования setter, getter и deleter, который убирает много лишнего кода и облегчает
        обращение с закрытыми и приватными методами класса
        """

        class Person:
            def __init__(self, name, old):
                self.__name = name
                self.__old = old

            @property  # помечаем метод декоратором property - обязательно над сеттером.
            def old(self):  # прописываем геттер
                return self.__old

            @old.setter  # расширяем декоратор property сеттером, и нужно переименовать метод класса
            def old(self, old):  # прописываем сеттер, после расширения декоратором set_old >> get_old >> old
                self.__old = old

            @old.deleter  # удаляем приватное закрытое локальное свойство из экземпляра класса
            def old(self):
                del self.__old

            # property принимает геттер и сеттер методы, и при обращении к переменной old мы можем использовать обе функции
            # p.old - геттер, p.old = 35 - сеттер
            # Если в классе создан атрибут объекта property, то у нее высший приоритет перед локальным атрибутом
            # old = property(get_old, set_old)    легкое обращение к сеттерам и геттерам, вместо p.set_old и p.get_old

        p = Person('Sergey', 20)
        print(p.old)  # property(get_old)
        p.old = 35  # property(set_old)
        p.__dict__['old'] = 'old in object p'  # добавляем локальное свойство экземпляра класса
        print(p.old)  # даже при наличии локального свойства old будет использоваться property(get_old)
        print(p.__dict__['old'])  # к локальному свойству можно обратиться через __dict__
        del p.old  # Удаляем закрытое приватное свойство __old, а локальное old остается, т.к. у свойства property приоритет

    def lesson_10():
        """
        Объекты свойства - использование сеттеров и геттеров
        """
        from string import ascii_letters

        class Person:
            S_RUS = 'йцукенгшщзхъфывапролджэячсмитьбю-'
            S_RUS_UPPER = S_RUS.upper()

            def __init__(self, fio, old, passport, weight):
                self.verify_fio(fio)  # при создании экземпляра класса проверяем корректность значения fio

                self.__fio = fio.split()
                self.old = old  # можно сразу воспользоваться объектами свойствами
                self.passport = passport
                self.weight = weight

            @classmethod
            def verify_fio(cls, fio):
                if str != type(fio):  # проверяем, что значение fio - это строка
                    raise TypeError("ФИО должно быть строкой")

                f = fio.split()
                if len(f) != 3:  # проверяем, что формат fio - список из трех объектов
                    raise TypeError("Неверный формат ФИО")

                letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
                for s in f:
                    if len(s) < 1:
                        raise TypeError("В ФИО должен быть хотя бы один символ")
                    if len(s.strip(letters)) != 0:
                        raise TypeError("В ФИО можно использовать только буквенные символы и дефис")

            @classmethod
            def verify_old(cls, old):
                if int != type(old) or old < 14 or old > 120:
                    raise TypeError("Возраст должен быть целым числом в диапазоне [14, 120]")

            @classmethod
            def verify_weight(cls, weight):
                if float != type(weight) or weight < 20:
                    raise TypeError("Возраст должен быть целым числом в диапазоне [14, 120]")

            @classmethod
            def verify_passport(cls, passport):
                if str != type(passport):
                    raise TypeError("Паспорт должен быть строкой")

                s = passport.split()
                if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
                    raise TypeError("Неверный формат паспорта")

                for p in s:
                    if not p.isdigit():
                        raise TypeError("Серия и номер паспорта должны быть числами")

            @property
            def fio(self):
                return self.__fio

            @property
            def old(self):
                return self.__old

            @old.setter
            def old(self, old):
                self.verify_old(old)
                self.__old = old

            @property
            def weight(self):
                return self.__weight

            @weight.setter
            def weight(self, weight):
                self.verify_weight(weight)
                self.__weight = weight

            @property
            def passport(self):
                return self.__passport

            @passport.setter
            def passport(self, passport):
                self.__passport = passport

        p = Person('Тараканова Алла Федоровна', 48, '1234 567890', 88.8)  # создаем экземпляр
        print(p.weight)  # обращаемся к геттеру веса
        p.weight = 83.8  # обращаемся к сеттеру веса
        print(p.weight)  # обращаемся к геттеру веса
        p.passport = '2222 444555'  # обращаемся к сеттеру паспорта
        p.old = 100  # обращаемся к сеттеру возраста
        print(p.__dict__)  # обратимся к локальным атрибутам экземпляра класса

    def lesson_11():
        """
        Дескриптор данных - это универсальный класс, который описывает геттеры, сеттеры и делитеры для любых переменных
        класса с приватными свойствами.
        Дескриптор не данных - это класс, который содержит только геттер, может только считывать информацию.
        """

        # Реализация дескриптора данных:
        class Integer:
            # Проверка числа на соответствие допустимых значений
            @classmethod
            def verify_coord(cls, coord):
                if type(coord) != int:
                    raise TypeError("Координата должна быть целым числом")

            # Создание локального свойства экземпляра класса
            def __set_name__(self, owner, name):
                self.name = "_" + name

            # Геттер, который читает данные локального свойства экземпляра класса
            def __get__(self, instance, owner):
                # использование встроенных методов считается правильным решением
                return getattr(instance, self.name)  # == return instance.__dict__[self.name]

            # Сеттер, который присваивает локальному приватному атрибуту экземпляра класса соответствующее значение
            def __set__(self, instance, value):
                self.verify_coord(value)
                print(f"__set__: {self.name} = {value}")
                # instance ссылается на текущий экземпляр класса Point3D и создает
                # в этом экземпляре локальное свойство со значением value
                instance.__dict__[self.name] = value  # == setattr(instance, self.name, value)

        # Реализация дескриптора не-данных
        class ReadIntX:
            def __set_name__(self, owner, name):
                self.name = '_x'

            def __get__(self, instance, owner):
                return getattr(instance, self.name)

        class Point3D:
            # Интерфейсы взаимодействия с координатами x, y, z
            x = Integer()
            y = Integer()
            z = Integer()

            def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z

        p = Point3D('1', 2, 3)
        print(p.__dict__)
        print(p.x)

    def lesson_12():
        """
        __call__ - магический метод вызова. Когда мы вызываем c = Point(), то здесь срабатывает __call__ из метакласса, у
        самого же экземпляра класса с нет метода __call__ и мы не можем его вызвать как функцию, т.е. с() == ошибка.

        Магические методы так же называются dunder_методы (сокр. двойное подчеркивание с англ.)
        Экземпляры класса мы не можем вызывать как функции, т.к. у него нет методы __call__
        Классы, у которых прописан метод __call__ называются функторы.
        __call__ может использоваться для замыкания функции или создания класса декоратора
        """

        class Counter:
            def __init__(self):
                self.__counter = 0

            def __call__(self, *args, **kwargs):
                print("__call__")
                self.__counter += 1
                return self.__counter

        class StripChars:
            def __init__(self, chars):
                self.__counter = 0
                self.__chars = chars

            def __call__(self, *args, **kwargs):
                if not isinstance(args[0], str):
                    raise TypeError("Аргумент должен быть строкой")

                return args[0].strip(self.__chars)

        """
        c = Counter() -> круглые скобки, т.е. вызов класса - это вызов функции __call__
        простая схема что такое __cal__:
        __call__(self, *args, **kwargs):
            obj = self.__new__(self, *args, **kwargs)
            self.__init__(obj, *args, **kwargs)
            return obj
        """
        c = Counter()
        c()  # можно вызывать как функцию

    def lesson_13():
        """
         Магические методы
         __str__ - срабатывает в момент отображения информации об объекте класса в консоли (для пользователя)
         __repr__ - срабатывает в момент отображения информации об объекте класса в режиме отладки (служебная-отладочная)
         __len__ - позволяет применять функцию len() к экземплярам класса
         __abs__ - позволяет применять функцию abs() к экземплярам класса
        """

        class Cat:
            def __init__(self, name):
                self.name = name

            def __repr__(self):
                return f"{self.__class__}: {self.name}"

            def __str__(self):
                return f"{self.name}"

        cat = Cat("Murrka")

        class Point:
            def __init__(self, *args):
                self.__coords = args

            def __len__(self):
                return len(self.__coords)

            def __abs__(self):
                return list(map(abs, self.__coords))

        p = Point(1, 2)
        print(len(p))
        print(abs(p))

    def lesson_14():
        """
        Магические методы арифметических операций для экземпляров класса
        __add__ - сложение
        __sub__ - вычитание
        __mul__ - умножение
        __truediv__ - деление
        __floorfiv__ - целочисленное деление
        __mod__ - остаток от деления
        + добавить i для оператора '+=', '-=' etc
        """

        class Clock:
            __DAY = 86400

            def __init__(self, seconds: int):
                if not isinstance(seconds, int):
                    raise TypeError("Секунды должны быть целым числом")
                self.seconds = seconds % self.__DAY

            def get_time(self):
                s = self.seconds % 60
                m = (self.seconds // 60) % 60
                h = (self.seconds // 3600) % 24
                return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

            @classmethod
            def __get_formatted(cls, x):
                return str(x).rjust(2, "0")

            """
            c1 = c1 + 100 == c1.__add__(100) и возвращает НОВЫЙ экземпляр класса, а старый автоматически удаляется  
            """

            def __add__(self, other):
                if not isinstance(other, int | Clock):
                    raise ArithmeticError("Правый операнд должен быть типов int или объектом Clock")

                sc = other
                if isinstance(other, Clock):
                    sc = other.seconds

                return Clock(self.seconds + sc)

            # __radd__ указывает, что экземпляр класса находится справа от оператора сложения
            def __radd__(self, other):
                return self + other

            # __iadd__ указывает на оператор += и его переопределение позволяет производить сложение без создания нового
            # экземпляра класса
            def __iadd__(self, other):
                print('__iadd__')
                if not isinstance(other, int | Clock):
                    raise ArithmeticError("Правый операнд должен быть типов int или объектом Clock")

                sc = other
                if isinstance(other, Clock):
                    sc = other.seconds

                self.seconds += sc
                return self

        c1 = Clock(1000)
        c2 = Clock(2000)
        c1.seconds = c1.seconds + 100  # обращение к свойствам экземпляра класса для увеличения числа секунд

        print(c1.get_time())
        c1 += 100  # без __iadd__ операция += создает новый экземпляр класса
        c3 = c1 + c2  # при сложении двух экземпляров создается новый экземпляр, что позволяет сделать длинную цепочку +

    def lesson_15():
        """
        Магические методы сравнений:
        __eq__ - == equal to
        __ne__ - != not equal to
        __lt__ - < less than
        __le__ - <= less than or equal to
        __gt__ - > greater than
        __ge__ - >= greater than or equal to
        """

        class Clock:
            __DAY = 86400

            def __init__(self, seconds: int):
                if not isinstance(seconds, int):
                    raise TypeError("Секунды должны быть целым числом")

                self.seconds = seconds % self.__DAY

            # проверка на корректность данных и избежание дублирования кода
            @classmethod
            def __verify_data(cls, other):
                if not isinstance(other, int | Clock):
                    raise TypeError("Правый операнд должен быть типом int или объектом Clock")

                    # в sc будет число, если other является int, а иначе other.seconds, т.к. other - это экземпляр Clock
                return other if isinstance(other, int) else other.seconds

            # реализация для оператора сравнения
            def __eq__(self, other):
                sc = self.__verify_data(other)
                return self.seconds == sc

            def __lt__(self, other):
                sc = self.__verify_data(other)
                return self.seconds < sc

        c1 = Clock(1003)
        c2 = Clock(1000)
        print(c1 == c2)  # сравниваются адреса объектов в памяти устройства, но не их значения
        print(c1 != c2)  # если не определять оператор неравенства, то python обратится к методу __eq__, сделает
        # проверку и отдаст противоположный результат, т.к. это будет логическим результатом от метода равенства
        print(c1 < c2)  # сравниваются по магическому методу __lt__
        print(c1 > c2)  # не определен метод __gt__, но есть __lt__ и python самостоятельно меняет операнды
        # местами, чтобы подставить нужный знак <

    def lesson_16():
        """
        Вычисление хеша для объектов
        Каждый объект(селедка) имеет свой хеш(рыба) и он не меняется, но это не означает, что одинаковый хеш(рыба) ведет к
        одинаковым объектам(селедка)

        Если a == b, то равен и их хеш.
        Если hash(a) == hash(b), это не гарантирует, что a и b равны
        Если hash(a) != hash(b), то объекты точно не равны
        Изменяемые объекты являются нехешируемыми. В качестве ключей словаря можно использовать только хешируемые объекты.
        Поиск по хешу увеличивает скорость нахождения нужного объекта
        """

        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            # если добавить магические методы операторов сравнения, например, то стандартный алгоритм выявления хеша
            # перестает работать

            def __eq__(self, other):
                return self.x == other.x and self.y == other.y

            # вычисляем хеш не от экземпляров класса, а от координат точек этих экземпляров, и хеш двух разных экземпляров
            # будет равен и с точки зрения python это будет один и тот же объект
            def __hash__(self):
                return hash((self.x, self.y))

        p1 = Point(10, 20)
        p2 = Point(1, 2)

        print(hash(p1), hash(p2), sep="\n")  # хеш вычисляется у экземпляров класса, как у неизменяемых объектов
        print(p1 == p2)

        d = {p1: 1, p2: 2}
        print(d)

    def lesson_17():
        """
        Магические методы и функция bool()
        __len__ - вызывается функцией bool(), если не определен магический метод __bool__.
        __bool__ - вызывается в приоритетном порядке функцией bool()
        """

        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            # переопределив магический метод __len__ меняет свою работу и функция bool()
            def __len__(self):
                return self.x * self.x + self.y * self.y

            def __bool__(self):
                print('__bool__')
                return self.x == self.y

        # bool() всегда возвращает True для объектов пользовательских классов
        c = Point(10, 10)
        print(bool(c))
        print(len(c))
        if c:  # здесь неявно отрабатывает магический метод __bool__
            print('Объект c дает True')
        else:
            print('Объект c дает False')

    def lesson_18():
        """
        Магические методы:
        __getitem__(self, item) - получение значения по ключу item
        __setitem__(self, key, value) - запись значения value по ключу key
        __delitem__(self, key) - удаление элемента по ключу key

        Эти методы используются для работы с объектами, которые ведут себя как контейнеры
        (например, списки, словари, или пользовательские классы, имитирующие их).
        Они позволяют переопределить доступ к элементам по ключу или индексу.
        """

        class Student:
            def __init__(self, name, marks):
                self.name = name
                self.marks = marks

            def __getitem__(self, item):
                if 0 <= item < len(self.marks):
                    return self.marks[item]
                else:
                    raise IndexError("Неверный индекс")

            def __setitem__(self, key, value):
                if not isinstance(key, int) or key < 0:
                    raise TypeError("Индекс должен быть целым неотрицательным числом")

                if key >= len(self.marks):
                    off = key + 1 - len(self.marks)
                    self.marks.extend([None] * off)

                self.marks[key] = value

            def __delitem__(self, key):
                if not isinstance(key, int):
                    raise TypeError("Индекс должен быть целым неотрицательным числом")

                del self.marks[key]

        s1 = Student('Sergey', [5, 5, 3, 2, 5])
        print(s1.marks[2])  # выводим оценку с индексом 2
        print(s1[3])  # определили метод __getitem__ и можем напрямую обращаться к списку по индексу
        s1[16] = 5  # вызов магического метода __setitem__ с пользовательской обработкой ошибок
        print(s1.marks)
        del s1[2]  # вызов магического метода __delitem__ и удаление элемента списка по индексу

    def lesson_19():
        """
        Магические методы __iter__ и __next__
        __iter__ - получение итератора для перебора объекта
        __next__ - переход к следующему значению и его считывание
        """
        list(range(5))
        a = iter(range(5))
        next(a)

        # Пользовательский класс эквивалентный функции range(start, stop, step)
        class FRange:
            def __init__(self, start=0.0, stop=0.0, step=1.0):
                self.start = start
                self.stop = stop
                self.step = step

            def __iter__(self):
                self.value = self.start - self.step
                return self

            def __next__(self):
                if self.value + self.step < self.stop:
                    self.value += self.step
                    return self.value
                else:
                    raise StopIteration

        fr = FRange(0, 2, 0.5)
        # fr.__next__() == next(fr)
        # Последовательность без определения метода __iter__  - экземпляр класса fr является неитерируемым объектом и не
        # может использовать цикл for:
        for x in fr:
            print(x)

        # цикл for в разрезе - итератор + счетчик
        iter(fr)
        print(next(fr))
        print(next(fr))
        print(next(fr))
        print(next(fr))

        class FRange2D:
            def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
                self.rows = rows
                self.fr = FRange(start, stop, step)

            def __iter__(self):
                self.value = 0
                return self

            def __next__(self):
                if self.value < self.rows:
                    self.value += 1
                    return iter(self.fr)
                else:
                    raise StopIteration

        fr = FRange2D(0, 2, 0.5, 4)
        for row in fr:
            for x in row:
                print(x, end=' ')
            print()

    def lesson_20():
        """
        Наследование - класс определяется на основе другого.
        Родительский
            ^
        дочерний
        Вызывать методы внутри других методов можно только те методы, которые определены либо в базовом классе, либо в
        родительском классе. Вызывать в родительском классе метод дочернего класс может привезти к ошибкам.
        """

        class Geom:
            name = 'Geom'

            # self родительского класса может ссылаться не только на объекты базового (текущего класса), но и на экземпляры
            # дочерних классов, если метод вызван экземпляром дочернего класса. Все зависит от того, откуда вызван метод.
            def set_coords(self, x1, x2, y1, y2):
                self.x1 = x1
                self.x2 = x2
                self.y1 = y1
                self.y2 = y2

            def draw(self):
                print("Рисование примитива")

        class Line(Geom):
            name = 'Line'  # переопределение атрибута

            def draw(self):
                print("Рисование линии")

        class Rect(Geom):
            def draw(self):
                print("Рисование прямоугольника")

        class Circle(Geom):
            def no_draw(self):
                print("Не-рисование прямоугольника")

        g = Geom()
        print(g.name)
        line = Line()
        line.draw()
        print(
            line.name)  # сначала мы ищем атрибут в пространстве имен Line, затем поиск продолжается в базовом классе Geom

        line = Line()
        rect = Rect()
        line.set_coords(1, 1, 2, 2)  # set_coords сначала ищется в пространстве базового класса, если его не
        # находит, то идет дальше в родительский класс в поисках этого метода
        rect.set_coords(1, 1, 2, 2)
        print(line.__dict__)
        print(rect.__dict__)

        circle = Circle()
        circle.set_coords(1, 1, 1, 1)

    def lesson_21():
        """
        Наследование классов от класса object
        По-умолчанию все пользовательские классы создаются от родительского класса object, хоть явно это и не указывается.
        """

        class Geom:
            pass

        class Line(Geom):
            pass

        geom = Geom()
        line = Line()
        print(geom)  # вызывается метод __str__ из класса object
        # Наследование классов
        # issubclass работает только с классами
        print(issubclass(Geom, object))  # является ли класс Geom дочерним по отношению к классу object
        print(issubclass(Line, Geom))  # является ли класс Line дочерним по отношению к классу Geom
        print(issubclass(Line, object))  # является ли класс Line дочерним по отношению к классу object
        # isinstance работает и с классами, и с экземплярами класса
        print(isinstance(line, Geom))  # является ли экземпляр класса Line производным от класса Geom

        # Все стандартные типы данных являются классами, производными от object (list, int, str, tuple, dict, etc)
        print(issubclass(list, object))  # является ли класс list дочерним по отношению к классу object

        # Встроенные типы данных, то бишь классы, можно расширять:
        class Vector(list):
            def __str__(self):
                return " ".join(map(str, self))

        v = Vector([1, 2, 3])
        print(type(v))

    def lesson_22():
        """
        Наследование. Функция super() и делегирование
        """

        class Geom:
            name = 'Geom'

            def __init__(self, x1, y1, x2, y2):
                print(f"Инициализатор Geom для {self.__class__}")
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2

        # Расширение базового класса, если метод в дочернем классе отсутствует в родительском классе.
        # Переопределение базового класса, если метод в дочернем классе присутствует в родительском классе.
        class Line(Geom):
            def draw(self):
                print("Рисование линии")

        class Rect(Geom):
            def __init__(self, x1, y1, x2, y2, fill=None):
                # Geom.__init__(self, x1, y1, x2, y2) - явно указывать базовый класс очень-очень плохо
                # вызвать метод через super() - делегировать (переложить выполнение метода на базовый класс?) вызов
                super().__init__(x1, y1, x2,
                                 y2)  # Инициализатор базового класса следует вызывать в самую первую очередь
                print("Инициализатор Rect")
                self.fill = fill

            def draw(self):
                print("Рисование прямоугольника")

        line = Line(0, 0, 10, 20)
        # () вызывает метод __call__ из метакласса, который в свою очередь вызывает метод __new__, а затем метод __init__
        # Метод __init__ был найден в классе Geom, а метод __new__ не определен там, поэтому поиск пошел дальше - в object
        rect = Rect(1, 2, 3, 4)

        print(rect.__dict__)
        print(line.__dict__)

    def lesson_23():
        """
        Private атрибуты жестко привязываются к текущему классу, могут быть вызваны только в базовом классе и не могут
        быть вызваны в дочерних классах. __атрибут может быть использована только в том классе, в котором непосредственно
        определен.
        Protected атрибуты могут быть использованы в дочерних классах. Они предназначены для внутренней логики работы класса
        и их трогать не следует, но к ним можно обращаться.
        """

        class Geom:
            name = 'Geom'

            def __init__(self, x1, y1, x2, y2):
                print(f"Инициализатор Geom для {self.__class__}")
                self.__verify_coord(x1)
                self.__x1 = x1
                self.__y1 = y1
                self.__x2 = x2
                self.__y2 = y2

            def __verify_coord(self, coord):
                return 0 <= coord < 100

            def get_coords(self):
                return self.__x1, self.__y1

        class Rect(Geom):
            def __init__(self, x1, y1, x2, y2, fill='red'):
                super().__init__(x1, y1, x2, y2)
                self.__fill = fill

        rect = Rect(0, 0, 10, 20)
        rect.get_coords()
        print(rect.__dict__)

    def lesson_24():
        """
        Полиморфизм - это возможность работы с совершенно разными объектами (языка Python) единым образом.
        К разным объектам мы обращаемся через единый интерфейс (через одинаковый метод), но в каждом классе этот метод
        переопределен под нужды своего класса и отдает разный результат.
        Метод, который обязательно нужно переопределять в дочерних классах и не имеет своей собственной
            реализации, называется абстрактным
        """

        class Geom:
            def get_pr(self):
                raise NotImplementedError("В дочернем классе должен быть переопределен метод get_pr()")

        class Rectangle(Geom):
            def __init__(self, w, h):
                self.w = w
                self.h = h

            def get_pr(self):
                return 2 * (self.w + self.h)

        class Square(Geom):
            def __init__(self, a):
                self.a = a

            def get_pr(self):
                return 4 * self.a

        class Triangle(Geom):
            def __init__(self, a, b, c):
                self.a = a
                self.b = b
                self.c = c

            def get_pr(self):
                return self.a + self.b + self.c

        geom = [
            Rectangle(1, 2),
            Rectangle(3, 4),
            Square(10),
            Square(20),
            Triangle(1, 2, 3),
            Triangle(3, 4, 5)
        ]

        for g in geom:
            print(g.get_pr())

    def lesson_25():
        """
        Множественное наследование
        Плохой сеньор будет прописывать новую логику (например, логирование) либо в базовом классе, либо в классе выше.
        При множественном наследовании в python отрабатывает специальный алгоритм обхода базовых классов MRO
        Во вспомогательных базовых классах инициализаторы следует прописывать без параметров в избежании ошибок при
        множественном наследовании от базовых классах, у которой есть аргументы. То есть аргументы можно указывать только у
        базового класса.

        __mro__ это тот порядок, по которому функция super() будет перебирать базовые классы
        """

        class Goods:
            def __init__(self, name, weight, price):
                # как super узнал, что нужно идти в Mixin
                super().__init__()
                print("Init Goods")
                self.name = name
                self.weight = weight
                self.price = price

            def print_info(self):
                print(f"{self.name}, {self.weight}, {self.price}")

        # Хороший сеньор напишет отдельный класс
        class MixinLog:
            ID = 0

            def __init__(self):
                print("Init MixinLog")
                self.ID += 1
                self.id = self.ID

            def save_log(self):
                print(f"{self.id}: товар был продан в 00:00 часов")

            def print_info(self):
                print("print_info из MixinLog")

        class Notebook(Goods, MixinLog):
            def print_info(self):
                MixinLog.print_info(self)

        n = Notebook("acer", 1.5, 30000)
        n.print_info()
        n.save_log()
        # список обхода классов при поиске нужного аргумента и иерархия пути от дочернего до родительского
        print(Notebook.__mro__)

    def lesson_26():
        """
        __slots__ накладывает ограничения только на локальные атрибуты, но не на атрибуты класса. Объект класса занимает
        меньше памяти и ускорение работы с локальными свойствами.
        """
        import timeit

        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def calc(self):
                self.x += 1
                del self.y
                self.y = 0

        pt = Point(1, 2)

        class Point2D:
            __slots__ = ("x", "y")  # коллекция __dict__ не формируется и другие локальные свойства нельзя создавать

            def __init__(self, x, y):
                self.x = x
                self.y = y

            def calc(self):
                self.x += 1
                del self.y
                self.y = 0

        pt2 = Point2D(10, 20)

        print(timeit.timeit(pt.calc), timeit.timeit(pt2.calc))

    def lesson_27():
        """
        __slots__ накладывает ограничения на атрибуты экземпляра класса, но не мешает атрибутам самого класса
        """

        class Point1D:
            __slots__ = ("x", "y", "__length")

            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.__length = (x * x + y * y) ** 0.5

            @property
            def length(self):  # length не локальная переменная экземпляра класса, а атрибут класса Point2D
                return self.__length

            @length.setter
            def length(self, value):
                self.__length = value

        pt = Point1D(1, 2)
        pt.length = 10

        class Point2D:
            __slots__ = ("x", "y")

            def __init__(self, x, y):
                self.x = x
                self.y = y

        class Point3D(Point2D):
            pass

        pt3 = Point3D(10, 20)
        pt3.z = 30
        print(pt3.__dict__)
        print(pt3.__slots__)
        print(pt3.x)

    def lesson_33():
        """
        Вложенные классы.
        Внутренний класс создан для того, чтобы к нему обращался внешний класс, но не наоборот.
        Подобные вложения служит только ради удобства разработчика или в django, например.
        """

        class Women:
            title = "объект класса для поля title"
            photo = "объект класса для поля photo"
            ordering = "объект класса для поля ordering"

            def __init__(self, user, psw):
                self._user = user
                self._psw = psw
                self.meta = self.Meta(user + "@" + psw)

            class Meta:
                ordering = ['id']

                def __init__(self, access):
                    self._access = access
                    # self._t = Women.title - не следует обращаться к атрибутам внешнего класса из вложенных классов

        print(Women.ordering)
        print(Women.Meta.ordering)

        w = Women('root', '12345')
        print(w.Meta.ordering)
        print(w.__dict__)
        print(w.meta.__dict__)

    def lesson_34():
        """
        Метаклассы - это глубокая магия. Авада Кедавра
        Все в python - это объекты. И классы тоже объекты. Создает их метакласс. Метакаласс это вершина и отправная точка
        всех классов. Метакласс - это type(). Через type() можно динамически создавать классы.
        """

        class Point:
            MAX_COORD = 100
            MIN_COORD = 0

        class A:
            pass

        print(type(A))
        A = type('Point', (), {"MAX_COORD": 100, "MIN_COORD": 0})

    def lesson_35():
        """
        Пользовательские метаклассы.
        Две одинаковые записи. Обычное создание класса и динамическое создание класса.
        class Point:                    ==      A = type('Point', (), {"MAX_COORD": 100, "MIN_COORD": 0})
            MAX_COORD = 100
            MIN_COORD = 0
        """

        # Простейшая функция-метакласс:
        def create_class_point(name, base, attrs):
            attrs.update({"MAX_COORD": 100, "MIX_COORD": 0})
            return type(name, base, attrs)

        class Point(metaclass=create_class_point):
            def get_coords(self):
                return 0, 0

        pt = Point()
        print(pt.MAX_COORD)
        print(pt.get_coords())

        class Meta(type):
            def __new__(cls, name, base, attrs):
                attrs.update({"MAX_COORD": 200, "MIX_COORD": 0})
                return type.__new__(cls, name, base, attrs)

            # def __init__(cls, name, base, attrs):
            #     super().__init__(name, base, attrs)
            #     cls.MAX_COORD = 200
            #     cls.MIN_COORD = 0

        class Point2(metaclass=Meta):
            def get_coords(self):
                return 0, 0

        pt2 = Point2()
        print(pt2.MAX_COORD)
        print(pt2.get_coords())

    def lesson_36():
        """
        Использование метаклассов упрощает некоторый функционал, например, в Django
        """

        class Meta(type):
            def create_local_attrs(self, *args, **kwargs):
                # формирует локальных атрибутов для экземпляров дочерних классов
                for key, value in self.class_attrs.items():
                    self.__dict__[key] = value

            def __init__(cls, name, base, attrs):
                cls.class_attrs = attrs
                cls.__init__ = Meta.create_local_attrs  # инициализатор для экземпляров дочернего класса Women

        class Women(metaclass=Meta):
            title = 'заголовок'
            content = 'контент'
            photo = 'путь к фото'

        class Men(metaclass=Meta):
            head = 'head'
            arms = 'arms'
            legs = 'legs'


def solid():
    """
    S - принцип единой ответственности.
        Каждый класс должен отвечать только за одну операцию.
        Принцип служит для разделения типов поведения, благодаря которому ошибки, вызванные модификациями в одном
        поведении, не распространялись на прочие, не связанные с ним типы.
    O - принцип открытости-закрытости.
        Классы должны быть открыты для расширения, но закрыты для модификации.
        Принцип служит для того, чтобы делать поведение класса более разнообразным, не вмешиваясь в текущие операции,
        которые он выполняет. Благодаря этому вы избегаете ошибок в тех фрагментах кода, где задействован этот класс.
    L - принцип подстановки Liskov.
        Переопределение родительских методов без потери логики этих методов
        Необходимо, чтобы класс-потомок был способен обрабатывать те же запросы, что и родитель, и выдавать тот же
        результат. Или же результат может отличаться, но при этом относиться к тому же типу.
        Принцип служит для того, чтобы обеспечить постоянство: класс-родитель и класс-потомок могут использоваться
        одинаковым образом без нарушения работы программы.
    I - принцип разделения интерфейсов.
        Не следует ставить клиент в зависимость от методов, которые он не использует.
        Класс должен производить только те операции, которые необходимы для осуществления его функций. Все другие
        действия следует либо удалить совсем, либо переместить, если есть вероятность, что они понадобятся другому
        классу в будущем.
        Принцип служит для того, чтобы раздробить единый набор действий на ряд наборов поменьше – таким образом, каждый
        класс делает то, что от него действительно требуется, и ничего больше.
    D - принцип инверсии зависимостей.
        Модули верхнего уровня не должны зависеть от модулей нижнего уровня. И те, и другие должны зависеть от
        абстракций. Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
    """


def patterns():
    def singleton():
        """
        Гарантирует, что у класса будет только один экземпляр, и предоставляет глобальную точку доступа к нему.
        Когда нужен единый объект для управления ресурсами, например, логирование, доступ к базе данных.
        """

        class CatRegistry:
            _instance = None  # ссылка на экземпляр класса

            def __new__(cls, *args, **kwargs):
                if not cls._instance:  # если ссылки нет
                    cls._instance = super().__new__(cls)  # то мы создаем ссылку, беря ее у родительского класса object
                return cls._instance  # возвращаем ссылку на созданный экземпляр класса

        registry1 = CatRegistry()
        registry2 = CatRegistry()

        print(registry1 is registry2)

    def factory_method():
        """
        Что это за паттерн:
            Определяет интерфейс для создания объектов, но позволяет подклассам изменять тип создаваемого объекта.
        Для чего используется:
            Для создания объектов, тип которых может изменяться в зависимости от контекста.
        Плюсы и минусы:
            Плюсы: Избавляет от привязки к конкретным классам, упрощает расширение.
            Минусы: Увеличивает сложность кода.
        Сильные стороны:
            Гибкость при добавлении новых типов объектов.
        Уязвимости:
            Может привести к избыточной иерархии классов.
        """
        from abc import ABC, abstractmethod

        # Абстрактный базовый класс (Abstract Base Class) — используется для создания интерфейсов.
        class Cat(ABC):  # Это базовый абстрактный класс, представляющий интерфейс для всех видов кошек.
            @abstractmethod  # Декоратор, который указывает, что метод должен быть реализован в подклассе.
            def sound(self):  # метод обязан быть реализован в каждом конкретном подклассе.
                pass

        # Классы DomesticCat и WildCat реализуют конкретное поведение кошек.
        # Подкласс Cat, представляющий домашнюю кошку. Реализует метод sound, возвращающий "Мяу!".
        class DomesticCat(Cat):
            def sound(self):
                return "Мяу!"

        # Подкласс Cat, представляющий дикую кошку. Реализует метод sound, возвращающий "Р-р-р!".
        class WildCat(Cat):
            def sound(self):
                return "Р-р-р!"

        # Абстрактный класс CatFactory задает интерфейс для создания кошек.
        class CatFactory(ABC):  # это базовый абстрактный класс для фабрик.
            @abstractmethod
            def create_cat(self):
                pass

        # Классы DomesticCatFactory и WildCatFactory реализуют фабрики, которые создают конкретные типы кошек.
        class DomesticCatFactory(CatFactory):
            def create_cat(self):
                return DomesticCat()

        class WildCatFactory(CatFactory):
            def create_cat(self):
                return WildCat()

        # Создаем фабрику для домашних кошек
        domestic_factory = DomesticCatFactory()
        domestic_cat = domestic_factory.create_cat()
        print(domestic_cat.sound())  # Вывод: "Мяу!"

        # Создаем фабрику для диких кошек
        wild_factory = WildCatFactory()
        wild_cat = wild_factory.create_cat()
        print(wild_cat.sound())  # Вывод: "Р-р-р!"

        # Фабрика скрывает детали создания объектов, предоставляя единый интерфейс для их создания.
        # Управляет созданием одного объекта.
        # Реализация добавляет один уровень абстракции (базовый класс с фабричным методом).
        # Определяет интерфейс для создания объекта, но оставляет подклассам возможность изменить тип создаваемого
        # объекта.
        # Когда нужно делегировать создание объекта подклассам. Например, если вы хотите, чтобы каждый подкласс
        # создавал свои уникальные версии объекта.

    def decorator():
        """
        Что это за паттерн:
            Позволяет динамически добавлять объекту новую функциональность, не изменяя его структуру.
        Для чего используется:
            Когда нужно расширить функциональность объекта без изменения его кода.
        Плюсы и минусы:
            Плюсы: Удобен для добавления функциональности.
            Минусы: Увеличивает сложность кода при множественном использовании.
        Сильные стороны:
            Гибкость в добавлении поведения.
        Уязвимости:
            Может запутывать, если декораторов слишком много.
        """

        class Cat:  # Класс Cat представляет базовый объект — кошку.
            def sound(self):
                return 'Мяу!'

        class LoudCatDecorator:  # класс-декоратор, который принимает объект cat
            def __init__(self, cat):
                self.cat = cat  # Сохраняет ссылку на объект cat, чтобы расширить его функциональность.

            # преобразует результат в верхний регистр с помощью .upper() и добавляет "!!!".
            def sound(self):
                return self.cat.sound().upper() + "!!!"

        class PurringCatDecorator:
            def __init__(self, cat):
                self.cat = cat

            def sound(self):
                return "Мурр... " + self.cat.sound()

        cat = Cat()  # создаем экземпляр класса Cat
        loud_cat = LoudCatDecorator(cat)  # оборачиваем объект cat в декоратор LoudCatDecorator.
        purring_cat = PurringCatDecorator(cat)
        print(loud_cat.sound())
        print(purring_cat.sound())
        loud_purring_cat = LoudCatDecorator(PurringCatDecorator(cat))  # можно комбинировать
        print(loud_purring_cat.sound())

        # Поведение объектов можно изменять динамически.
        # Базовый класс Cat не изменяется, что упрощает поддержку и расширение кода.

    def observer():
        """
        Что это за паттерн:
            Определяет зависимость "один ко многим", при которой изменение состояния одного объекта уведомляет все
            зависимые объекты.

        Для чего используется:
            Для создания системы подписки, например, для уведомлений.

        Плюсы и минусы:

            Плюсы: Хорошо подходит для динамического взаимодействия объектов.
            Минусы: Может быть сложно отладить.

        Сильные стороны:
            Удобен для построения событийных систем.

        Уязвимости:
            Если подписчиков много, производительность может снизиться.
        """

        # Объект Cat является издателем событий. Когда он "мяукает", он уведомляет всех подписанных наблюдателей,
        # чтобы они могли отреагировать.
        class Cat:
            def __init__(self, name):
                self.name = name  # Имя кота, чтобы можно было различать экземпляры.
                self.observers = []  # Список, в котором хранятся все наблюдатели, подписанные на события этого кота.

            def add_observer(self, observer):  # Добавляет объект-наблюдатель в список observers
                self.observers.append(observer)  # позволяет динамически добавлять или удалять наблюдателей, которые
                # хотят следить за действиями кота.

            # Когда кот "мяукает" или совершает другое действие, метод уведомляет всех подписанных наблюдателей, чтобы
            # те могли выполнить свои задачи, связанные с этим событием.
            def notify_observers(self):
                for observer in self.observers:  # Проходит по всем наблюдателям в списке observers
                    observer.update(self)  # Вызывает метод update у каждого наблюдателя, передавая ссылку на
                    # текущий объект Cat.

        class CatObserver:
            # метод вызывается Cat при уведомлении.
            def update(self, cat):  # объект cat как аргумент, чтобы знать, кто вызвал уведомление.
                print(f"{cat.name} сделал 'Мяу!'")  # сообщение о том, что кот мяукнул.

            # Наблюдатель реагирует на событие, генерируемое издателем. В данном случае, он просто выводит сообщение, но
            # в реальных приложениях это может быть запись в журнал, отправка уведомления или любое другое действие.

        cat = Cat("Барсик")
        observer1 = CatObserver()
        observer2 = CatObserver()

        cat.add_observer(observer1)
        cat.add_observer(observer2)

        cat.notify_observers()  # все наблюдатели получают сообщение о действиях кота

        # Cat не знает, что делают его наблюдатели. Он просто уведомляет их о событиях.
        # Наблюдатели сами решают, как реагировать на уведомление.
        # Можно добавлять, удалять или заменять наблюдателей без изменения кода Cat.
        # Используется в графических интерфейсах (например, обновление интерфейса при изменении данных).
        # В системах подписки/уведомлений (например, уведомления по email).
        # В игровых движках (например, уведомление об изменении состояния объекта).

    def abstract_factory():
        """
        Предоставляет интерфейс для создания семейств взаимосвязанных объектов, не уточняя их конкретные классы.
        Когда нужно создавать семейства взаимосвязанных объектов, которые должны использоваться вместе.
        Содержит несколько методов для создания объектов разных типов.
        Реализуется как отдельный класс, который предоставляет методы для создания нескольких взаимосвязанных объектов.
        Одна фабрика создает семейство объектов (кот и его игрушка).
        Управляет созданием семейства объектов.
        Реализация сложнее, так как нужно учитывать больше типов объектов и их взаимосвязи.
        """

        from abc import ABC, abstractmethod

        # Абстрактные продукты задают общую структуру для всех продуктов, чтобы клиентский код мог работать
        # с ними независимо от их конкретных реализаций.
        class Cat(ABC):  # базовые классы (интерфейсы) для продуктов, которые будут создаваться фабриками.
            @abstractmethod
            def sound(self):
                pass

        class CatToy(ABC):
            @abstractmethod
            def play(self):
                pass

        # Конкретные продукты для домашних котов
        class DomesticCat(Cat):
            def sound(self):
                return "Мяу!"

        class Ball(CatToy):
            def play(self):
                return "Домашний кот играет с мячиком."

        # Конкретные продукты для диких котов
        class WildCat(Cat):
            def sound(self):
                return "Р-р-р!"

        class Stick(CatToy):
            def play(self):
                return "Дикий кот играет с палкой."

        # Абстрактная фабрика
        class CatFactory(ABC):
            @abstractmethod
            def create_cat(self):
                pass

            @abstractmethod
            def create_toy(self):
                pass

        # Конкретная фабрика для домашних котов
        class DomesticCatFactory(CatFactory):
            def create_cat(self):
                return DomesticCat()

            def create_toy(self):
                return Ball()

        # Конкретная фабрика для диких котов
        class WildCatFactory(CatFactory):
            def create_cat(self):
                return WildCat()

            def create_toy(self):
                return Stick()

        # Клиентский код
        # Функция, которая использует фабрику для создания кота и игрушки.
        def client_code(factory: CatFactory):  # через интерфейс CatFactory неизвестно какая конкретная фабрика передана
            cat = factory.create_cat()
            toy = factory.create_toy()
            print(cat.sound())
            print(toy.play())

        # Использование
        # Клиентский код вызывается с разными фабриками, что приводит к созданию разных семейств объектов.
        print("Домашний кот:")
        client_code(DomesticCatFactory())

        print("\nДикий кот:")
        client_code(WildCatFactory())

        # Позволяет создавать логически связанные объекты (например, коты и их игрушки).
        # Клиентский код не зависит от конкретных классов создаваемых объектов.
        # Легко добавлять новые семейства объектов, просто создавая новую фабрику.
        # Используется, когда нужно создавать объекты, которые должны работать вместе (например, элементы
        # пользовательского интерфейса для разных платформ).

    def builder():
        """
        Паттерн Builder используется для пошагового создания сложных объектов. Он позволяет создавать объекты, которые
        состоят из множества частей, без необходимости указывать их порядок или процесс сборки в клиентском коде.
        В DjangoORM этот паттерн позволяет строить запросы к базе данных по частям, что упрощает чтение и поддержку кода
        """
        from abc import ABC, abstractmethod

        # Класс, представляющий объект, который мы будем строить
        class Cat:
            def __init__(self):
                self.name = None
                self.breed = None
                self.color = None
                self.accessories = []

            def __str__(self):  # переопределяем пользовательский вывод
                return (
                    f"Кот: {self.name}, Порода: {self.breed}, Цвет: {self.color}, "
                    f"Аксессуары: {', '.join(self.accessories) if self.accessories else 'нет'}"
                )

        # Универсальный строитель для котов
        # Абстрактный строитель
        class CatBuilder(ABC):
            def __init__(self):
                self.cat = Cat()

            @abstractmethod
            def set_name(self, name):
                pass

            @abstractmethod
            def set_breed(self, breed):
                pass

            @abstractmethod
            def set_color(self, color):
                pass

            @abstractmethod
            def add_accessory(self, accessory):
                pass

            def get_cat(self):
                return self.cat

        # Конкретный строитель для домашнего кота
        class DomesticCatBuilder(CatBuilder):
            def set_name(self, name):
                self.cat.name = name

            def set_breed(self, breed):
                self.cat.breed = breed

            def set_color(self, color):
                self.cat.color = color

            def add_accessory(self, accessory):
                self.cat.accessories.append(accessory)

        # Конкретный строитель для дикого кота
        class WildCatBuilder(CatBuilder):
            def set_name(self, name):
                self.cat.name = name

            def set_breed(self, breed):
                self.cat.breed = breed

            def set_color(self, color):
                self.cat.color = color

            def add_accessory(self, accessory):
                self.cat.accessories.append(accessory)

        # Директор управляет процессом сборки. Он использует строитель для создания конкретных вариаций котов.
        # Это позволяет клиентскому коду не заботиться о деталях процесса сборки.
        # Директор полезен, если у нас есть повторяющиеся сценарии сборки (Домашние коты всегда имеют имя, породу, цвет
        # и аксессуары определенного типа или Дикие коты имеют другие характеристики.)
        class CatDirector:
            def __init__(self, builder: CatBuilder):
                self.builder = builder

            def construct_cat(self, name, breed, color, accessories):
                self.builder.set_name(name)
                self.builder.set_breed(breed)
                self.builder.set_color(color)
                for accessory in accessories:
                    self.builder.add_accessory(accessory)
                return self.builder.get_cat()

        # Использование
        domestic_builder = DomesticCatBuilder()
        wild_builder = WildCatBuilder()

        # Создаем домашнего кота
        domestic_director = CatDirector(domestic_builder)
        domestic_cat = domestic_director.construct_cat(
            name="Барсик",
            breed="Персидский",
            color="Белый",
            accessories=["Колокольчик", "Игрушка-мышка"]
        )

        # Создаем дикого кота
        wild_director = CatDirector(wild_builder)
        wild_cat = wild_director.construct_cat(
            name="Тигр",
            breed="Амурский тигр",
            color="Оранжевый с черными полосами",
            accessories=["Палка", "Когти"]
        )

        print(domestic_cat)
        # Кот: Барсик, Порода: Персидский, Цвет: Белый, Аксессуары: Колокольчик, Игрушка-мышка

        print(wild_cat)
        # Кот: Тигр, Порода: Амурский тигр, Цвет: Оранжевый с черными полосами, Аксессуары: Палка, Когти

        # Строитель концентрируется на деталях создания объекта.
        # Клиентский код или директор управляет процессом, не вникая в детали.
        # Если объект состоит из множества частей, паттерн Builder упрощает управление процессом создания.
        # Легко добавить новые типы объектов (например, уличного кота) или этапы сборки.
        # Код становится более организованным и легким для понимания.

    def prototype():
        """
        Паттерн Prototype позволяет создавать объекты на основе уже существующих, клонируя их. Это полезно, когда
        создание объекта с нуля — сложная или затратная операция.
            Быстрое создание новых объектов, похожих на уже существующие.
            Избегание повторной инициализации сложных объектов.
            Упрощение создания множества похожих объектов.
            Уменьшает количество дублирующего кода.
            Позволяет динамически изменять клонируемые объекты.
        Если объект имеет сложную структуру, глубокое копирование может быть непростым.
        """
        import copy

        class Cat:  # основной класс для представления котов.
            # принимает параметры: имя, породу, цвет и список аксессуаров.
            def __init__(self, name, breed, color, accessories=None):
                self.name = name
                self.breed = breed
                self.color = color
                self.accessories = accessories or []

            def __str__(self):  # используется для удобного вывода информации о коте.
                accessories = ", ".join(self.accessories) if self.accessories else "нет"
                return (
                    f"Кот: {self.name}, Порода: {self.breed}, Цвет: {self.color}, "
                    f"Аксессуары: {accessories}"
                )

            # Использует модуль copy для создания глубокой копии объекта. Это важно, чтобы клонированный объект был
            # полностью независим от оригинала.
            def clone(self):
                # Создаем глубокую копию объекта
                return copy.deepcopy(self)

        # Использование
        # Создаем оригинального кота
        original_cat = Cat(
            name="Барсик",
            breed="Персидский",
            color="Белый",
            accessories=["Колокольчик", "Игрушка-мышка"]
        )

        # Клонируем оригинального кота и изменяем параметры
        # Оригинальный кот остается неизменным.
        # Клонированный кот имеет свои уникальные параметры.
        cloned_cat = original_cat.clone()
        cloned_cat.name = "Мурзик"
        cloned_cat.color = "Серый"
        cloned_cat.accessories.append("Шарфик")

        # Печатаем результаты
        print(original_cat)
        # Кот: Барсик, Порода: Персидский, Цвет: Белый, Аксессуары: Колокольчик, Игрушка-мышка

        print(cloned_cat)
        # Кот: Мурзик, Порода: Персидский, Цвет: Серый, Аксессуары: Колокольчик, Игрушка-мышка, Шарфик

        # Когда использовать паттерн Prototype?
        #   Когда создание объекта с нуля сложно или дорого.
        #   Когда нужно создать множество похожих объектов с небольшими изменениями.
        #   Когда структура объекта может быть динамической, и вы хотите избежать повторного создания с нуля.
        # Паттерн Prototype позволяет эффективно клонировать объекты, избегая повторного создания сложных структур.
        # Он полезен в сценариях, где нужно быстро создать похожие, но уникальные экземпляры.

    def adapter():
        """
        Паттерн Adapter (Адаптер) используется для того, чтобы адаптировать интерфейс одного класса к интерфейсу,
        который ожидает другой класс. Это позволяет объектам с несовместимыми интерфейсами работать вместе.
        Представь, что у тебя есть кот, который умеет мяукать, но ты хочешь, чтобы он издавал звук тигра.
        Паттерн адаптера поможет сделать так, чтобы кот мог "переиграть" свой звук, но при этом не менять саму
        структуру класса кота.
        Паттерн Adapter позволяет объектам с несовместимыми интерфейсами работать вместе. Он "оборачивает" объект с
        несовместимым интерфейсом, предоставляя ему нужный интерфейс.
        Для чего используется:
            Когда нужно интегрировать старый или сторонний код с новым, но интерфейсы несовместимы.
            Когда необходимо преобразовать один интерфейс в другой, чтобы классы могли работать вместе.
        Позволяет работать с устаревшими или сторонними библиотеками без изменения их исходного кода.
        Упрощает интеграцию различных компонентов системы.
        Слишком много адаптеров может усложнить архитектуру программы.
        """

        # Это обычный кот, который умеет мяукать. У него есть метод sound(), который возвращает строку "Мяу!".
        class Cat:
            def sound(self):
                return "Мяу!"

        # Это тигр, который издает рычание. У него есть метод roar(), который возвращает строку "Р-р-р!".
        class Tiger:
            def roar(self):
                return "Р-р-р!"

        # Это адаптер, который позволяет тигру издавать звук как кот.
        # Адаптер реализует метод sound(), который вызывает метод roar() у объекта Tiger.
        class TigerAdapter:
            def __init__(self, tiger):
                self.tiger = tiger

            # Адаптер "переводит" интерфейс тигра в интерфейс кота, позволяя использовать тигра там, где ожидается кот.
            def sound(self):
                # Адаптируем метод рычания тигра под интерфейс кота
                return self.tiger.roar()

        # Использование
        cat = Cat()  # создается объект Cat, который издает "Мяу!".
        print(f"Кот: {cat.sound()}")  # Мяу!

        tiger = Tiger()  # создается объект Tiger, который издает "Р-р-р!".
        # Создаем адаптер для тигра, чтобы тигр мог издавать звук кота.

        tiger_adapter = TigerAdapter(tiger)
        print(f"Тигр через адаптер: {tiger_adapter.sound()}")  # Р-р-р!

        # Когда необходимо использовать класс с интерфейсом, несовместимым с текущей системой.
        # Когда нужно интегрировать сторонние библиотеки или старый код с новым, не меняя их.
        # Когда необходимо адаптировать поведение объектов, но без изменения их внутренней логики.
        # Это особенно полезно для интеграции разных компонентов системы, старого кода или сторонних библиотек, когда
        # изменить их интерфейс невозможно или нежелательно.

    def bridge():
        """
        Паттерн Bridge (Мост) используется для разделения абстракции и ее реализации, чтобы они могли изменяться
        независимо друг от друга. Он позволяет избежать жесткой связи между абстракцией и ее реализацией, обеспечивая
        гибкость и расширяемость.
        Это позволяет изменять реализацию, не затрагивая абстракцию, и наоборот.
        Для чего используется:
            Когда необходимо разделить абстракцию и реализацию, чтобы они могли изменяться независимо.
            Когда нужно обеспечить гибкость в добавлении новых реализаций и абстракций.
            Когда абстракция и реализация могут изменяться часто, и нужно минимизировать зависимость между ними.
        """

        # Реализация: поведение кота
        class CatBehavior:  # это абстрактный класс, который определяет метод sound()
            def sound(self):
                pass

        class DomesticCatBehavior(CatBehavior):  # поведение домашнего кота
            def sound(self):  # метод sound() для домашнего кота, возвращая строку "Мяу!".
                return "Мяу!"

        class WildCatBehavior(CatBehavior):  # поведение дикого кота
            def sound(self):  # метод sound() для дикого кота, возвращая строку "Р-р-р!".
                return "Р-р-р!"

        # Абстракция: кот
        class Cat:
            def __init__(self, behavior: CatBehavior):
                self.behavior = behavior

            def perform_sound(self):
                return self.behavior.sound()

        # Использование
        domestic_cat = Cat(DomesticCatBehavior())  # Создаем объект Cat с поведением DomesticCatBehavior()
        wild_cat = Cat(WildCatBehavior())  # Создаем объект Cat с поведением WildCatBehavior()

        print(f"Домашний кот: {domestic_cat.perform_sound()}")  # выводит звук домашнего кота Мяу!
        print(f"Дикий кот: {wild_cat.perform_sound()}")  # выводит звук дикого кота Р-р-р!

        # Когда необходимо разделить абстракцию и реализацию, чтобы они могли изменяться независимо.
        # Когда требуется гибкость в добавлении новых абстракций и реализаций без необходимости изменять код.
        # Когда абстракция и реализация могут изменяться часто и нужно минимизировать зависимость между ними.

    def composite():
        """
        Паттерн Composite (Компоновщик) используется для организации объектов в древовидные структуры, которые могут
        быть обработаны одинаково, независимо от того, являются ли они отдельными объектами или группами объектов.
        Это позволяет создавать сложные структуры, где элементы могут быть как простыми объектами, так и составными,
        состоящими из других объектов.
        Для чего используется:
            Когда нужно работать с деревом объектов, где каждый объект или группа объектов должны быть обработаны
            одинаково.
            Когда нужно объединить объекты в структуру, которая может быть как простой, так и сложной.
        """
        from abc import ABC, abstractmethod

        # Компонент, представляющий общий интерфейс для всех объектов
        # абстрактный класс, который определяет метод sound().
        # Все коты, как простые, так и группы котов, должны реализовывать этот метод.
        class Cat(ABC):
            @abstractmethod
            def sound(self):
                pass

        # Листовой объект: Домашний кот
        class DomesticCat(Cat):
            def sound(self):  # реализуют метод sound(), который возвращает звук, который издает кот.
                return "Мяу!"

        # Листовой объект: Дикий кот
        class WildCat(Cat):
            def sound(self):  # реализуют метод sound(), который возвращает звук, который издает кот.
                return "Р-р-р!"

        # Композитный объект: Группа котов
        class CatGroup(Cat):
            def __init__(self):
                self.cats = []

            def add(self, cat: Cat):
                self.cats.append(cat)

            def remove(self, cat: Cat):
                self.cats.remove(cat)

            def sound(self):  # вызывает метод sound() для каждого кота в группе и соединяет их звуки с помощью |
                return " | ".join(cat.sound() for cat in self.cats)

        # Использование
        domestic_cat = DomesticCat()  # создаем экземпляр домашнего кота
        wild_cat = WildCat()  # создаем экземпляр дикого кота
        wild_cat2 = WildCat()  # создаем второй экземпляр дикого кота

        # Группа котов
        group_of_cats = CatGroup()  # создаем экземпляр группы котов
        group_of_cats.add(domestic_cat)  # добавляем к котам домашнего кота
        group_of_cats.add(wild_cat)  # добавляем к котам дикого кота
        group_of_cats.add(wild_cat2)  # добавляем к котам второго дикого кота

        # Вывод звуков котов
        print(f"Домашний кот: {domestic_cat.sound()}")  # Мяу!
        print(f"Дикий кот: {wild_cat.sound()}")  # Р-р-р!
        print(f"Группа котов: {group_of_cats.sound()}")  # Мяу! | Р-р-р! | Р-р-р!

        # Когда нужно работать с древовидной структурой объектов.
        # Когда объекты могут быть как простыми, так и составными, и нужно обрабатывать их одинаково.
        # Когда необходимо гибко управлять группами объектов, не зная заранее, какие объекты будут в группе.
        # Паттерн Composite позволяет работать с объектами и их группами одинаково.

    def facade():
        """
        Паттерн Facade (Фасад) используется для упрощения взаимодействия с системой, предоставляя единый интерфейс,
        который скрывает сложность подсистемы. Это позволяет клиентам взаимодействовать с системой через простой
        интерфейс, не беспокоясь о ее внутренней сложности.
        Он скрывает сложность и взаимодействие между компонентами, предоставляя клиенту только необходимый функционал
        через один интерфейс.
        Для чего используется:
            Когда необходимо упростить интерфейс сложной системы.
            Когда система состоит из множества классов, и необходимо предоставить простой способ взаимодействия с ними.
            Когда нужно скрыть детали реализации системы и предоставить клиентам только нужные функции.
            Упрощает использование сложной системы.
            Снижает количество классов, с которыми нужно взаимодействовать.
            Обеспечивает единообразие в работе с подсистемой.
        Может привести к слишком обобщенному интерфейсу, скрывающему важные детали.
        Если фасад слишком сложен, это может затруднить расширение системы.
        """

        class FeedingSystem:  # подсистема, которая занимается кормлением кота.
            def feed(self, cat):
                print(f"{cat.name} накормлен!")

        class PlayingSystem:  # подсистема, которая управляет игрой кота.
            def play(self, cat):
                print(f"{cat.name} играет с игрушкой!")

        class GroomingSystem:  # подсистема, которая отвечает за уход за шерстью кота.
            def groom(self, cat):
                print(f"{cat.name} ухожен!")

        # Фасад, который упрощает взаимодействие с подсистемами
        class CatCareFacade:
            def __init__(self, cat):  # принимает объект кота
                self.cat = cat
                self.feeding_system = FeedingSystem()  # использует все три подсистемы для ухода за котом
                self.playing_system = PlayingSystem()
                self.grooming_system = GroomingSystem()

            def take_care_of_cat(self):  # вызывает методы всех подсистем для выполнения всех действий с котом.
                self.feeding_system.feed(self.cat)
                self.playing_system.play(self.cat)
                self.grooming_system.groom(self.cat)

        # Класс кота
        class Cat:
            def __init__(self, name):
                self.name = name

        # Использование
        cat = Cat("Барсик")  # создаем объект кота cat с именем "Барсик".
        cat_care_facade = CatCareFacade(cat)  # создаем фасад, который управляет всеми действиями с котом

        # Использование фасада для ухода за котом
        cat_care_facade.take_care_of_cat()

        # Паттерн Facade помогает упростить взаимодействие со сложными подсистемами, предоставляя клиенту простой
        # интерфейс. В нашем примере фасад скрывает все детали взаимодействия с системой ухода за котами, предоставляя
        # клиенту удобный способ заботиться о коте, не беспокоясь о внутренней сложности системы.
