class MyDate(object):

    def __init__(self,date) -> None:
        self.date = date

    @staticmethod
    def toDasDate(date):
        return date.replace('/','-')


mydate = MyDate('10/10/2020')


dateFromDB = '12-14-2020'

if (dateFromDB == mydate.toDasDate('12/12/2020')):
    print('Equal')

