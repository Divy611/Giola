from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('<int:video_id>/video/', watch_video, name='watch_video'),
    path('video/add_comment/', add_comment, name='add_comment'),
    path('video/add_like/<int:video_id>/', add_like, name='add_like'),
    path('<str:session_username>/profile/', profile, name='profile'),
    path('<str:session_username>/dashboard/', dashboard, name='dashboard'),
    path('add_subscriber/<viewer>/', add_sub, name='add_subscriber'),
    path('upload/', upload_video, name='upload'),
    path("trending/",trending, name="trending"),
    path("category1/",category1, name="category1"),
    path("settings",settings, name="settings"),
    path("my_subscriptions/",subscriptions, name="subscriptions"),
    path("category2/",category2, name="category2"),
    path("category3/",category3, name="category3"),
    path("category4/",category4, name="category4"),
    path("category5/",category5, name="category5"),
    path("<str:session_username>/creator_profile/",creatorprof, name="creator_profile"),
    path("help_and_faqs/",helpnfaqs, name="helpndfaqs"),
    path("privacy_policy/",privacypolicy, name="privacypolicy"),
    path("terms_and_conditions/",termsnconditions, name="termsnconditions"),
    path('edit_video/<int:video_id>', edit_video, name='edit_video'),
    path('delete_video/', delete_video, name='delete_video'),
    path('update_details/', update_details, name='update_details'),
    path('wallet/',wallet,name='wallet'),
    path('signup/', signup, name='signup'),
    path('library/', library, name='library'),
    path('login/', user_login, name='login'),
    path('payments/',paymentpage,name='payments'),
    path('loginpg/', loginpg, name='loginpg'),
    path('logout/', user_logout, name='logout'),
    path('pricing/',plansnpricing,name='plansnpricing'),
    path('search/', search, name='search'),
]