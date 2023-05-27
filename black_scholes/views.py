from django.shortcuts import render
from django.http import HttpResponse
from scipy.stats import norm
from math import exp, sqrt, log


def home(request):
    
    return render(request, 'black_scholes/home.html')

def black_scholes(request):

    Snot = float(request.POST['Snot'])
    K = float(request.POST['K'])
    r = float(request.POST['r'])/100
    sigma = float(request.POST['sigma'])/100
    T = float(request.POST['T'])/12

    d1 = (log(Snot/K)+(r+sigma*sigma/2)*T)/(sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T)

    u1 = norm(loc=0, scale=1).cdf(d1)
    u2 = norm(loc=0, scale=1).cdf(d2)

    result = Snot*u1 - exp(0-r*T)*K*u2

    result2 = result + K*exp(0-r*T) - Snot

    return render(request, 'black_scholes/result.html', {'result' : result, 'result2': result2})