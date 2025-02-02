from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Needed for AJAX requests
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

    # Handle AJAX form submission
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        service = request.POST.get("service")
        message = request.POST.get("message")

        try:
                # Get the form data
                name = request.POST.get("name")
                email = request.POST.get("email")
                phone = request.POST.get("phone")
                service = request.POST.get("service")
                message = request.POST.get("message")
                
                # Prepare the email content
                email_subject = f"New Contact Me Form submission: {service}"
                email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nService: {service}\nMessage: {message}"
                
                # Send email using Mailgun domain
                send_mail(
                    email_subject,
                    email_message,
                    'info@jabezhuya.tech' , #my custom sender
                    ['mukoshijabez@gmail.com',
                    'mukoshijabez@yahoo.com'],  # Authorized recipient email
                    fail_silently=False,
                )
                
                # Return success response
                return JsonResponse({"status": "success", "message": "Your message has been sent successfully!"})
            
        except Exception as e:
                # Handle any errors
                return JsonResponse({
                    "status": "error",
                    "message": f"Failed to send your message: {str(e)}"
                })


    # Render the webpage with the greeting
    context = {
        'greeting': greeting,
    }
    return render(request, 'index.html', context)
