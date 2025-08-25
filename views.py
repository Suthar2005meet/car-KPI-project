from django.shortcuts import render # type: ignore
from .models import Car # type: ignore
import pandas as pd # type: ignore

def car_stats(request):
    cars = Car.objects.all().values()
    df = pd.DataFrame(cars)

    stats = {}
    if not df.empty:
        stats['avg_budget'] = df['budget'].mean()
        stats['max_mileage'] = df['mileage'].max()

    return render(request, "car_stats.html", {"stats": stats})
