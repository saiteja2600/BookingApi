from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import BookSlot, Register
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from datetime import datetime
from django.utils.html import format_html

def Home(request):
    if 'user_email' not in request.session:
        return redirect('login')
    return render(request, 'FrontEnd/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Register.objects.get(email=email)

            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                messages.success(request, "Login successful.")
                return redirect('home')
            else:
                messages.error(request, "Invalid password.")
        except Register.DoesNotExist:
            messages.error(request, "Email not found.")

    return render(request, 'FrontEnd/login.html')

def logout(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')

        if password != conf_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'FrontEnd/signup.html')

        if Register.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'FrontEnd/signup.html')

        try:
            hashed_password = make_password(password)
            user = Register.objects.create(
                username=username,
                email=email,
                password=hashed_password,
                conf_password=hashed_password
            )
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Something went wrong: {e}")

    return render(request, 'FrontEnd/signup.html')

def about(request):
    if 'user_email' not in request.session:
        return redirect('login')
    return render(request, 'FrontEnd/about.html')

def schedule(request):
    if 'user_email' not in request.session:
        return redirect('login')

    user_email = request.session['user_email']
    bookings = BookSlot.objects.filter(client_email=user_email)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        events = [{
            "start": f"{b.date}T{b.time.strftime('%H:%M:%S')}",
            "title": f"{b.client_name} | {b.slottype} | {b.trainee} | {b.time.strftime('%I:%M %p')}",
        } for b in bookings]
        return JsonResponse(events, safe=False)

    schedule = {}
    for booking in bookings:
        schedule.setdefault(booking.date, []).append(booking)

    return render(request, 'FrontEnd/schedule.html', {
        'schedule': schedule
    })

def bookSlot(request):
    if 'user_email' not in request.session:
        return redirect('login')

    user_email = request.session['user_email']
    try:
        user = Register.objects.get(email=user_email)
        client_name = user.username
    except Register.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('login')

    slottype = request.GET.get('slot_type', '')  
    trainees = BookSlot.TRAINEE_MAPPING.get(slottype, [])

    form_data = {
        'client_name': '',
        'client_email': '',
        'trainee': '',
        'date': '',
        'time': ''
    }

    if request.method == 'POST':
        form_data = {
            'client_name': request.POST.get('client_name', ''),
            'client_email': request.POST.get('client_email', ''),
            'trainee': request.POST.get('trainee', ''),
            'date': request.POST.get('date', ''),
            'time': request.POST.get('time', '')
        }

        if all(form_data.values()):
            trainee_conflict = BookSlot.objects.filter(
                trainee=form_data['trainee'],
                date=form_data['date'],
                time=form_data['time']
            ).exists()

            if trainee_conflict:
                messages.error(request, f"{form_data['trainee']} is already booked at {form_data['date']} {form_data['time']}.")
                form_data.update({'trainee': '', 'date': '', 'time': ''})
            else:
                existing_booking = BookSlot.objects.filter(
                    client_email=form_data['client_email'],
                    trainee=form_data['trainee'],
                    date=form_data['date'],
                    time=form_data['time']
                ).exists()

                if existing_booking:
                    messages.error(request, "You have already booked this slot.")
                else:
                    BookSlot.objects.create(
                        client_name=form_data['client_name'],
                        client_email=form_data['client_email'],
                        slottype=slottype,
                        trainee=form_data['trainee'],
                        date=form_data['date'],
                        time=form_data['time']
                    )

                    formatted_time = datetime.strptime(form_data['time'], "%H:%M").strftime("%I:%M %p")

                    subject = "Slot Booking Confirmation - Fitness Studio"
                    html_message = f"""
                    <div style="font-family: Arial, sans-serif; font-size: 16px;">
                        <p>Hi {form_data['client_name']},</p>
                        <p>Your booking is <strong>confirmed</strong>!</p>
                        <p><strong>Details:</strong></p>
                        <ul>
                            <li><strong>Slot Type:</strong> {slottype}</li>
                            <li><strong>Trainee:</strong> {form_data['trainee']}</li>
                            <li><strong>Date:</strong> {form_data['date']}</li>
                            <li><strong>Time:</strong> {formatted_time}</li>
                        </ul>
                        <p>Thank you for choosing <strong>Fitness Studio</strong>.</p>
                    </div>
                    """

                    email = EmailMessage(
                        subject=subject,
                        body=html_message,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[form_data['client_email']],
                    )
                    email.content_subtype = "html"
                    email.send()

                    messages.success(request, "Slot booked successfully and confirmation email sent!")
                    return redirect('schedule')

    return render(request, 'FrontEnd/bookslot.html', {
        'slot_type': slottype,
        'trainees': trainees,
        'form_data': form_data
    })

def slot_delete(request, client_id):
    if 'user_email' not in request.session:
        return redirect('login')

    user_email = request.session['user_email']
    slot = get_object_or_404(BookSlot, client_id=client_id, client_email=user_email)
    
    slot.delete()
    messages.success(request, "Slot deleted successfully!")
    return redirect('schedule')