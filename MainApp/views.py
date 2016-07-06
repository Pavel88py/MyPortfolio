from django.shortcuts import render
from datetime import datetime, date, time
from .models import Work


companyName = 'Zorozex company'
companyAdress = "795 Folsom Ave \nSuite 600 San Francisco \nCA 94107"
phoneNumber = '(123) 456-7890'
email = 'pavel@example.com'

workPlace = ['Google,', 'Apple,', 'Cisco']

pets = ''   # ['Cat,', 'Dog,', 'Elephent']

year = '2016'






def home(request):
    myName = 'pavel silber'
    myRole = 'Django framework web-developer, HTML/CSS page designer, freelancer'
    myAge = date(1988, 8, 17)
    myLanguages = 'russian, hebrew, english'
    mySkills = 'HTML / CSS, Javascript / jQuery / AJAX / MySQL / Django  / Python'
    myExperience = 'Build interactive websaits since 2015'

    # work_list = [
    #             {"header": "My first work place", "desc": ''' "Vichay" '''},
    #             {"header": "My second work place", "desc": ''' "Flextronix" '''},
    #             {"header": "My Third work place", "desc": ''' "Shafir production" '''},  
    #             ]

    _work_places = Work.objects.all()


    return render(request, 'index.html', {'myName':myName,

     						'myRole': myRole, 
     						'myAge':myAge,
     						'myLanguages':myLanguages,
     						'mySkills':mySkills,
     						'myExperience':myExperience,
     						'email':email,
     						'workPlace':workPlace,
     						'pets':pets,
                            "work_places": _work_places},
                            )

##########################################################################################################
# <ul>
#             {%for item in high_education %}
#             <li>{{item.university}}, {{item.department}} отделение, {{item.faculty}} факультет</li>
#             {%empty %}
#                 Отсутствует
#             {%endfor %}
#         </ul>


# def study(request):
#     title_page='Обучение'
#     courses=Course.objects.all()

#     high_education=[{'university':'Казанский Государственный Университет им. В. И. Ульянова-Ленина',
#                      'department':'дневное',
#                      'faculty':'биолого-почвенный'}]


#     return render(request, 'study.html', {'title_page':title_page,  'high_education': high_education, 'courses':courses})

##########################################################################################################


def work(request):
    return render(request, 'work.html')


def contact(request):
    return render(request, 'contact.html', {'companyName': companyName, 
    										'companyAdress': companyAdress,
    										'phoneNumber': phoneNumber,
    										'email': email,
    										})

    
def base(request):
    return render(request, 'base.html')

