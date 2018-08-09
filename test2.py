'''实现Singleton模式'''

# 方法1：通过__new__方法只创建一个实例
class Singleton1:
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance

# 方法2：共享属性，不同实例
class Singleton2:
    _storage = {}
    
    def __new__(cls,*args,**kwargs):
        instance = super().__new__(cls,*args,**kwargs)
        instance.__dict__ = cls._storage
        return instance

# 方法3：装饰器实现
def singleton(cls,*args,**kwargs):
    instances = {}
    def returnInstance():
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return returnInstance

@singleton
class MyClass:
    pass

# 方法4：import方法，import导入的模块在程序中只加载一次，本身单例。
# singleton.py
# class Singleton4:
#     pass
# instance = Singleton4()

# other.py
# from singleton import instance