from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

import datetime
import json
import pandas as pd

import base64

import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from deep_bau_app.utils.heatmap import viz_process


@csrf_exempt
def index(request):
    return render(request, "index.html")


@csrf_exempt
def predict(request):
    """View to predict output for selected prediction model

    Args:
        request (json): prediction model input (and parameters)

    Returns:
        json: prediction output
    """
    projects = [{"name":"Erschließung Ob den Häusern Stadt Tengen", "id":101227},
                    {"name":"Stadtbauamt Bräunlingen Feldweg", "id":101205}] 
    
    
    if request.method == "GET":
        
        context = {"projects": projects}
        return render(request, "app/predict.html", context)

    elif request.method == "POST":
        
        df = pd.read_csv('/home/tquentel/projects/SDaCathon/deep_bau/data/features/df_deep_bau.csv', index_col=0)
        
        id = int(request.POST['id'])
        days = int(request.POST['days'])

        context = {"projects": projects,
                   "image": viz_process(df, "Tätigkeit", id, days),
                   "personen": viz_process(df, "Person", id, days),
                   "geraete": viz_process(df, "GeraetID", id, days),
                   "wetter": viz_process(df, "Wetter", id, days)
                   }

        return render(request, 'app/predict.html', context)