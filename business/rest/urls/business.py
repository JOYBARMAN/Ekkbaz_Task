"""Url mapping for busiess"""

from django.urls import path

from business.rest.views.business import (
    BusinessList,
    BusinessDetail,
    BusinessesWithinRadiusView,
)

urlpatterns = [
    path("", BusinessList.as_view(), name="business-list-create"),
    path("/<uuid:uid>", BusinessDetail.as_view(), name="business-details"),
    path(
        "/within-radius",
        BusinessesWithinRadiusView.as_view(),
        name="business-within-radius",
    ),
]
