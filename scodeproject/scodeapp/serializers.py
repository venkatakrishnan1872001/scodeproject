

from django.forms.models import model_to_dict
import pytz
from rest_framework import serializers

from .models import Blog,Scodedetail
from django.utils import timezone

from django.db.models import Max
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import permissions, generics, status
from rest_framework import serializers
from rest_framework import serializers, status
from rest_framework.response import Response



class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields ='__all__'


class ScodedetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scodedetail
        fields ='__all__'