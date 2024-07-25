from django.shortcuts import render
from rest_framework.views import APIView, Response

from api.serializers.query_basic_model_serializer import QueryBasicModelSerializer
from api.services.llm_service import LLMService
# Create your views here.

class QueryBasicView(APIView):
    
    def get(self, request):
        return Response(status=200)
    
    def post(self, request):
        data = QueryBasicModelSerializer(data=request.data)
        

        if data.is_valid():
            llm_service = LLMService()
            
            response = llm_service.get_response(data.validated_data["query"])
            content = response.content

            return Response({'response': f"{content}"}, status=200)
        
        return Response(data.errors, status=400)