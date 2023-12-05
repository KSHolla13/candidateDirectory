from rest_framework import serializers
from .models import CandidateDirectory


class CandidateDirectorySerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='CandidateDirectory-Detail',  # 'yourmodel-detail' should be replaced with your actual DRF view name
    #     lookup_field='pk'
    # )
    # url = serializers.HyperlinkedIdentityField(view_name="CandidateDirectoryDetailAV")
    class Meta:
        model = CandidateDirectory
        fields = "__all__"


