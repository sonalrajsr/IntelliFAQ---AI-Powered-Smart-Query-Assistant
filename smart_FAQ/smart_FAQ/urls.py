from django.contrib import admin
from django.urls import path
from faq.views import ask_question, home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ask/', ask_question, name='ask_question'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
