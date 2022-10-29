from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from crud import views

urlpatterns = [
    path('', views.auth_reg),
    path('auth_login/', views.auth_login),
    path('logIn_page/', views.logInPage),
    path('auth_logout/', views.auth_logout),
    path('create_account/', views.creataAccount),

    path('setfile/', views.set_File),
    path('viewFile/', views.viewFile),
    path('update_files/<id>/', views.update_files),
    path('delete/setFile/<id>/', views.delete_files),

    path('single_setfile/', views.view_singleFile),
    path('upload_single_file/', views.saveSingleImg),
    path('modi_single_file/', views.modiSingleImg),
    path('update/updateSingleImg/<id>/', views.updateSingleImg),
    path('delete/singleFileDel/<id>/', views.delete_single_files),

    path('settext/', views.setText),
    path('viewText/', views.viewText),
    path('editSetText/<id>', views.update),
    path('deleteSetText/<id>', views.delete),
]
