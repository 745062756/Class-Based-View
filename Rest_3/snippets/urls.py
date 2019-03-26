from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import view_three

urlpatterns = [
    path('snippets/', view_three.Snippetlist.as_view()),
    path('snippets/<int:pk>/', view_three.Snippetdetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)