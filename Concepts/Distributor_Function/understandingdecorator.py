def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function

class decorator_class(object):
    def __init__(self,original_function):
        self.original_function = original_function

    #Below function behaves just like Wrapper Function
    def __call__(self, *args, **kwargs):
        print('Call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print('Display function name')


@decorator_function
def display_info(name, age):
    print('Display info ran with arguments({},{})'.format(name, age))


# display_info = decorator_function(display_info) this statement is implicity getting called
display_info('Arlene', 23)
display()