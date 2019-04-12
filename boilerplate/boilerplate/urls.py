from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
]

urlpatterns.extend([
    path('api/offers', ),
    path('api/options', ),
    path('api/sources', ),
    path('api/dealers', ),
    path('api/clients', )
])
