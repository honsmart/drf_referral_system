from rest_framework import serializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rs.models import ReferralsHistory
from .serializers import ReferralsHistorySerializer


class ReferralHistoryView(ListAPIView):
    serializer_class = ReferralsHistorySerializer

    def get_queryset(self):
        reffered_by = self.kwargs['reffered_by']
        return ReferralsHistory.objects.filter(reffered_by=reffered_by)


