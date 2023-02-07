from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import UserSerializers, UserProfileSerilizer
from rest_framework import viewsets
from rs.models import Users



class RegisterView(GenericAPIView):
       serializer_class = UserSerializers

       def post(self, request):
           serializer = UserSerializers(data=request.data)

           if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data, status=status.HTTP_201_CREATED)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       

class UserProfileView(ListAPIView):
      serializer_class = UserProfileSerilizer

      def get_queryset(self):
            user_id =  self.kwargs['user_id']
            return Users.objects.filter(id=user_id)


                 

                
                
