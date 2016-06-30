from django.shortcuts import render
from datetime import datetime, date, time

companyName = 'Zorozex company'
companyAdress = "795 Folsom Ave \nSuite 600 San Francisco \nCA 94107"
phoneNumber = '(123) 456-7890'
email = 'pavel@example.com'

# dayOfWeek = datetime.date.today()

workPlace = ['Google,', 'Apple,', 'Cisco']

pets = ''   # ['Cat,', 'Dog,', 'Elephent']

year = '2016'






def home(request):
    myName = 'pavel silber'
    myRole = 'Django framework web-developer, HTML/CSS page designer, freelancer'
    myAge = date(1988, 8, 17)
    myLanguages = 'Russian, Hebrew, Eglish'
    mySkills = 'HTML / CSS, Javascript / jQuery / AJAX / MySQL / Django  / Python'
    myExperience = 'Build interactive websaits since 2015'

    return render(request, 'index.html', {'myName':myName,

     						'myRole': myRole, 
     						'myAge':myAge,
     						'myLanguages':myLanguages,
     						'mySkills':mySkills,
     						'myExperience':myExperience,
     						'email':email,
     						'workPlace':workPlace,
     						'pets':pets,
     						# 'dayOfWeek':dayOfWeek,

     						})






def work(request):
    return render(request, 'work.html')


def contact(request):

	# Variables doesn't work here, in home function it does. strange!

    return render(request, 'contact.html', {'companyName': companyName, 
    										'companyAdress': companyAdress,
    										'phoneNumber': phoneNumber,
    										'email': email,
    										})

    						


def home2(request):
    return render(request, 'index2.html')


def base(request):
    return render(request, 'base.html', {'year': year})


def basetest(request):
    return render(request, 'basetest.html')