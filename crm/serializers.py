from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):  #serializer function for customer
    class Meta:
        model = Customer
        fields = (
            'cust_name', 'organization', 'role', 'email', 'bldgroom', 'address', 'account_number', 'city', 'state',
            'zipcode', 'phone_number')
