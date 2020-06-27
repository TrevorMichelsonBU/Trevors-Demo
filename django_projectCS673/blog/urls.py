from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDetailView, PostDeleteView, UserPostListView
from .views import MenuCreateView, MenuDetailView
#urls.py call functions withing .views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #Empty path will be homepage, views.home is a function that will be called and 
    										#sent to our views.py file
    										#the name will be used for reference in base.html for links
   	path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
   	#<pk> is primary key, int forces it to be a #
   	path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
   	path('post/new', PostCreateView.as_view(), name='post-create'),
   	path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'),
   	path('post/<int:pk>/delete', PostDeleteView.as_view(),name='post-delete'),
   	path('about/', views.about, name='blog-about'),

    #menus
    path('menu/new', MenuCreateView.as_view() ,name = 'menu-create'),
    path('menu/<str:pk>/', MenuDetailView.as_view(), name = 'menu-detail'),
]

