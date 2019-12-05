from django.db import models
from rest_framework import serializers

import logging

class Test:
    def __init__(self, id="", name=""):
        self.id = id
        self.name = name


class TestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        """
        validated data is to verify if data is validated. Ot
        :param validated_data:
        :return:
        """
        if not validated_data:
            logging.log(1, "Empty validate data")
        return Test(**validated_data)

    def update(self, instance, validated_data):
        pass

testSerializer = TestSerializer(data={"id": "sd", "name": "yahya"})

testSerializer.is_valid()
"""
Json.parse can be used to parse the data into the data types of python. This can be passed on
"""
print(testSerializer.errors)