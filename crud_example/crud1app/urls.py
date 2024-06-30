from django.urls import path
from . import views

urlpatterns = [
    path('',views.retrieve_list,name='retrieve_list'),
    path('create/',views.create_view,name='create_view'),
    path('detail/<id>',views.delete_view,name='detail_view'),
    path('detail/edit/<id>',views.update_view,name='update_view'),
    path('delete/<id>',views.delete_view,name='delete_view'),

]