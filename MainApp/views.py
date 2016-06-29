from django.shortcuts import render

# Create your views here.
companyName = 'Zoro company'

def home(request):
    myName = 'Pavel Silber'
    myRole = 'Django framework web-developer, HTML/CSS page designer, freelancer'
    myAge = '17.08.1988'
    myLanguages = 'Russian, Hebrew, Eglish'
    mySkills = 'HTML / CSS, Javascript / jQuery / AJAX / MySQL / Django  / Python'
    myExperience = 'Build interactive websaits since 2015'

    return render(request, 'index.html', {'myName':myName,
     						'myRole': myRole, 
     						'myAge':myAge,
     						'myLanguages':myLanguages,
     						'mySkills':mySkills,
     						'myExperience':myExperience,
     						})


def work(request):
    return render(request, 'work.html')


def contact(request):


    return render(request, 'contact.html', {'companyName': companyName})

    	# , {'companyName':companyName})
    						


def home2(request):
    return render(request, 'index2.html')