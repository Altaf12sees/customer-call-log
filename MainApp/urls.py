from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('login/update/', views.update_call_view, name="update_call_view"),
    path('add_new_call_log/', views.add_new_call_log, name="add_new_call_log"),
    path('create_product/', views.create_product, name="create_product"),
    path('update_product/', views.update_product, name="update_product"),
    path('delete_product/<int:pk>/', views.delete_product, name="delete_product"),
    path('call_logs/', views.get_call_logs, name="call_logs"),
    path('call_reports/', views.get_call_reports, name="get_call_reports"),
    # path('logout', views.logout_view, name='logout')
]