# inheriting attributes

class Date(object):  # inherit from 'object' class
    def get_date(self):
        return '2022-03-13'


class Time(Date):  # inherit from 'Date' class
    def get_time(self):
        return '11:00:00'


dt = Date()
print('Get date from the Date class: ', dt.get_date())

tm = Time()
print('Get time from the Time class: ', tm.get_time())
print('Get date from the Time class by inheriting or calling Date class method: ',
      tm.get_date())  # found this method in 'Date' class
