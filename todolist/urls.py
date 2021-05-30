from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="ind"),
    path('add',views.add_item,name="add"),
    path('completed/<td_id>',views.completed_todo,name="com"),
    path('del_completed',views.del_com,name="d_c"),
    path('del_all',views.del_all,name="d_a")
]
