from django.shortcuts import render
from django.template.response import TemplateResponse
import pandas as pd

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

    if amt and mp > 0:
        metered_amt = (amt - mp) * 0.925
        print("Metered amt ", metered_amt)

    result = getServiceArea(amt, serviceArea, propertyClass)
    distributionCompany = result[0]
    unitRate = result[1]
    unit = result[2]
    print("distribution company", result[0])

    msg = {
        'amount': amt,
        'repayment': mp,
        'serviceArea': serviceArea,
        'propertyClass': propertyClass,
        'distributionCompany': distributionCompany,
        'unitRate': unitRate,
        'únit': unit
    }
    return TemplateResponse(request, 'unitcal.html', msg)


def getServiceArea(amt, serviceArea, propertyClass):
    sa = serviceArea
    metered_amt = amt

    df1 = df[df['Service Areas'] == sa]
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
    # if unit:
    #  return unit
    #
    # if unit_rate:
    #  return unit_rate


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

    print('app1Hr', app1Hr)
    print('category1', cat1)
    print('appName1', appName1)
    print('appNo1', appNo1)

    if cat1 != "" and appName1 != "" and app1Hr != "" and appNo1 != "":
        load1 = calculateCategory1Load(cat1, appName1, app1Hr, appNo1)
        print("load", load1)
    else:
        load1 = 0

    if cat2 != "" and appName2 != "" and app2Hr != "" and appNo2 != "":
        load2 = calculateCategory2Load(cat2, appName2, app2Hr, appNo2)
        print("load", load2)
    else:
        load2 = 0

    if cat3 != "" and appName3 != "" and app3Hr != "" and appNo3 != "":
        load3 = calculateCategory3Load(cat3, appName3, app3Hr, appNo3)
        print("load", load3)
    else:
        load3 = 0

    if cat4 != "" and appName4 != "" and app4Hr != "" and appNo4 != "":
        load4 = calculateCategory4Load(cat4, appName4, app4Hr, appNo4)
        print("load", load4)
    else:
        load4 = 0

    if cat5 != "" and appName5 != "" and app5Hr != "" and appNo5 != "":
        load5 = calculateCategory5Load(cat5, appName5, app5Hr, appNo5)
        print("load", load5)
    else:
        load5 = 0

    if cat6 != "" and appName6 != "" and app6Hr != "" and appNo6 != "":
        load6 = calculateCategory6Load(cat6, appName6, app6Hr, appNo6)
        print("load", load6)
    else:
        load6 = 0

    if cat7 != "" and appName7 != "" and app7Hr != "" and appNo7 != "":
        load7 = calculateCategory7Load(cat7, appName7, app7Hr, appNo7)
        print("load", load7)
    else:
        load7 = 0

    total_load = load1 + load2 + load3 + load4 + load5 + load6 + load7
    print("total load", total_load)

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
        'appNo7': appNo7
    }
    return TemplateResponse(request, 'analysis.html', msg)


def calculateCategory1Load(cat1, appName1, app1Hr, appNo1):
    df3 = df2[df2['Category'] == cat1]

    Load = df3[df3['Appliance'] == appName1]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load)
    load = (int(Load) * int(app1Hr) * int(appNo1)) / 1000
    return load


def calculateCategory2Load(cat2, appName2, app2Hr, appNo2):
    df3 = df2[df2['Category'] == cat2]

    Load2 = df3[df3['Appliance'] == appName2]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load2)
    load2 = (int(Load2) * int(app2Hr) * int(appNo2)) / 1000
    return load2


def calculateCategory3Load(cat3, appName3, app3Hr, appNo3):
    df3 = df2[df2['Category'] == cat3]

    Load3 = df3[df3['Appliance'] == appName3]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load3)
    load3 = (int(Load3) * int(app3Hr) * int(appNo3)) / 1000
    return load3


def calculateCategory4Load(cat4, appName4, app4Hr, appNo4):
    df3 = df2[df2['Category'] == cat4]

    Load4 = df3[df3['Appliance'] == appName4]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load4)
    load4 = (int(Load4) * int(app4Hr) * int(appNo4)) / 1000
    return load4


def calculateCategory5Load(cat5, appName5, app5Hr, appNo5):
    df3 = df2[df2['Category'] == cat5]

    Load5 = df3[df3['Appliance'] == appName5]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load5)
    load5 = (int(Load5) * int(app5Hr) * int(appNo5)) / 1000
    return load5


def calculateCategory6Load(cat6, appName6, app6Hr, appNo6):
    df3 = df2[df2['Category'] == cat6]

    Load6 = df3[df3['Appliance'] == appName6]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load6)
    load6 = (int(Load6) * int(app6Hr) * int(appNo6)) / 1000
    return load6


def calculateCategory7Load(cat7, appName7, app7Hr, appNo7):
    df3 = df2[df2['Category'] == cat7]

    Load7 = df3[df3['Appliance'] == appName7]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load7)
    load7 = (int(Load7) * int(app7Hr) * int(appNo7)) / 1000
    return load7