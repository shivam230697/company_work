from django.urls import path

from . import views
from .views import user_login, user_logout, user_signup

urlpatterns = [
    path('', views.base, name="base"),
    path('index/', views.index, name="index"),
    path('raw_material/', views.raw_material, name="raw_material"),
    path('raw_material_details/', views.raw_material_view, name="raw_material_view"),
    path('raw_material_update/<int:pk>', views.raw_material_update, name="rm_update"),
    path('confirm/<int:pk>', views.confirm, name="confirm"),
    path('delete_rm/<int:pk>', views.delete_raw_material_entry, name="delete_rm_entry"),
    path('add_production/', views.add_production, name="add_production"),
    path('view_productions/', views.view_production, name="view_production"),
    path('edit_production/<int:pk>', views.edit_production, name="edit_production"),
    path('update_production/<int:pk>', views.update_production, name="update_production"),
    path('delete_production/<int:pk>', views.delete_production, name="delete_production"),
    path('dashboard_page/', views.dashboard, name="dashboard"),
    path('view_final_goods/', views.view_final_goods, name="view_final_goods"),
    path('add_final_goods/', views.add_final_good, name="add_final_goods"),

    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', user_signup, name='signup'),

]
