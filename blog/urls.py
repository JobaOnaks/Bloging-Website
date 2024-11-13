from django.urls import path
from .views import HomePageView,BlogListview,MyBlogListView,BlogDetailView,BlogUpdateView,BlogCreateView,BlogDeleteView,CommentCreateView,CategoryView

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('readblog/', BlogListview.as_view(), name='readblog'),
    path('<uuid:pk>/', BlogDetailView.as_view(), name='readblogdetails'),
    path('myblog/', MyBlogListView.as_view(), name='myblog'),
    path('editblog/<uuid:pk>/', BlogUpdateView.as_view(), name='update'),
    path('createblog/', BlogCreateView.as_view(), name='create'),
    path('deleteblog/<uuid:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('add_comment/<uuid:pk>/', CommentCreateView.as_view(), name='add_comment'),
]