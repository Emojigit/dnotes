from django.shortcuts import render, redirect
from django.http import HttpResponse
from main import models, settings, util
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import json

sitename = settings.site_name

# Create your views here.


login = LoginView.as_view(template_name="login.html",extra_context={"sitename":sitename,"title":"Login"})
logout = LogoutView.as_view(template_name="logout.html",extra_context={"sitename":sitename,"title":"Logout"})

@login_required(login_url="/login/")
def dashboard(request):
    title = "Dashboard"
    if "errormsg" in request.GET:
        errormsg = request.GET["errormsg"]
    notelist = models.Note.objects.filter(owner=request.user)
    return render(request, "dashboard.html", {**globals(),**locals()})

@login_required(login_url="/login/")
def index(request):
    return redirect("/dashboard/")

def register(request):
    META = request.META
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request,"register.html",{**globals(),**locals()})

@login_required(login_url="/login/")
def post_action(request):
    if request.POST:
        data = request.POST
        if "type" in data:
            if data["type"] == "create":
                n = models.Note.objects.create(title=data["title"],owner=request.user,content=data["content"])
                n.save()
                return redirect("/note/" + n.tid + "/")
            else:
                if models.Note.objects.filter(tid=data["tid"]).exists():
                    n = models.Note.objects.get(tid=data["tid"])
                    if n.owner == request.user:
                        if data["type"] == "delete":
                            n.delete()
                            return redirect("/dashboard/")
                        elif data["type"] == "modify":
                            n.title = data["title"]
                            n.content = data["content"]
                            n.link_share = True if "linkshare" in data and data["linkshare"] == "yes" else False
                            n.save()
                            return redirect("/note/" + n.tid + "/")
    return redirect("/dashboard/?errormsg=Some%20Error%20Occurs.")

def note(request, tid: str):
    data = request.GET
    if models.Note.objects.filter(tid=tid).exists():
        n = models.Note.objects.get(tid=tid)
        if util.can_user_see_note(request.user,n):
            title = n.title
            return render(request, "note.html", {**globals(),**locals()})
    # Fallback 404
    title = "404"
    message = "Note Not Found"
    return render(request, "error.html", {**globals(),**locals()}, status=404)

