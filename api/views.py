from django.shortcuts import render
from rest_framework.views import APIView, Response

from api.serializers.query_basic_model_serializer import QueryBasicModelSerializer
# Create your views here.

class QueryBasicView(APIView):
    
    def get(self, request):
        return Response(status=200)
    
    def post(self, request):
        data = QueryBasicModelSerializer(data=request.data)
        llm_service = LLMService()
        if data.is_valid():
            return Response({'response': f"{data.validated_data["query"]}"}, status=200)
        
        return Response(data.errors, status=400)