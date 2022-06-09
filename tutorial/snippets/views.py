from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
# Create your views here.
#adding format=None because no hardwired type of content and add support for format suffixes to our API endpoints
#class based view
class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

