from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers.brand import *
from api.permissions import ReadOnly
from shop.models.brand import Brand


class BrandViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = Brand.objects.all()
    permission_classes = [IsAdminUser|ReadOnly]

    def get_serializer_class(self):
        """Return appropriate serializer class."""
        if self.action == 'upload_logo':
            return BrandBrandingLogoSerializer
        return BrandSerializer

    # Make this work for to upload from url also.
    # https://www.trell.se/blog/file-uploads-json-apis-django-rest-framework/
    @action(
        detail=True,
        methods=['POST',],
        url_path='upload-logo',
        parser_classes=[MultiPartParser],
    )
    def upload_logo(self, request, pk):
        obj = self.get_object()
        serializer = self.get_serializer(obj.branding, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )
