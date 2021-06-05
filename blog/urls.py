from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('',views.HomeView.as_view(),name='home')
    ,path('blog/',views.CreateListView.as_view(),name='blog')
    ,path('about/',views.SkillListView.as_view(),name='about')
    ,path('blog/<int:pk>/',views.ArticleDetailView.as_view(), name='article')
    ,path('contact/', views.ContactFormView.as_view(), name='contact')
    ,path('contact/', views.ContactListView.as_view(), name='contact')
    ,path('portfolio/',views.PortfolioListView.as_view(),name='portfolio')
    ,path('portfolio/', views.PortfolistDettailView.as_view(),name='portfolio')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    '''
    ,path('portfolio/',views.MyartListView.as_view(),name='portfolio')
    ,path('portfolio/',views.LogoartListView.as_view(),name='portfolio')
    ,path('portfolio/',views.VideoartListView.as_view(),name='portfolio')
    ,path('portfolio/',views.WebdesignListView.as_view(),name='portfolio')
    '''
