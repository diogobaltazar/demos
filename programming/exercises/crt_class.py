import typing as t

class C:
    static_attribute: t.ClassVar[t.Dict[str, int]] = {}
    
    instance_attribute: int = 0

    def __init__(self, instance_attribute: int = 0, static_attribute: t.Dict[str, int] = {}):
        self.instance_attribute = instance_attribute
        self.static_attribute = static_attribute


c1 = C('attribute value 1', {'hey': 'there'})
c2 = C('attribute value 2')
print(c1.__dict__)
print(c2.__dict__)
print(C.static_attribute)

