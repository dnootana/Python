from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

month_dict = {
    "january": "This is January",
    "february": "This is February",
    "march": "This is March",
    "april": "This is April!",
    "may": "This is May!",
    "june": "This is June!",
    "july": "This is July",
    "august": "This is August!",
    "september": "This is September!",
    "october": "This is October!",
    "november": "This is November",
    "december": None,
}


def index(request):
    months = list(month_dict.keys())
    # response_data = "<ul>"
    # for month in months:
    #     link_url = reverse("month-challenge", args=[month])
    #     response_data += f"<li><a href='{link_url}'>{month.capitalize()}</a></li>"
    # response_data += "</ul>"
    # return HttpResponse(response_data)
    return render(request,'challenges/index.html',{
        "months": months
    })


def jan(request):
    return HttpResponse("This works, and it is january!")


def feb(request):
    return HttpResponse("This is february!")


def monthly_challenge_by_number(request, month_name):
    challenge_text = None
    try:
        all_months = list(month_dict.keys())
        redirect_month = all_months[month_name - 1]
        redirect_url = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_url)
    except:
        response_msg = render_to_string('404.html')
        return HttpResponseNotFound(response_msg)


def monthly_challenge(request, month_name):
    challenge_text = None
    try:
        challenge_text = month_dict[month_name]
        return render(request,"challenges/challenge.html",{
            'text': challenge_text,
            'month': month_name,
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # response_msg = render_to_string('404.html')
        # return HttpResponseNotFound(response_msg)
        raise Http404()
