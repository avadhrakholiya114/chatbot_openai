from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import openai, os, requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
openai.api_key = api_key


def image_genrate(request):
    chat_response = None
    if api_key is not None and request.method == 'POST':
        user_input = request.POST.get("user_input")

        response = openai.Image.create(

            prompt=user_input,
            size='256x256',

        )

        print(response)
        img_url = response['data'][0]['url']
        response = requests.get(img_url)
        print(response)
    return render(request, 'image.html', {"response": chat_response})
