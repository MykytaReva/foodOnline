from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib import messages


def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # using the form
            # password = form.cleaned_data['password']
            # print(form.cleaned_data)
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # form.save()

            # create user using method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password
            )
            user.role = User.CUSTOMER
            user.save()

            messages.success(request, 'Account created, check your inbox for the activation email.')

            return redirect('registerUser')
        else:
            print('Invalid form:')
            print(form.errors)
    else:
        form = UserForm()
    # form = UserForm()
    # form.save()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context=context)