from django.shortcuts import redirect, render
from .models import Etudiant , Formation  , Insc
# Create your views here.
from django.contrib.auth import authenticate, login , logout




def auth_view(request,id=None):
    if request.method == 'POST':
        if "login_submit" in request.POST:
            email = request.POST.get('email')
            password = request.POST["password"]
            print(password)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if id:
                    return redirect('formation-detail',id) 
                else :
                    return redirect("landing-page")
            else:
                return render(request, 'courses/auth/auth.html',
                            
                            {'error_message': 'Invalid credentials. Please try again.' ,
                            "formation_id":id})
        if "signup_submit" in request.POST:
            print("SIGNUP")
            # Retrieve form data
            first_name = request.POST.get('nom')
            last_name = request.POST.get('prenom')
            email = request.POST.get('email')
            numero_tel = request.POST.get('numero')
            # address = request.POST.get('address')
            niveau = request.POST.get('niveau')
            password = request.POST.get('password')
            username = f'{first_name} {last_name}  '
            new_etudiant = Etudiant.objects.create_user(username = username ,email=email, first_name=first_name, last_name=last_name,
                                                        numero_tel=numero_tel, niveau=niveau,
                                                        password=password)
            
            
            
            user = authenticate(request, email=email, password=password)
            
            login(request , user)
            if id:
                    return redirect('formation-detail',id) 
            else :
                return redirect("landing-page")
            
    else:
        return render(request, 'courses/auth/auth.html' , {"formation_id":id})

def logout_view(request):
	logout(request)
	return redirect('landing-page')



def create_formation(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        localisation = request.POST.get('localisation')
        cout = request.POST.get('cout')

        formation = Formation.objects.create(
            title=title,
            desc=desc,
            localisation=localisation,
            cout=cout
        )
        
        return redirect('list-formations')


    return render(request, 'courses/add_formation.html')



#Formation

def landing_page(request):
    formations = Formation.objects.all()
    top_formations = formations.filter(top=True)
    return render(request , 'courses/index.html' , {'formations' : formations , "top_formations":top_formations})



def formation_details(request,id):
    formation = Formation.objects.get(id=id)
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if not user :
            return redirect('mes-formations',request.user.id) 
        return redirect('formation-detail',id)
        
    return render(request , 'courses/formation.html' , {'formation':formation})

def inscrire(request,id):
    
    etudiant_id = request.user.id 
    i , _= Insc.objects.get_or_create(etudiant_id=etudiant_id,formation_id = id)
    
    
    return redirect('mes-formations' , etudiant_id)

def mes_formations(request,id):
    if not request.user.is_authenticated :
        redirect("login-etudiant")
        
    inscriptions = Insc.objects.filter(etudiant_id = id)
    formations = []
    for i in inscriptions:
        formation = Formation.objects.get(id = i.formation_id) 
        formations.append(formation)
        
    return render(request , "courses/mes_formations.html", {"formations":formations,"inscriptions":inscriptions})

