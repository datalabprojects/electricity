from django.shortcuts import render
from django.template.response import TemplateResponse
import pandas as pd
from .analyse import calculatecategory1load
from .analyse import calculatecategory2load
from .analyse import calculatecategory3load
from .analyse import calculatecategory4load
from .analyse import calculatecategory5load
from .analyse import calculatecategory6load
from .analyse import calculatecategory7load
from .analyse import calculatecategory8load
from .analyse import calculatecategory9load
from .analyse import calculatecategory10load
from .analyse import calculateTotalUnits
from . analyse import calculateUsage

# from . import analyse

df = pd.read_csv('electricity - Sheet1.csv')
df2 = pd.read_csv('appliances - Sheet1.csv')
dfaq = pd.read_csv('ELECTRICITY CONSUMPTION AND BILLING APPLICATION - FAQ.csv')
SA = df['Service Areas'].unique().tolist()
cat = df2['Category'].unique().tolist()
cat.insert(0, 'No Appliance')
quest = dfaq['Question'].unique().tolist()


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def table(request):
    return render(request, 'table.html')


def chart(request):
    return render(request, 'chart.html')


def unitcal(request):
    return render(request, 'unitcal.html')


def analysis(request):
    return render(request, 'analysis.html')

    # def unitcal(request):
    # unit_ = state["unit"] if "unit" in state else 0.0
    # unit_rate_ = state["unit_rate"] if "unit_rate" in state else 0.0

    # st.header("# ELECTRIC UNIT CALCULATOR ðŸŽˆ")
    # st.sidebar.markdown("# Main page ðŸŽˆ")

    # Amount = st.number_input('How much credit are you buying (Naira)')
    # MP = st.number_input('How much is your monthly oustanding debt repayment/Service fee')
    # sa = st.selectbox('Service Area', SA)

    amt = request.POST.get('amount')
    mp = request.POST.get('repayment')
    print('ámt', amt)

    # if amt and mp > 0:
    #     metered_amt = (amt - mp) * 0.925
    #     print("Metered amt ", metered_amt)
    # return render(request, 'unitcal.html', {'amount': amt, 'repayment': mp})


def getunit(request):
    amt = request.POST.get('amount')
    mp = request.POST.get('repayment')
    serviceArea = request.POST.get('serviceArea')
    propertyClass = request.POST.get('propertyClass')

    print('amount', amt)
    print('service area', serviceArea)
    print('property class', propertyClass)

    amt = int(amt)
    mp = int(mp)

    if amt > 0 and mp > 0:
        metered_amt = (amt - mp) * 0.925
        print("Metered amt ", metered_amt)

    result = getServiceArea(amt, serviceArea, propertyClass)
    distributionCompany = result[0]
    unitRate = result[1]
    unit = result[2]
    print("distribution company", result[0])
    print("unit", result[2])

    msg = {
        'amount': amt,
        'repayment': mp,
        'serviceArea': serviceArea,
        'propertyClass': propertyClass,
        'distributionCompany': distributionCompany,
        'unitRate': unitRate,
        'unit': unit
    }
    # return TemplateResponse(request, 'unitcal.html', msg)
    return TemplateResponse(request, 'analysis.html', msg)


def getServiceArea(amt, serviceArea, propertyClass):
    print("hello property")
    sa = serviceArea
    metered_amt = amt

    df1 = df[df['Service Areas'] == sa]
    print(f'Your Service  Area is  {df1}')
    DISCO = df1['Disco'].reset_index(drop=True)[0]
    print(f'Your Distribution Company is  {DISCO}')
    tar_class = df1['Tariff Type'].reset_index(drop=True).tolist()
    # Class = st.selectbox('Select Your Property Class', tar_class)
    Class = tar_class
    unit_rate = df1[df1['Tariff Type'] == Class]['Tariff Rate 2022']
    unit_rate = unit_rate.values[0]
    print(f'Your Unit rate is {unit_rate}')
    unit = metered_amt / unit_rate
    unit = round(unit, 2)
    print(f'Your purchased unit is {unit}')
    return DISCO, unit_rate, unit


def analyse(request):
    cat1 = request.POST.get('category1')
    cat2 = request.POST.get('category2')
    cat3 = request.POST.get('category3')
    cat4 = request.POST.get('category4')
    cat5 = request.POST.get('category5')
    cat6 = request.POST.get('category6')
    cat7 = request.POST.get('category7')
    cat8 = request.POST.get('category8')
    cat9 = request.POST.get('category9')
    cat10 = request.POST.get('category10')
    app1Hr = request.POST.get('app1Hr')
    app2Hr = request.POST.get('app2Hr')
    app3Hr = request.POST.get('app3Hr')
    app4Hr = request.POST.get('app4Hr')
    app5Hr = request.POST.get('app5Hr')
    app6Hr = request.POST.get('app6Hr')
    app7Hr = request.POST.get('app7Hr')
    app8Hr = request.POST.get('app8Hr')
    app9Hr = request.POST.get('app9Hr')
    app10Hr = request.POST.get('app10Hr')
    appName1 = request.POST.get('appName1')
    appName2 = request.POST.get('appName2')
    appName3 = request.POST.get('appName3')
    appName4 = request.POST.get('appName4')
    appName5 = request.POST.get('appName5')
    appName6 = request.POST.get('appName6')
    appName7 = request.POST.get('appName7')
    appName8 = request.POST.get('appName8')
    appName9 = request.POST.get('appName9')
    appName10 = request.POST.get('appName10')
    appNo1 = request.POST.get('appNo1')
    appNo2 = request.POST.get('appNo2')
    appNo3 = request.POST.get('appNo3')
    appNo4 = request.POST.get('appNo4')
    appNo5 = request.POST.get('appNo5')
    appNo6 = request.POST.get('appNo6')
    appNo7 = request.POST.get('appNo7')
    appNo8 = request.POST.get('appNo8')
    appNo9 = request.POST.get('appNo9')
    appNo10 = request.POST.get('appNo10')
    unitRate = request.POST.get('unitRate')
    unit = request.POST.get('unit')

    print('Unit', unit)
    unitRate = float(unitRate)
    unit = float(unit)

    print('app1Hr', app1Hr)
    print('category1', cat1)
    print('appName1', appName1)
    print('appNo1', appNo1)
    print('Unit Rate', unitRate)

    if cat1 != "" and appName1 != "" and app1Hr != "" and appNo1 != "":
        load1 = calculatecategory1load(cat1, appName1, app1Hr, appNo1)
        print("load", load1)
    else:
        load1 = 0

    if cat2 != "" and appName2 != "" and app2Hr != "" and appNo2 != "":
        load2 = calculatecategory2load(cat2, appName2, app2Hr, appNo2)
        print("load", load2)
    else:
        load2 = 0

    if cat3 != "" and appName3 != "" and app3Hr != "" and appNo3 != "":
        load3 = calculatecategory3load(cat3, appName3, app3Hr, appNo3)
        print("load", load3)
    else:
        load3 = 0

    if cat4 != "" and appName4 != "" and app4Hr != "" and appNo4 != "":
        load4 = calculatecategory4load(cat4, appName4, app4Hr, appNo4)
        print("load", load4)
    else:
        load4 = 0

    if cat5 != "" and appName5 != "" and app5Hr != "" and appNo5 != "":
        load5 = calculatecategory5load(cat5, appName5, app5Hr, appNo5)
        print("load", load5)
    else:
        load5 = 0

    if cat6 != "" and appName6 != "" and app6Hr != "" and appNo6 != "":
        load6 = calculatecategory6load(cat6, appName6, app6Hr, appNo6)
        print("load", load6)
    else:
        load6 = 0

    if cat7 != "" and appName7 != "" and app7Hr != "" and appNo7 != "":
        load7 = calculatecategory7load(cat7, appName7, app7Hr, appNo7)
        print("load", load7)
    else:
        load7 = 0

    if cat8 != "" and appName8 != "" and app8Hr != "" and appNo8 != "":
        load8 = calculatecategory8load(cat8, appName8, app8Hr, appNo8)
        print("load", load8)
    else:
        load8 = 0

    if cat9 != "" and appName9 != "" and app9Hr != "" and appNo9 != "":
        load9 = calculatecategory9load(cat9, appName9, app9Hr, appNo9)
        print("load", load9)
    else:
        load9 = 0

    if cat10 != "" and appName10 != "" and app10Hr != "" and appNo10 != "":
        load10 = calculatecategory10load(cat10, appName10, app10Hr, appNo10)
        print("load", load10)
    else:
        load10 = 0

    total_load = round(load1 + load2 + load3 + load4 + load5 + load6 + load7 + load8 + load9 + load10, 2)
    print("total load", total_load)

    if total_load > 0:
        monthly_estimate = round(total_load * 30, 2)
        print("total estimate", monthly_estimate)
        print("total estimate type", type(monthly_estimate))
        print("unit rate type", type(unitRate))

    if monthly_estimate > 0 and unitRate > 0:
        totalUnits = calculateTotalUnits(monthly_estimate, unitRate)
    else:
        totalUnits = 0

    if total_load > 0 and unit > 0:
        usage = calculateUsage(unit, total_load)
    else:
        usage = 0

    msg = {
        'category1': cat1,
        'category2': cat2,
        'category3': cat3,
        'category4': cat4,
        'category5': cat5,
        'category6': cat6,
        'category7': cat7,
        'category8': cat8,
        'category9': cat9,
        'category10': cat10,
        'app1Hr': app1Hr,
        'app2Hr': app2Hr,
        'app3Hr': app3Hr,
        'app4Hr': app4Hr,
        'app5Hr': app5Hr,
        'app6Hr': app6Hr,
        'app7Hr': app7Hr,
        'app8Hr': app8Hr,
        'app9Hr': app9Hr,
        'app10Hr': app10Hr,
        'appName1': appName1,
        'appName2': appName2,
        'appName3': appName3,
        'appName4': appName4,
        'appName5': appName5,
        'appName6': appName6,
        'appName7': appName7,
        'appName8': appName8,
        'appName9': appName9,
        'appName10': appName10,
        'appNo1': appNo1,
        'appNo2': appNo2,
        'appNo3': appNo3,
        'appNo4': appNo4,
        'appNo5': appNo5,
        'appNo6': appNo6,
        'appNo7': appNo7,
        'appNo8': appNo8,
        'appNo9': appNo9,
        'appNo10': appNo10,
        'total_load': total_load,
        'monthly_estimate': monthly_estimate,
        'totalUnits': totalUnits,
        'usage': usage
    }
    # return TemplateResponse(request, 'analysis.html', msg)
    return TemplateResponse(request, 'dashboard.html', msg)
