from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register_user, name="register"),
    path("update_password", views.update_password, name="update_password"),
    path("update_user", views.update_user, name="update_user"),
    path("update_info", views.update_info, name="update_info"),
    path("producto/<int:pk>", views.producto, name="producto"),
    path("catalogo", views.catalogo, name="catalogo"),
    path("categoria/<str:foo>", views.categoria, name="categoria"),
    # API
    path("api/productos", views.producto_list, name="producto_list"),
    path("api/productos/", views.producto_list, name="producto_list"),
    path("api/productos/<int:pk>", views.producto_json, name="producto_json"),


]
