# 41.Over the millennia, different civilizations have used different ways to measure
# weights. Our metric system was introduced about 200 years ago and is based on
# the decimal (#10) system. The earliest known system was developed by the
# Sumerians about 6000 years ago, and is based on the sexagesimal (#60) system.
# This system was adopted and modified by many subsequent civilizations, but the
# ratio of 60 minas to 1 talent remained common. Using Django, create a talents to
# minas and minas to talents converter. For example, http://127.0.0.1:8000/
# converter/talents_to_minas/123 displays 7380 minas and http://127.0.0.1:8000/
# converter/minas_to_talents/7399 displays 123 talents and 19 minas


# in converter/urls.py:
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('talents_to_minas/<int:talents>/', views.talents_to_minas, name='views.talents_to_minus'),
#     path('minas_to_talents/<int:minas>/', views.minas_to_talents, name='views.minas_to_talents'),
# ]




# in views.py:

# from django.http import HttpResponse
# def index(request):
#     return HttpResponse('Supported conversions: minas_to_talents, talents_to_minas')

# def talents_to_minas(request,talents):
#     minas = talents * 60
#     return HttpResponse(f"{talents} talents = {minas} minas")
# #return HttpResponse(str(minas) + 'minas') 
# def minas_to_talents(request, minas):
#     talents, remaining_minas = minas // 60, minas % 60
#     return HttpResponse(f"{minas} minas = {talents} talents and {remaining_minas} minas") 
#return HttpResponse(str(talents) + ' talents and ' + str(remaining_minas) + ' minas

# 42.In the days of the Roman Republic, there were 9 coin denominations in common
# circulation, including the denarius and the quadrans. A denarius was worth 40
# quadrans. This changed to 64 quadrans in the early days of the Roman Empire.
# Using Django, create a quadrans to denarius converter for the Republic and Early
# Empire days. Modify urls.py and views.py so that, for example, http://
# 127.0.0.1:8000/converter/republic_quadrans/123 displays 3 denarii and 3 quadrans
# and http://127.0.0.1:8000/converter/early_empire_quadrans/123 displays 1 denarius
# and 59 quadrans
# Note that the plural of denarius is denarii

# denarius = 40 quadrans in Roman
# denarius = 64 quadrans in early
# in urls.py:

#     path('', view.index, name = 'index'),
#     path('converter/republic_quadrans/<int:quadrans>/', view.Roman, name="roman"),
#     path('converter/early_empire_quadrans/<int:quadrans>/', view.early, name="early")

# in view.py:
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse('Supported conversions:early_empire_quadrans,republic_quadrans')

# def early(request, quadrans):
#     denarii = quadrans // 64 
#      remaining_quadrans = quadrans % 40
#     return HttpResponse(str(denari) + ('i ' if denari != 1 else 'us ') + ' and ' +  str(remaining_quadrans) + ' remaing quadrans ')

# def Roman(request, quadrans):
#     denarius = quadrans // 40 
#     remaining_quadrans = quadrans % 40
#     return HttpResponse(f' denarius = {denarius} remaining quadrans = {remaining_quadrans}')
# 43.Write a Django app so that http://localhost:8000/furryfriends/ratings/n returns all the
# furry friends that have a fluffiness of n or higher, e.g., http://localhost:8000/
# furryfriends/ratings/3 prints out all furry friends who have a fluffiness rating of 3 or
# higher, nicely tabulated in HTML. Note that fluffiness must be in range [0, 5].


# in models.py:

# from django.db import models
# from django.core.exceptions import ValidationError

# MAX_FLUFFINESS = 5

# def validate_fluff_range(value):
#     if value < 0 or value > MAX_FLUFFINESS:
#         raise ValidationError('Out of range', code='fluffiness_value')


# class FurryFriend(models.Model):
#     nickname = models.CharField(max_length=30)
#     fluffiness = models.IntegerField(validators=[validate_fluffiness_range])

# def __str__(self):
#     stars = ''.join('*' for _ in range(self.fluffiness))
#     return self.nickname + ': ' + stars



# urls.py:

# from django.urls import path
# from . import views
# urlpaoerns = [
#     path('', views.index, name='index'),
#     path('create/', views.FurryFriendCreator.as_view(), name='creaFon'),
#     path('rarings/<int:fluffiness>', views.raFngs, name='raFngs'),
# ]

# #frind.html

# # friend_list.html
# <!DOCTYPE html>
# <html lang="en">
#     <head>
#         <tile>Friends</title>
#     </head>
#     <body>
#     {% if friend_list %}
#         <table>
#             <tr><th>nickname</th> <th>Fluffiness</th></tr>
#             {% for friend in friend_list %}
#             <tr><td>{{friend.nickname}}</td><td>{{friend.fluffiness}}</td></tr>
#             {% endfor %}
#         </table>
#     {%else%}
#         <p>No furry friend</p>
#     {% endif %}
#         </table>
#     </body>
# </html>

# nickname	Fluffiness
# Mittens	5
# Fluffy	7


# #views.py
# from django.shortcuts import render #html
# from django.urls import reverse_lazy #get url of view lazy because uses it beofre url ocnfgi
# from django.views.generic.edit import CreateView #class based view for creating model instance
# from .models import FurryFriend

# def index(request):
#     lst = FurryFriend.objects.all()
#     context = {"friend_list": lst}
#     return render(request,'furryfriends/friend_list.html', context)

# def ratings(request,fluffiness):
#     lst = FurryFriend.objects.filter(fluffiness__gte=fluffiness)
#     #filter greater or equal 
#     context = {"friend_list": lst}
#     return render(request, 'furryfriends/friend_list.html', context)

# class FurryFriendCreater(CreateView):
#     model = FurryFriend #view to work with model
#     fields = '__all__' #include all model fileds
#     success_url = reverse_lazy('index') #after successfull submission redirect tp index paeg

# # 44.Update tests.py so that ratings in views.py is properly tested

# from django.test import TestCase
# from .models import FurryFriend

# class FurryFriendTestCase(TestCase):
#     def test_create(self):
#     response = self.client.post("/furryfriends/create/", {'nickname': 'Fluffy the Cat', 'fluffiness':5})
#     f = FurryFriend.objects.get(nickname='Fluffy the Cat')
#     self.assertEqual(f.fluffiness, 5)

#     def test_raFngs(self):
#     response = self.client.post("/furryfriends/create/", {'nickname': 'Fluffy the Cat', 'fluffiness':5})
#     response = self.client.post("/furryfriends/create/", {'nickname': 'Gruffy the Dog', 'fluffiness':1})
#     response = self.client.post("/furryfriends/create/", {'nickname': 'Sonic the Hedgehog','fluffiness': 0})
#     response = self.client.get("/furryfriends/raFngs/0")
#     self.assertTrue('Fluffy the Cat' in response._container[0].decode())
#     self.assertTrue('Gruffy the Dog' in response._container[0].decode())
#     self.assertTrue('Sonic the Hedgehog' in response._container[0].decode())
#     response = self.client.get("/furryfriends/raFngs/1")
#     self.assertTrue('Fluffy the Cat' in response._container[0].decode())
#     self.assertTrue('Gruffy the Dog' in response._container[0].decode())
#     self.assertTrue('Sonic the Hedgehog' not in response._container[0].decode())
#     response = self.client.get("/furryfriends/raFngs/5")
#     self.assertTrue('Fluffy the Cat' in response._container[0].decode())
#     self.assertTrue('Gruffy the Dog' not in response._container[0].decode())
#     self.assertTrue('Sonic the Hedgehog' not in response._container[0].decode())




# # 45.Write a Django app so that http://localhost:8000/inventory/count/n returns all the
# # items that have a count of n or higher, e.g., http://localhost:8000/inventory/count/3
# # prints out all items that have a count of 3 or higher, nicely tabulated in HTML. Note
# # that count must be in range [0, 50].



# # 46.Update tests.py so that stock in views.py is properly tested
# # 47.Write a Django app so that http://localhost:8000/menu/spiciness/n returns all the
# # items that have a spiciness of n or higher, e.g., http://localhost:8000/menu/
# # spiciness/2 prints out all items that have a spiciness of 2 or higher, nicely tabulated
# # in HTML. Note that spiciness must be in range [0, 3].




# # 48.Update tests.py so that spiciness in views.py is properly tested
# # 50