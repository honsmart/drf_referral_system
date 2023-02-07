from rest_framework.serializers import ModelSerializer
from rs.models import ReferralsHistory
 

class ReferralsHistorySerializer(ModelSerializer):
    class Meta:
        model = ReferralsHistory
        fields = '__all__'
