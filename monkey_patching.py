class A:
    def original_function(self):
        print("calling original function")


def monkey_function():
    print("monkey is called")


A.original_function = monkey_function



a = A
a.original_function()

