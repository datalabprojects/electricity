from django.shortcuts import render
from django.template.response import TemplateResponse
import pandas as pd

# df = pd.read_csv('electricity - Sheet1.csv')
# df2 = pd.read_csv('appliances - Sheet1.csv')
# dfaq = pd.read_csv('ELECTRICITY CONSUMPTION AND BILLING APPLICATION - FAQ.csv')
# SA = df['Service Areas'].unique().tolist()
# cat = df2['Category'].unique().tolist()
# cat.insert(0, 'No Appliance')
# quest = dfaq['Question'].unique().tolist()


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def form(request):
    return render(request, 'form.html')


def chart(request):
    return render(request, 'chart.html')