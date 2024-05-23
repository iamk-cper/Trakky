from django.urls import path
from user.views import (api_update_userprofile_view, api_detail_userprofile_view, api_is_product_manager_view)

app_name = 'user'

urlpatterns = [
    path('userprofile/', api_detail_userprofile_view, name='userprofile_detail'),
    path('userprofile/update/', api_update_userprofile_view, name='userprofile_update'),
    path('is_product_manager/', api_is_product_manager_view)
]