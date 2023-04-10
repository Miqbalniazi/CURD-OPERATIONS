from rest_framework.serializers import ModelSerializer
from .models import CURD_APP_Contact


class ContactSerializer(ModelSerializer):

    class Meta:
        model = CURD_APP_Contact

        fields = ['country_code', 'id', 'first_name', 'last_name', 'phone_number',
                  'contact_picture', 'is_favorite'
                  ]