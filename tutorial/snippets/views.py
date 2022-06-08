from snippets.model import Snippet
from snippet.serializer import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
# Create your views here.
#adding format=None because no hardwired type of content and add support for format suffixes to our API endpoints
#class based view
class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

