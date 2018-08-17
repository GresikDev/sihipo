from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    url(r'^setting/$', views.SettingView.as_view(), name='setting'),
    url(r'^plantplant/$', views.PlantPlantList.as_view(), name='plantplant_list'),
    url(r'^plantplant/create$', views.PlantPlantCreate.as_view(), name='plantplant_create'),
    url(r'^plantplant/update/(?P<pk>\d+)$', views.PlantPlantUpdate.as_view(), name='plantplant_update'),
    url(r'^plantplant/delete/(?P<pk>\d+)$', views.PlantPlantDelete.as_view(), name='plantplant_delete'),
    url(r'^plantopt/$', views.PlantOptList.as_view(), name='plantopt_list'),
    url(r'^plantopt/create$', views.PlantOptCreate.as_view(), name='plantopt_create'),
    url(r'^plantopt/update/(?P<pk>\d+)$', views.PlantOptUpdate.as_view(), name='plantopt_update'),
    url(r'^plantopt/delete/(?P<pk>\d+)$', views.PlantOptDelete.as_view(), name='plantopt_delete'),
    url(r'^plantoptdetail/$', views.PlantOptDetailList.as_view(), name='plantoptdetail_list'),
    url(r'^plantoptdetail/create/$', views.PlantOptDetailCreate.as_view(), name='plantoptdetail_create'),
    url(r'^plantoptdetail/update/(?P<pk>\d+)$', views.PlantOptDetailUpdate.as_view(), name='plantoptdetail_update'),
    url(r'^plantoptdetail/delete/(?P<pk>\d+)$', views.PlantOptDetailDelete.as_view(), name='plantoptdetail_delete'),
    url(r'^plantsensor/$', views.PlantSensorList.as_view(), name='plantsensor_list'),
    url(r'^plantsensor/create/$', views.PlantSensorCreate.as_view(), name='plantsensor_create'),
    url(r'^plantsensor/update/(?P<pk>\d+)$', views.PlantSensorUpdate.as_view(), name='plantsensor_update'),
    url(r'^plantsensor/delete/(?P<pk>\d+)$', views.PlantSensorDelete.as_view(), name='plantsensor_delete'),
    url(r'^plantsensor/dashboard/$', views.PlantSensorDashboard.as_view(), name='plantsensor_dashboard'),
    url(r'^plantsensordetail/$', views.PlantSensorDetailList.as_view(), name='plantsensordetail_list'),
    url(r'^plantsensordetail/create/$', views.PlantSensorDetailCreate.as_view(), name='plantsensordetail_create'),
    url(r'^plantsensordetail/update/(?P<pk>\d+)$', views.PlantSensorDetailUpdate.as_view(), name='plantsensordetail_update'),
    url(r'^plantsensordetail/delete/(?P<pk>\d+)$', views.PlantSensorDetailDelete.as_view(), name='plantsensordetail_delete'),
    url(r'^plantcontrol/$', views.PlantControlList.as_view(), name='plantcontrol_list'),
    url(r'^plantcontrol/create/$', views.PlantControlCreate.as_view(), name='plantcontrol_create'),
    url(r'^plantcontrol/update/(?P<pk>\d+)$', views.PlantControlUpdate.as_view(), name='plantcontrol_update'),
    url(r'^plantcontrol/delete/(?P<pk>\d+)$', views.PlantControlDelete.as_view(), name='plantcontrol_delete'),
    url(r'^plantcontrol/dashboard/$', views.PlantControlDashboard.as_view(), name='plantcontrol_dashboard'),
    url(r'^plantcontroldetail/$', views.PlantControlDetailList.as_view(), name='plantcontroldetail_list'),
    url(r'^plantcontroldetail/create/$', views.PlantControlDetailCreate.as_view(), name='plantcontroldetail_create'),
    url(r'^plantcontroldetail/update/(?P<pk>\d+)$', views.PlantControlDetailUpdate.as_view(), name='plantcontroldetail_update'),
    url(r'^plantcontroldetail/delete/(?P<pk>\d+)$', views.PlantControlDetailDelete.as_view(), name='plantcontroldetail_delete'),
    url(r'^plantrack/$', views.PlantRackList.as_view(), name='plantrack_list'),
    url(r'^plantrack/create/$', views.PlantRackCreate.as_view(), name='plantrack_create'),
    url(r'^plantrack/update/(?P<pk>\d+)$', views.PlantRackUpdate.as_view(), name='plantrack_update'),
    url(r'^plantrack/delete/(?P<pk>\d+)$', views.PlantRackDelete.as_view(), name='plantrack_delete'),
    url(r'^plantrackpoint/$', views.PlantRackPointList.as_view(), name='plantrackpoint_list'),
    url(r'^plantrackpoint/create/$', views.PlantRackPointCreate.as_view(), name='plantrackpoint_create'),
    url(r'^plantrackpoint/update/(?P<pk>\d+)$', views.PlantRackPointUpdate.as_view(), name='plantrackpoint_update'),
    url(r'^plantrackpoint/delete/(?P<pk>\d+)$', views.PlantRackPointDelete.as_view(), name='plantrackpoint_delete'),
    url(r'^plantsensorlog/$', views.PlantSensorLogList.as_view(), name='plantsensorlog_list'),
    url(r'^plantsensorlog/create/$', views.PlantSensorLogCreate.as_view(), name='plantsensorlog_create'),
    url(r'^plantsensorlog/update/(?P<pk>\d+)$', views.PlantSensorLogUpdate.as_view(), name='plantsensorlog_update'),
    url(r'^plantsensorlog/delete/(?P<pk>\d+)$', views.PlantSensorLogDelete.as_view(), name='plantsensorlog_delete'),
    url(r'^plantsensorlogdetail/$', views.PlantSensorLogDetailList.as_view(), name='plantsensorlogdetail_list'),
    url(r'^plantsensorlogdetail/create/$', views.PlantSensorLogDetailCreate.as_view(), name='plantsensorlogdetail_create'),
    url(r'^plantsensorlogdetail/update/(?P<pk>\d+)$', views.PlantSensorLogDetailUpdate.as_view(), name='plantsensorlogdetail_update'),
    url(r'^plantsensorlogdetail/delete/(?P<pk>\d+)$', views.PlantSensorLogDetailDelete.as_view(), name='plantsensorlogdetail_delete'),
    url(r'^plantcontrollog/$', views.PlantControlLogList.as_view(), name='plantcontrollog_list'),
    url(r'^plantcontrollog/create/$', views.PlantControlLogCreate.as_view(), name='plantcontrollog_create'),
    url(r'^plantcontrollog/update/(?P<pk>\d+)$', views.PlantControlLogUpdate.as_view(), name='plantcontrollog_update'),
    url(r'^plantcontrollog/delete/(?P<pk>\d+)$', views.PlantControlLogDelete.as_view(), name='plantcontrollog_delete'),
    url(r'^plantcontrollogdetail/$', views.PlantControlLogDetailList.as_view(), name='plantcontrollogdetail_list'),
    url(r'^plantcontrollogdetail/create/$', views.PlantControlLogDetailCreate.as_view(), name='plantcontrollogdetail_create'),
    url(r'^plantcontrollogdetail/update/(?P<pk>\d+)$', views.PlantControlLogDetailUpdate.as_view(), name='plantcontrollogdetail_update'),
    url(r'^plantcontrollogdetail/delete/(?P<pk>\d+)$', views.PlantControlLogDetailDelete.as_view(), name='plantcontrollogdetail_delete'),
    url(r'^plantevalif/$', views.PlantEvalIfList.as_view(), name='plantevalif_list'),
    url(r'^plantevalif/create/$', views.PlantEvalIfCreate.as_view(), name='plantevalif_create'),
    url(r'^plantevalif/update/(?P<pk>\d+)$', views.PlantEvalIfUpdate.as_view(), name='plantevalif_update'),
    url(r'^plantevalif/delete/(?P<pk>\d+)$', views.PlantEvalIfDelete.as_view(), name='plantevalif_delete'),
    url(r'^plantevalthen/$', views.PlantEvalThenList.as_view(), name='plantevalthen_list'),
    url(r'^plantevalthen/create/$', views.PlantEvalThenCreate.as_view(), name='plantevalthen_create'),
    url(r'^plantevalthen/update/(?P<pk>\d+)$', views.PlantEvalThenUpdate.as_view(), name='plantevalthen_update'),
    url(r'^plantevalthen/delete/(?P<pk>\d+)$', views.PlantEvalThenDelete.as_view(), name='plantevalthen_delete'),
    url(r'^planteval/$', views.PlantEvalList.as_view(), name='planteval_list'),
    url(r'^planteval/create/$', views.PlantEvalCreate.as_view(), name='planteval_create'),
    url(r'^planteval/update/(?P<pk>\d+)$', views.PlantEvalUpdate.as_view(), name='planteval_update'),
    url(r'^planteval/delete/(?P<pk>\d+)$', views.PlantEvalDelete.as_view(), name='planteval_delete'),
    url(r'^plantevallog/$', views.PlantEvalLogList.as_view(), name='plantevallog_list'),
    url(r'^plantevallog/create/$', views.PlantEvalLogCreate.as_view(), name='plantevallog_create'),
    url(r'^plantevallog/update/(?P<pk>\d+)$', views.PlantEvalLogUpdate.as_view(), name='plantevallog_update'),
    url(r'^plantevallog/delete/(?P<pk>\d+)$', views.PlantEvalLogDelete.as_view(), name='plantevallog_delete'),
    url(r'^plantalert/$', views.PlantAlertList.as_view(), name='plantalert_list'),
    url(r'^plantalert/create$', views.PlantAlertCreate.as_view(), name='plantalert_create'),
    url(r'^plantalert/update/(?P<pk>\d+)$', views.PlantAlertUpdate.as_view(), name='plantalert_update'),
    url(r'^plantalert/delete/(?P<pk>\d+)$', views.PlantAlertDelete.as_view(), name='plantalert_delete'),
    url(r'^plantalert/simple/$', views.PlantAlertSimple, name='plantalert_simple'),
    url(r'^plantalert/count/$', views.PlantAlertCount, name='plantalert_count'),
    url(r'^plantalert/de/$', views.PlantAlertDe, name='plantalert_de'),
    url(r'^plantalert/de/(?P<pk>\d+)$', views.PlantAlertDe, name='plantalert_de'),
]