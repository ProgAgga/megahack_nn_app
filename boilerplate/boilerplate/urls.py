from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

from boilerplate.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
]

urlpatterns.extend([
    path('api/offers', OfferListView.as_view()),
   # path('api/options', ),
   # path('api/sources', ),
    path('api/dealers', DealerListView.as_view()),
    path('api/clients', ClientsListView.as_view()),
    path('api/clients/<int:id>', ClientDetailView.as_view()),
   # path('api/orders', ),
   # path('api/check_offer', )
])

urlpatterns.append(re_path('.*', TemplateView.as_view(template_name='index.html')))
