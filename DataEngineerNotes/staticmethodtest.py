class Test:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def static_method(num1):
        return f"Value is: {str(num1)}"  # Error: 'self' is not defined


print(Test.static_method(10))
# Here static method doesnt have self and hence it works directly, if it has self had to instantiate