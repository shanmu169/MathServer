from django.shortcuts import render
def mileage(request):
    distance= int(request.POST.get('Distance', 0))
    feulconsumed=int(request.POST.get('feulconsumed',0))
    mileage = distance/feulconsumed if request.method == 'POST' and feulconsumed!=0 else 0
    print("Distance_Travelled=",distance)
    print("FeulConsumed =",feulconsumed)
    print("mileage=", mileage)
    return render(request,'mathapp/math.html',{'distance':distance,'feulconsumed':feulconsumed,'mileage':mileage})