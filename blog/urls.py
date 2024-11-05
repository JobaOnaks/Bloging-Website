from django.urls import path
from .views import HomePageView,BlogListview,MyBlogListView,BlogDetailView,BlogUpdateView,BlogCreateView,BlogDeleteView

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('readblog/', BlogListview.as_view(), name='readblog'),
    path('<uuid:pk>/', BlogDetailView.as_view(), name='readblogdetails'),
    path('myblog/', MyBlogListView.as_view(), name='myblog'),
    path('<uuid:pk>/editblog/', BlogUpdateView.as_view(), name='update'),
    path('createblog/', BlogCreateView.as_view(), name='create'),
    path('<uuid:pk>/deleteblog/', BlogDeleteView.as_view(), name= 'delete'),
]