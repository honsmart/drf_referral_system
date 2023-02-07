# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from . import views


# router = DefaultRouter()
# router.register(r'register', views.users.views.RegisterView, basename="rigister") 

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.users.views.RegisterView.as_view()),
    path('referralhistory/<str:reffered_by>/', views.referrals.views.ReferralHistoryView.as_view()),
    path('profile/<str:user_id>/', views.users.views.UserProfileView.as_view()),


]