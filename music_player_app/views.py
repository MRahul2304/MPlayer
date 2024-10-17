from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistrationForm, LoginForm
from .models import Song  # Import your Song model
from .serializers import SongSerializer  # Import your Song serializer
from rest_framework import generics
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Song
from .serializers import SongSerializer

class SongCreateView(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)  # Print the errors for debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def AddSong(request):
    return render(request, 'AddSong.html')

@login_required
def UpdateSong(request, pk):
    return render(request, 'UpdateSong.html')
