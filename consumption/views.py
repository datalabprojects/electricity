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
