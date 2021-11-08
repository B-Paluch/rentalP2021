from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404



# Create your views here.
from users.forms import ItemCreateForm, RentItemForm
from users.models import RentItem


def login(request):
    if request.user.is_authenticated:
        messages.error(request, 'Jestes juz zalogowany, nie mozesz sie zalogować drugi raz')
        return render(request, 'users/index.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('rentalUsername')
            password = request.POST.get('rentalPassword')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Pomyślnie zalogowano')
                return render(request, 'users/index.html')
            else:
                messages.error(request, 'Invalid credentials')
                return render(request, 'users/login.html')
        else:
            return render(request, 'users/login.html')

@login_required()
def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request, 'Pomyślnie wylogowano')
        return redirect('login')

def index(request):
    return render(request, 'users/index.html')

def lenditems(request):
    allitems = RentItem.objects.all()

    return render(request, 'users/lenditem.html', {'allitems': allitems})

@login_required()
def returnitems(request):
    return render(request, 'users/returnitems.html')

@login_required()
def additems(request):
    if request.method == 'POST':
        additems = ItemCreateForm(request.POST)
        if additems.is_valid():
            additems.save()
            return redirect('additems')
        else:
            return HttpResponse("""błędny formularz""")
    else:
        additems = ItemCreateForm()
        return render(request, 'users/additems.html', {'form': additems})

@login_required()
def lentlist(request):
    return render(request, 'users/lentlist.html')



def lenditem(request, _id):
    old_data = get_object_or_404(RentItem,id =_id )
    old_data.rentState = True

    form =RentItemForm(request.POST or None, instance =old_data)

    if form.is_valid():
            form.save()
            return HttpResponseRedirect('lenditem') 
            
    context ={'form':form }

    return render(request,'users/lendsingleitem.html',context)


