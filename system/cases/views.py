def case_select(request):
	if not request.user.is_authenticated:
		return redirect('login')
	return render(request, 'case_select.html')
from django.contrib.auth import logout
def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('login')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.

def login_view(request):
	error = None
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			error = '账号或密码错误'
	return render(request, 'login.html', {'error': error})

def index(request):
	if not request.user.is_authenticated:
		return redirect('login')
	return render(request, 'index.html')
# Create your views here.
