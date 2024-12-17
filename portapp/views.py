from datetime import datetime
from django.shortcuts import render

def home(request):
    # Get the current hour
    current_hour = datetime.now().hour

    # Determine the greeting based on the time
    if current_hour < 12:
        greeting = "Good Morning!"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"

    # Pass the greeting to the template
    context = {
        'greeting': greeting
    }
    return render(request, 'index.html', context)
