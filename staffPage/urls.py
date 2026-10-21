from django.urls import path
from . import views

urlpatterns = [
    path("",views.staffView,name="staff_view"),
    path("zakupki/",views.staffZakupki,name="staff_zakupki"),
    path("editor/",views.staffEditor,name="staff_editor"),
    path("editorCompl/<int:pk>",views.staffEditorCompl,name="staff_editor_compl")
]