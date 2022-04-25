from django.urls import path
from .views import home, form_set, get_form,delete_record,update_record,save_record

urlpatterns = [
    path("", home),
    path("set_form/", form_set),
    path("get_form/", get_form),
    path("get_form/", get_form),
    path("delete_record/", delete_record),
    path("update_record/", update_record),
    path("save_record/", save_record),
]
