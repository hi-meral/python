try:

    with open("operateme.log") as f:
        pass

    x = 1/0

except FileNotFoundError as err:
    print(err)
except Exception as err:
    print(err)
else:
    print("congrats no error")
finally:
    print("ho liya, nikal lo")
