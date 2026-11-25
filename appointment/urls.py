
from django.urls import path
from . import views

urlpatterns = [

    # ================= LOGIN AND LOGOUT =================

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    # ================= HOME =================

    path('app_home/', views.home, name='app_home'),

    # ================= ABOUT =================

    path('about/', views.about, name='about'),

    # ================= DOCTOR =================

    path('doctor/', views.doctor_show, name='doctor'),
    path('doctor/show/', views.doctor_show, name='doctor_show'),
    path('doctor/insert/', views.doctor_insert, name='doctor_insert'),
    path('doctor/update/<int:did>/', views.doctor_update, name='doctor_update'),
    path('doctor/delete/<int:did>/', views.doctor_delete, name='doctor_delete'),

    # ================= APPOINTMENT =================

    path('appointment/', views.appointment_show, name='appointment'),
    path('appointment/show/', views.appointment_show, name='appointment_show'),
    path('appointment/insert/', views.appointment_insert, name='appointment_insert'),
    path('appointment/update/<int:aid>/', views.appointment_update, name='appointment_update'),
    path('appointment/delete/<int:aid>/', views.appointment_delete, name='appointment_delete'),

    # ================= PATIENT =================

    path('patient/', views.patient_show, name='patient'),
    path('patient/show/', views.patient_show, name='patient_show'),
    path('patient/insert/', views.patient_insert, name='patient_insert'),
    path('patient/update/<int:pid>/', views.patient_update, name='patient_update'),
    path('patient/delete/<int:pid>/', views.patient_delete, name='patient_delete'),

]
