from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

def home(request):
    # Get the current time based on the server's time zone
    current_time = datetime.now()

    # Check for the user's time zone offset in cookies
    timezone_offset = request.COOKIES.get('timezone_offset')
    if timezone_offset:
        try:
            # Convert the offset to an integer (in minutes)
            offset_minutes = int(timezone_offset)
            # Adjust the server time by the offset to get the user's local time
            current_time -= timedelta(minutes=offset_minutes)
        except ValueError:
            # Handle invalid offset values gracefully
            pass

    # Get the current hour in the user's local time zone
    current_hour = current_time.hour

    # Determine the greeting based on the local time
    if current_hour < 12:
        greeting = "Good Morning!"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"

    # Pass the greeting to the template
    context = {
        'greeting': greeting
    }

    # Handle form submission
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        service = request.POST.get("service")
        message = request.POST.get("message")

        # Example: Send an email (configure your email settings in settings.py)
        try:
            send_mail(
                subject=f"New contact form submission: {service}",
                message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
                from_email=email,
                recipient_list=["mukoshijabez@yahoo.com",
                                'mukoshijabez@gmail.com'],
            )
            context['success'] = "Your message has been sent successfully!"
        except Exception as e:
            context['error'] = f"Failed to send your message: {str(e)}"

    return render(request, 'index.html', context)

