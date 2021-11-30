# -*- coding: utf-8 -*-
from django.shortcuts import render
#from django.http import HttpResponse
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
model = pickle.load(open('cgpa_for_stud.pkl', 'rb'))
standard_to = StandardScaler()
def index(request):
    return render(request,'index.html')
def predict(request):
    
    
    if request.method == 'POST':
        SEM1 =request.POST.get('1_SEM')
        SEM2=request.POST.get('2_SEM')
        SEM3=request.POST.get('3_SEM')
        SEM4=request.POST.get('4_SEM')
        prediction=model.predict([[SEM1,SEM2,SEM3,SEM4]])
        output=np.round(prediction[0],2)
        print(output)
        if output<0 or output>10:
            params={'text':" ",'prediction_text':"PLEASE ENTER  CORRECT DETAILS"}
            return render(request,'index.html',params)
        else:
            params={'text':'Your SGPA could be','prediction_text':output}
            return render(request,'index.html',params)
    else:
        return render(request,'index.html')
