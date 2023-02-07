from rest_framework import serializers
from rs.models import Users, ReferralsHistory


class UserSerializers(serializers.ModelSerializer):
     first_name = serializers.CharField(max_length=30, min_length=2)
     last_name = serializers.CharField(max_length=30, min_length=2)
     user_name = serializers.CharField(max_length=30, min_length=8)
     reffered_by = serializers.CharField(max_length=30, min_length=0)
     email = serializers.EmailField(max_length=255, min_length=3)
     password = serializers.CharField(max_length=30, min_length=8)

     class Meta:
          model = Users
          fields = '__all__'

     def validate(self, attrs):
         email = attrs.get("email", "")
         reffered_by = attrs.get("reffered_by", "")
         user_name = attrs.get("user_name", "")


         email_exist = Users.objects.filter(email=email).exists()
         referral_id_exist = Users.objects.filter(refferal_ID=reffered_by).exists()
         user_exist = Users.objects.filter(user_name=user_name).exists()


         if email_exist:
              raise serializers.ValidationError({'email': ('Email already exist')})
         
         if user_exist:
              raise serializers.ValidationError({'user_name': ('Username already exist')})
         
         if reffered_by:
           if not referral_id_exist:
              raise serializers.ValidationError({"reffered_by": ('Referral Id does not exist')})
         
         return super().validate(attrs)
    
     def create(self, validated_data):
          user = Users.objects.create(**validated_data)
          if user:
               ref_profile = Users.objects.filter(refferal_ID= user.reffered_by).first()
               if ref_profile:
                         ref_profile.total_reffered += 1
                         ref_profile.referal_balance += 500
                         ref_profile.total_referral_bonus_earned += 500
                         ref_profile.save()
                         referral_history = ReferralsHistory.objects.create(user=user,reffered_by=user.reffered_by, amount=500, status="rewarded")      
          return user
         

class UserProfileSerilizer(serializers.ModelSerializer):
         class Meta:
              model = Users
              fields = '__all__'

         
              
         

      
