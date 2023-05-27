from django.shortcuts import render
from django.http import HttpResponse
from math import exp, sqrt, pow

def nCr(n, r):
    return (fact(n) / (fact(r) * fact(n - r)))
 
def fact(n):
    if n == 0:
        return 1
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res

def max(x,y):
    if x > y:
        return x
    else:
        return y

def home(request):
    
    return render(request, 'Two_step_BT/home.html')

def two_step_calc(request):

    Snot = float(request.POST['Snot'])
    K = float(request.POST['K'])
    r = float(request.POST['r'])/100
    sigma = float(request.POST['sigma'])/100
    T = float(request.POST['T'])/12
    div = float(request.POST['dividend'])/100

    u = exp(sigma*sqrt(T/2))
    d = 1/u
    p = (exp((r-div)*T/2) - d)/(u-d)
    alpha = 0
    for i in range(0,3):
        alpha += nCr(2, i)*pow(p,i)*pow(1-p, 2-i)*max(Snot*pow(u,i)*pow(d,2-i)-K, 0)
    result = exp(0-r*T)*alpha
    result2 = result + K*exp(0-r*T) - Snot*exp(0-div*T)


    return render(request, 'Two_step_BT/result.html', {'result' : result, 'delT':T/2, 'u':u, 'd':d, 'p':p, 'result2':result2})