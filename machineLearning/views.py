from typing import ContextManager
from django.shortcuts import HttpResponse, render
import pickle

def home(request):
    new_predict = 0
    predict = None
    if request.method == 'POST':
        room = request.POST.get('room')
        bathroom = request.POST.get('bathroom')
        Balcony = request.POST.get('Balcony')
        SquareFt = request.POST.get('Square.Ft')
        floor = request.POST.get('floor')
        kolkata = request.POST.get('kolkata')
        newtown = request.POST.get('newtown')
        saltlake = request.POST.get('saltlake')
        prediction = pickle.load(open('housePrice.pkl', 'rb'))
        try:
            new_predict=round(prediction.predict([[room, bathroom, Balcony, SquareFt, floor, kolkata, newtown, saltlake]])[0],2)
        except Exception as e:
            print(e)
       
        
    return render(request, 'home.html',{"predict": new_predict}) 
    
