class C:
    def __init__(self, attribute):
        self.attribute = attribute

c = C('attribute value')
print(c.__dict__)
print(c.__dir__())
