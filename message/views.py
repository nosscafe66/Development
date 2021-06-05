from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):#インデックス
    template_name = "index.html"

    def get_context_data(self):
      ctxt = super().get_context_data()
      ctxt["username"] = "yuto"
      return ctxt

class AboutView(TemplateView):#自己紹介(Skillset)
    template_name = "about.html"

    def get_context_data(self):
      ctxt = super().get_context_data()
      ctxt["num_services"] = 5
      ctxt["Skills"] = [
        "python"
        ,"Go"
        ,"Django"
        ,"HTML&CSS"
      ]
      return ctxt
'''
class SidebarView(TemplateView):#サイドバーメニュ一覧
    template_name = "sidebar.html"

    def get_context_data(self):
      side_bar = super().get_context_data()
      side_bar["side_bar"] = [
        "Top"
        ,"Portfolio"
        ,"Contact"
        ,"Category"
        ,"Access"
      ]
      return ctxt
'''
class MainView(TemplateView):
    pass

class BlogView(TemplateView):#記事一覧
    template_name = "blog.html"

    def get_context_data(self):
      ctxt = super().get_context_data()
      return ctxt