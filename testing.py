import datetime

date_object = datetime.datetime.strptime('Sun 10/03, 8:05 PM', "%a %m/%d, %I:%M %p")


# Sun 10/03, 5:00 PM
# Sun 10/03, 5:00 PM
# Sun 10/03, 5:00 PM
# Sun 10/03, 5:00 PM
# Sun 10/03, 5:00 PM
# Sun 10/03, 5:00 PM
# Sun 10/03, 5:00 PM
# Sun 10/03, 5:00 PM
# Sun 10/03, 5:00 PM
# Sun 10/03, 8:05 PM
# Sun 10/03, 8:05 PM
# Sun 10/03, 8:25 PM
# Sun 10/03, 8:25 PM
# Mon 10/04, 12:20 AM
# Tue 10/05, 12:15 AM

if datetime.datetime.now().month > date_object.month:
    new_year=date_object.replace(year=(datetime.datetime.now().year + 1)) + datetime.timedelta(hours=-5)
else:
    new_year=date_object.replace(year=datetime.datetime.now().year) + datetime.timedelta(hours=-5)


string_object = datetime.datetime.strftime(new_year,"%a %m/%d, %I:%M %p")
print(string_object)





