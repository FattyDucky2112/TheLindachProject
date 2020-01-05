from django.shortcuts import render
from django.views.generic import View,TemplateView
from accountapp.forms import UserForm, UserProfileInfoForm


# class login(TemplateView):
#     template_name = "login.html"

# class register(TemplateView):
#     template_name = "login.html"
def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.set_password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'login.html', {'user_form':user_form,
                                        'profile_form':profile_form,
                                        'registered':registered
                                        })
