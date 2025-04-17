from django.shortcuts import render
from rest_framework import response
from rest_framework import status
from .gemini import analyze_text_with_gemini
from .actionSuggestor import suggest_actions
from .models import ActionAnalyzer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def analyze(request):
    query =  request.data.get('query','')
    if not query:
        return response.Response({'error':'Query is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    analysis = analyze_text_with_gemini(query)
    tone = analysis.get('tone')
    intent = analysis.get('intent')
    
    suggestion =  suggest_actions(tone,intent)
    
    ActionAnalyzer.objects.create(
        query = query,
        tone = tone,
        intent = intent,
        suggested_action = suggestion
    )
    
    return response.Response({
        'query':query,
        'analysis':{
            'tone':tone,
            'intent':intent
        },
        'suggested_actions':suggestion
    })
