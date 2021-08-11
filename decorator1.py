def my_log(original_function):
    import logging

    def wraper_function(*args, **kwargs):
        logging.basicConfig(filename="{}.log".format(
            original_function.__name__), level=logging.INFO)
        logging.info('ran with argument {} and {}'.format(args, kwargs))
        return original_function(*args, **kwargs)

    return wraper_function


@my_log
def operateme(x, y, opt=""):
    if(opt == "add"):
        return x+y
    elif(opt == "multi"):
        return x*y
    else:
        return 0


print(operateme(5, 6, opt="add"))
