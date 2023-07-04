from django.urls import path
from . import views

urlpatterns = [
    path('load-homepage', views.load_homepage, name='home'),
    path('load-note/<slug:slug>', views.load_note, name='note'),
    path('load-comments/<slug:slug>', views.load_comments, name='comments'),
    path('load-all', views.load_all, name='all'),
    path('load-random', views.load_random, name='random'),
    path('make-comment', views.make_comment, name='make-comment'),
    path('load-category/<str:category>', views.load_category, name='category'),
    # path('double-database', views.double_database),
]