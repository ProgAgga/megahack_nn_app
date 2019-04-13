from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

from boilerplate.detailed_views import *
from boilerplate.list_views import *
from boilerplate.views import  *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path(r'.*', TemplateView.as_view(template_name='index.html'))
    
]

urlpatterns.extend([
    path('api/sources', SourcesListView.as_view()),
    path('api/sources/<int:id>', SourceDetailView.as_view()),
    path('api/clients', ClientsListView.as_view()),
    path('api/clients/<int:id>', ClientDetailView.as_view()),
    path('api/dealers', DealersListView.as_view()),
    path('api/dealers/<int:id>', DealerDetailView.as_view()),
    path('api/offers/<int:id>', OfferDetailView.as_view()),
    path('api/offers', OffersListView.as_view()),
    path('api/orders', OffersOrdersListView.as_view()),
    path('api/orders/<int:id>', OfferOrderDetailView.as_view()),
    path('api/options', OptionsListView.as_view()),
    path('api/options/<int:id>', OptionsDetailView.as_view()),
])

urlpatterns.extend([
    path('api/check-offer', CheckOffer.as_view())
])

urlpatterns.append(re_path('.*', TemplateView.as_view(template_name='index.html')))
