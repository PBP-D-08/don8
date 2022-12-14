from django.shortcuts import render
from homepage.models import Donation
from authentication.models import User
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from donation_app.forms import DonationForm
from django.contrib.auth.decorators import login_required
import datetime, time, json
from django.core.serializers.json import DjangoJSONEncoder
from donation_app.models import UserDonation
from django.views.decorators.csrf import csrf_exempt
from organizations_profile.models import ProfileO

def show_donation_page(request, id):

    context = {
        "form": DonationForm(),
    }

    if request.user.is_authenticated and not request.user.is_superuser:
        if request.user.role == 1:
            context["pengguna"] = True
    else :
        context["pengguna"] = False
    
    return render(request, "donation_page.html", context)


@login_required(login_url="/auth/login/")
def make_donation(request, id):
    form = DonationForm(request.POST or None)
    if request.POST and form.is_valid():
        request.session["last_donation" + str(id)] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = form.save(request, id)  # form.save() return data
        
        return JsonResponse({"data": data, "time": request.session["last_donation" + str(id)]})


def show_json(request):
    donations = Donation.objects.all()
    donations_dict = []
    for d in donations:
        donations_dict.append(
            {
                "pk": d.pk,
                "fields": {
                    "title": d.title,
                    "description": d.description,
                    "date_expired": d.date_expired,
                    "image_url": d.image_url,
                    "date_created": d.date_created,
                    "money_needed": d.money_needed,
                    "money_accumulated": d.money_accumulated,
                    "is_saved": d.saved.filter(
                        user__username=request.user.username
                    ).exists(),
                    "curr_role": request.user.role
                    if request.user.is_authenticated
                    else None,
                },
            }
        )
    return HttpResponse(
        json.dumps(donations_dict, indent=1, cls=DjangoJSONEncoder),
        content_type="application/json",
    )


# mengambil data donasi dalam json by id
def get_donation_data(request, id):
    donation_data = Donation.objects.filter(id=id)
    return HttpResponse(
        serializers.serialize("json", donation_data), content_type="application/json"
    )


def get_organization(request, id):
    organization_data = User.objects.filter(id=id)
    # organization_data = User.objects.all()
    return HttpResponse(
        serializers.serialize("json", organization_data),
        content_type="application/json",
    )


def check_user(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        if request.user.role == 1:

            return JsonResponse({"pengguna": True})

    return JsonResponse({"pengguna": False})


def get_current_date(request):
    return JsonResponse({"current_date": datetime.date.today()})


def get_last_donation(request, id):
    if request.user.is_authenticated and not request.user.is_superuser:
        if request.user.role == 1:
            return JsonResponse({"time": request.session.get("last_donation" + str(id), "-")})
    return JsonResponse({"time": None})


@csrf_exempt
def flutter_make_donation(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

    # get data needed
    user = User.objects.get(id=data["user"])
    donation = Donation.objects.get(id=data["donation"])
    organization = ProfileO.objects.get(organization=data["organization"])

    # update data
    user.balance -= data["amount_of_donation"]
    donation.money_accumulated += data["amount_of_donation"]
    donation.user.balance += data["amount_of_donation"]

    # save updated data
    user.save()
    donation.save()
    organization.save()
    donation.user.save()

    # add new UserDonation to database
    UserDonation.objects.create(
        user = user,
        organization = donation.user,
        donation = donation,
        date = datetime.datetime.now(),
        amount_of_donation = data["amount_of_donation"]
    )
    return JsonResponse({"success": "You've successfully made a donation"}) 

def flutter_donation_creator(request, id): # donation id
    donation = Donation.objects.get(id=id)
    return JsonResponse(
        {"pk": donation.user.pk, "username": donation.user.username}
    )

def get_user_donations(request):
    user_donations = UserDonation.objects.all()
    return HttpResponse(
        serializers.serialize("json", user_donations), content_type="application/json"
    )