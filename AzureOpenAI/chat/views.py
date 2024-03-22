from django.shortcuts import render
from django.http import JsonResponse 
from openai import AzureOpenAI
import os
import json

# Create your views here.

with open('.\config.json') as config_fie:
    config_details = json.load(config_fie)

client = AzureOpenAI(
    azure_endpoint = config_details["OPENAI_API_BASE"], 
    api_key=os.getenv("OPENAI_API_KEY"),  
    api_version= config_details["OPENAI_API_VERSION"]
)


def get_completion(prompt):
    print(prompt)
    query = client.chat.completions.create(
        model=config_details["CHATGPT_MODEL"],
        messages=[
            # {"role": "system", "content": "you are a Microsoft SQL Server expert."},
            {"role" : "user","content" : prompt}              
        ]
    )
    response = query.choices[0].message.content
    print(response)
    return response

def query_view(request): 
    if request.method == 'POST': 
        prompt = request.POST.get('prompt') 
        response = get_completion(prompt) 
        return JsonResponse({'response': response}) 
    return render(request, 'index.html') 
    

