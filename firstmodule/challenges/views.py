from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls.base import reverse

# Parameter is passed automatically when the function is executed
# def january(request):
#     # Return is the response that is being sent back to the client, to the browser sending that request
#     return HttpResponse("Eat no meat for the entire month")

# def february(request):
#     return HttpResponse("Walk for atleast 20 minutes every day !")


# def march(request):
#     return HttpResponse("Learn Django for every day atleast for 20 minutes !")


monthly_challenges = {
                    "january": "Eat no meat for the entire month",
                   "february": "Walk for atleast 20 minutes every day !",
                   "march" : "Learn Django for every day atleast for 20 minutes !",
                   "april": "Eat no meat for the entire month",
                   "may": "Walk for atleast 20 minutes every day !",
                   "june" : "Learn Django for every day atleast for 20 minutes !",
                   "july": "Eat no meat for the entire month",
                   "august": "Walk for atleast 20 minutes every day !",
                   "september" : "Learn Django for every day atleast for 20 minutes !",
                   "october": "Eat no meat for the entire month",
                   "november": "Walk for atleast 20 minutes every day !",
                   "december" : "Learn Django for every day atleast for 20 minutes !"
                   }


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalised_month = month.capitalize()
        month_path = reverse("month-challenge",args=[month])
        list_items +=f"<li><a href=\"{month_path}\">{capitalised_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


# Creating a dynamic which takes month as the input
def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponse("Invalid month")
    else:
        redirect_month = months[month-1 ]
        redirect_path = reverse("month-challenge",args=[redirect_month]) # redirects to  /challenges/january
        #return HttpResponseRedirect("/challenges/" + redirect_month) 
        """ If we had changed the extension in the mainapp urls, then it has to be hard coded every where
        instead of that , we use naming convention and reverse just to make sure that any changes in the urls of the
        mainapp must be in accord with the paths that are redirected to it """
        return HttpResponseRedirect(redirect_path )

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        response_text = f'<h1>{challenge_text}</h1>'
        # return HttpResponse(challenge_text)
        return HttpResponse(response_text)
    except:
        return HttpResponse(f"<h1>This is not supported !</h1>")


# Below is the old logic
# def monthly_challenge(request,month):
#     challenge_text = None
#     if month=='january':
#         challenge_text="Eat no meat for the entire month"
#     elif month=='february':
#         challenge_text="Walk for atleast 20 minutes every day !"
#     elif month=='march':
#         challenge_text="Learn Django for every day atleast for 20 minutes !"
#     else:
#         return HttpResponseNotFound("This month is not supported!")
#     return HttpResponse(challenge_text)
    
