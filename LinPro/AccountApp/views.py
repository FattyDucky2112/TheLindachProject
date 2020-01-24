from django.shortcuts import render
from django.views.generic import View,TemplateView
from accountapp.forms import UserForm


# class login(TemplateView):
#     template_name = "login.html"

# class register(TemplateView):
#     template_name = "login.html"
def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)


        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.set_password)
            user.save()
            registered = True



        else:
            print(user_form.errors)

    else:
        user_form = UserForm()


    return render(request, 'register.html', {'user_form':user_form,
                                        'registered':registered
                                        })
