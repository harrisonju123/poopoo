from rest_framework import viewsets
from pooapp.models.poops import Poops
from ..ai.openai_service import evaluate_poop_log
from ..serializers import PoopsSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from ..dataclass import EvaluationResult
import json
import re

def poop_evaluation(request, user_id):
    # Evaluate the poop log using the OpenAI service
    content = evaluate_poop_log(user_id)
    pattern = r'\{.*?\}'
    matches = re.findall(pattern, content, re.DOTALL)
    evaluation_json = json.loads(matches[0])

    return JsonResponse(evaluation_json)


class PoopsViewSet(viewsets.ModelViewSet):
    queryset = Poops.objects.all()
    serializer_class = PoopsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Validation Errors: ", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
