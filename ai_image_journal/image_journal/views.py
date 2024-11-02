from django.shortcuts import render
from .models import GeneratedImage
from .utils import img_gen  # Import the function
from django.http import JsonResponse


# Create your views here.

def generate_image_view(request):
    if request.method == 'POST':
        img = img_gen() #calls the function
        

        with open('img.png', 'rb') as image_file:
            new_image = GeneratedImage(content="User input prompt here", image=image_file)
            new_image.save()

        return JsonResponse({"message": "Image generated and saved!"})
    
    return JsonResponse({"error": "Bad Move Bitch."}, status=400)