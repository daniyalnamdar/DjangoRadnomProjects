from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

def scrape(request):
    page = requests.get('https://www.facebook.com')
    soup = BeautifulSoup(page.text, 'html.parser')
    
    linkAddress = []
    
    for link in soup.find_all('a'):
        linkAddress.append(link.get('href'))
        
    return render(request, 'myapp/result.html',{'linkAddress': linkAddress})