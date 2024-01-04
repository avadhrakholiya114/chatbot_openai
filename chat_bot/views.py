from django.shortcuts import render
import openai, os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)


def chat_bot(request):
    chat_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get("user_input")
        prompt=user_input
        response=openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            temperature=0.5
        )

        print(response)
    return render(request, 'main.html', {})
