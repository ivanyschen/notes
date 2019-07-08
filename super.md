# super()

```python
class Parent:

    def __init__(self):
        pass
    
    def method1(self):
        pass

class Child(Parent):
		
    def __init__(self):
      	super().__init__()
```

*  The first parameter of `super()` : refers to the subclass **above** which python starts to look for a method to inhere.
*  The order that Python uses to get the information for inherence is called method resolution order (mro). Use `__mro__` to get the mro of a class
*  For the second parameter:
   *  No second argument: the super object returned is unbound
   *  Second arguemtn is an object, the super object reutned is bounded and either `isinstance(obj, type)` or `issubclass(type2, type)` must be true.
*  In most cases, `super()` (without passing in any arguement) suffice.
