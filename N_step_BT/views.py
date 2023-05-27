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

def home_n(request):
    
    return render(request, 'N_step_BT/home.html')

def n_step_calc(request):

    Snot = float(request.POST['Snot'])
    K = float(request.POST['K'])
    r = float(request.POST['r'])/100
    sigma = float(request.POST['sigma'])/100
    T = float(request.POST['T'])/12
    div = float(request.POST['dividend'])/100
    n = int(request.POST['n'])

    u = exp(sigma*sqrt(T/n))
    d = 1/u
    p = (exp((r-div)*T/n) - d)/(u-d)
    alpha = 0
    for i in range(0,n+1):
        alpha += nCr(n, i)*pow(p,i)*pow(1-p, n-i)*max(Snot*pow(u,i)*pow(d,n-i)-K, 0)
    result = exp(0-r*T)*alpha
    result2 = result + K*exp(0-r*T) - Snot*exp(0-div*T)


    return render(request, 'N_step_BT/result.html', {'result' : result, 'delT':T/n, 'u':u, 'd':d, 'p':p, 'result2':result2})