from django.urls import include, path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

import userauth.views

urlpatterns = [
    path('login/', auth_views.login,
            {'template_name': 'userauth/login.html'}, name='userauth_login'),
    path('logout/', auth_views.logout, {
            'next_page': reverse_lazy('recipes_recipe_index'),
            },
            name='userauth_logout'),
    path('password-change/', auth_views.password_change,
            {
                'template_name': 'userauth/password_change_form.html',
                'post_change_redirect': 'userauth_password_change_done',
            },
        name='userauth_password_change'),
    path('password-change-done/', auth_views.password_change_done,
            {'template_name': 'userauth/password_change_done.html'},
            name='userauth_password_change_done'),
    path('register/', userauth.views.register,
            {'next_page_name': 'userauth_register_done'},
            name='userauth_register'),
    path('welcome/',
            TemplateView.as_view(template_name='userauth/register_done.html'),
            name='userauth_register_done'),            
]