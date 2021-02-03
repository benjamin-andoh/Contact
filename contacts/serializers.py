from rest_framework.serializers import ModelSerializer
from contacts.models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'country_code',
                  'phone_number', 'contact_picture', 'is_favorite', 'owner']

        # extra_kwargs = {'owner': {'read_only': True, 'required': False}}
