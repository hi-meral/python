def log_decorator(client_function):
    def wrapper_function(*args, **kwargs):
        print (f"{client_function.__name__}  {args},{kwargs} ")
        return client_function(*args, **kwargs)
    return wrapper_function

@log_decorator
def printMsg(msg,time="noon"):
    print(msg + time)

printMsg("Hey, call me in the ",time="morning")