import pandas as pd
import math

df = pd.read_csv('electricity - Sheet1.csv')
df2 = pd.read_csv('appliances - Sheet1.csv')
dfaq = pd.read_csv('ELECTRICITY CONSUMPTION AND BILLING APPLICATION - FAQ.csv')


def calculatecategory1load(cat1, appName1, app1Hr, appNo1):
    df3 = df2[df2['Category'] == cat1]

    Load = df3[df3['Appliance'] == appName1]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load)
    load = (int(Load) * int(app1Hr) * int(appNo1)) / 1000
    return load


def calculatecategory2load(cat2, appName2, app2Hr, appNo2):
    df3 = df2[df2['Category'] == cat2]

    Load2 = df3[df3['Appliance'] == appName2]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load2)
    load2 = (int(Load2) * int(app2Hr) * int(appNo2)) / 1000
    return load2


def calculatecategory3load(cat3, appName3, app3Hr, appNo3):
    df3 = df2[df2['Category'] == cat3]

    Load3 = df3[df3['Appliance'] == appName3]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load3)
    load3 = (int(Load3) * int(app3Hr) * int(appNo3)) / 1000
    return load3


def calculatecategory4load(cat4, appName4, app4Hr, appNo4):
    df3 = df2[df2['Category'] == cat4]

    Load4 = df3[df3['Appliance'] == appName4]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load4)
    load4 = (int(Load4) * int(app4Hr) * int(appNo4)) / 1000
    return load4


def calculatecategory5load(cat5, appName5, app5Hr, appNo5):
    df3 = df2[df2['Category'] == cat5]

    Load5 = df3[df3['Appliance'] == appName5]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load5)
    load5 = (int(Load5) * int(app5Hr) * int(appNo5)) / 1000
    return load5


def calculatecategory6load(cat6, appName6, app6Hr, appNo6):
    df3 = df2[df2['Category'] == cat6]

    Load6 = df3[df3['Appliance'] == appName6]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load6)
    load6 = (int(Load6) * int(app6Hr) * int(appNo6)) / 1000
    return load6


def calculatecategory7load(cat7, appName7, app7Hr, appNo7):
    df3 = df2[df2['Category'] == cat7]

    Load7 = df3[df3['Appliance'] == appName7]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load7)
    load7 = (int(Load7) * int(app7Hr) * int(appNo7)) / 1000
    return load7


def calculatecategory8load(cat8, appName8, app8Hr, appNo8):
    df3 = df2[df2['Category'] == cat8]

    Load8 = df3[df3['Appliance'] == appName8]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print(Load8)
    load8 = (int(Load8) * int(app8Hr) * int(appNo8)) / 1000
    return load8


def calculatecategory9load(cat9, appName9, app9Hr, appNo9):
    df3 = df2[df2['Category'] == cat9]

    Load9 = df3[df3['Appliance'] == appName9]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print("Load 9 is : ", Load9)
    load9 = (int(Load9) * int(app9Hr) * int(appNo9)) / 1000
    return load9


def calculatecategory10load(cat10, appName10, app10Hr, appNo10):
    df3 = df2[df2['Category'] == cat10]

    Load10 = df3[df3['Appliance'] == appName10]['Standard Load (Watts)'].reset_index(drop=True)[0]
    print("Load 10 is: ", Load10)
    load10 = (int(Load10) * int(app10Hr) * int(appNo10)) / 1000
    return load10


def calculateTotalUnits(monthly_estimate, unitRate):
    totalUnits = round(monthly_estimate / unitRate, 2)
    print("total unit is ", totalUnits)
    return totalUnits


def calculateUsage(units, total_load):
    # round down to the nearest whole number
    usage = math.floor((units / total_load))
    print('usage ', usage)
    return usage
