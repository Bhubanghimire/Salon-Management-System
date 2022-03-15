from django.urls import path, include
from .views import CreateAppointment,CancelAppointment,UpdateAppointment,Makepayment,PaymentComplete


urlpatterns = [
    path("new/",CreateAppointment, name="create-new"),
    path("appointment/<uuid:uuid>/cancel/", CancelAppointment, name="cancel-appointment"),
    path('appointment/<uuid:uuid>/update/',UpdateAppointment, name="appointment-update"),
    path("payment/", Makepayment, name="make-payment"),
    path("payment-complete", PaymentComplete, name="payment-complete"),
]