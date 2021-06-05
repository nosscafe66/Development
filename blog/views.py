from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm
from .models import (
    Create
    ,About
    ,Home
    ,Portfolio
    ,Contact
    ,Myart
    ,Logoart
    ,Videoart
    ,Webdesign
)

#投稿機能の実装(表示)
class CreateListView(ListView):
    template_name = 'blog/blog.html'
    model = Create
    article_name = 'creates'
    ordering = ['-id']

#スキルセット一覧機能
class SkillListView(ListView):
    template_name = 'about/about.html'
    model = About
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['num'] = 3
        ctxt['skills'] = [
            'Design(設計)'
            ,'Development(開発)'
            ,'Consultation(相談)'
            ,'メンター制度'
        ]
        return ctxt

#homeに記載する内容
class HomeView(TemplateView):
    template_name = 'home/home.html'
    model = Home,Create
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Home.objects.all()[:4]
        return context
    
#コンテンツの内容の表示機能
class ArticleListView(ListView):
    template_name = 'article/article.html'
    model = Create
    article_name = 'articles'
    ordering = ['-id']

#記事詳細ページの表示機能
class ArticleDetailView(DetailView):
    template_name = 'article/article.html'
    model = Create

#コンタクトフォームのページの表示機能
class ContactFormView(FormView):
    template_name = 'contact/contact.html'
    model = Contact
    form_class = ContactForm

#コンタクトフォームの最新投稿機能(ゆくゆくは異なる記事を表示させるようにする。)
class ContactListView(ListView):
    template_name = 'contact/contact.html'
    model = Contact
    contact_name = 'contacts'
    ordering = ['-id']

#ポートフォリオ画面の構築
class PortfolioListView(ListView):
    template_name = 'portfolio/portfolio.html'
    model = Portfolio
    def get_context_data(self,**kwargs):
        context = super(PortfolioListView,self).get_context_data(**kwargs)
        context.update({
            'myarts':Myart.objects.all()[:2]
            ,'logoarts':Logoart.objects.all()[:2]
            ,'videoarts':Videoart.objects.all()[:2]
            ,'webdesignarts':Webdesign.objects.all()[:2]
        })
        #context['_list'] = Portfolio.objects.all()[:4]
        return context


class PortfolistDettailView(DetailView):
    template_name = 'portfolio/portfolio.html'
    model = Portfolio


def get_object(self, queryset=None):
    article = super().get_object()
    if article.is_public or self.request.user.is_authenticated:
        return article
    else:
        raise Http404

#myart
class MyartListView(ListView):
    template_name = 'portfolio/portfolio.html'
    model = Myart
    def get_context_data(self,**kwargs):
        myart_context = super().get_context_data(**kwargs)
        myart_context['object_list'] = Myart.objects.all()[:2]
        return myart_context

#logoart
class LogoartListView(ListView):
    template_name = 'portfolio/portfolio.html'
    model = Logoart
    def get_context_data(self,**kwargs):
        logo_context = super().get_context_data(**kwargs)
        logo_context['logo_list'] = Logoart.objects.all()[:2]
        return logo_context

#videoart
class VideoartListView(ListView):
    template_name = 'portfolio/portfolio.html'
    model = Videoart
    def get_context_data(self,**kwargs):
        video_context = super().get_context_data(**kwargs)
        video_context['video_list'] = Videoart.objects.all()[:2]
        return video_context

#webdesign
class WebdesignListView(ListView):
    template_name = 'portfolio/portfolio.html'
    model = Webdesign
    def get_context_data(self,**kwargs):
        design_context = super().get_context_data(**kwargs)
        design_context['webdesign_list'] = Webdesign.objects.all()[:2]
        return design_context
