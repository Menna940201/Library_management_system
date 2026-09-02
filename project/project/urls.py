"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from loans.views import borrow_book, return_book, my_loans
from accounts.views import signup_view, login_view, logout_view
from catalog.views import book_list
from catalog.views import about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return/<int:loan_id>/', return_book, name='return_book'),
    path('my-loans/', my_loans, name='my_loans'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('books/', book_list, name='book_list'),
    path('about-us/', about_us, name='about_us'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)