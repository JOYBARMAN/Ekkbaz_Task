"""Views for business"""
from django.db.models import ExpressionWrapper, F, FloatField
from django.db.models.functions import Cast
from django.http import JsonResponse

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from core.permissions import (
    IsAuthenticated,
    IsBusinessOwnerOrReadOnly,
    IsActivatedUser,
    SAFE_METHODS,
)
from business.models import Business
from business.rest.serializers.business import BusinessListSerializer

from geopy.distance import geodesic


class BusinessList(ListCreateAPIView):
    """Views to get or create business instance"""

    serializer_class = BusinessListSerializer
    permission_classes = [
        IsAuthenticated,
        # IsActivatedUser,
    ]
    queryset = Business().get_all_actives().select_related("user").all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={"user": self.request.user},
        )
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()

        return Response(response_data, status=status.HTTP_200_OK)


class BusinessDetail(RetrieveUpdateAPIView):
    """View to retrieve or update a business instance."""

    serializer_class = BusinessListSerializer
    queryset = BusinessList().queryset
    lookup_field = "uid"

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [
                IsAuthenticated(),
                # IsActivatedUser(),
            ]
        else:
            return [
                IsBusinessOwnerOrReadOnly(),
                # IsActivatedUser(),
            ]


class BusinessesWithinRadiusView(APIView):
    """Views for get business instance within radius 20000 km"""

    permission_classes = [
        IsAuthenticated,
        # IsActivatedUser,
    ]

    def get(self, request):
        latitude = request.query_params.get("latitude")
        longitude = request.query_params.get("longitude")
        radius = 2000  # 2000 km radius

        if latitude and longitude:
            user_location = (latitude, longitude)
            businesses = Business().get_all_actives()
            filtered_businesses = []

            for business in businesses:
                business_location = (business.latitude, business.longitude)
                distance = geodesic(user_location, business_location).km
                if distance <= radius:
                    filtered_businesses.append(business)

            serializer = BusinessListSerializer(filtered_businesses, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Latitude and longitude required"}, status=400)
