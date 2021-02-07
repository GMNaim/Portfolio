from django.urls import path, include

urlpatterns = [
    path('api/', include('my_portfolio.api.urls')),
]
