from django.urls import path,include

from inapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('details/<int:id>/',views.Detail,name='details'),
    path('add/',views.add_product,name="add"),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
    ]