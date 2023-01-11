class StaticClass:
    def __new__(cls):
        raise TypeError(f"{cls.__name__} is static. It cannot be instantiated!")