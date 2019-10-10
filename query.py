import requests
import json
from pprint import pprint
type_fl = list()
temps = list()
response = requests.get('https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets')
input_data = response.json()


#First two requirements are satisfied by running the loop
t = 0
for each in input_data:
    if each["HostStarMassSlrMass"] == "" and each["HostStarRadiusSlrRad"] == "" and each["HostStarMetallicity"] =="" and each["HostStarTempK"] == "" and each["HostStarAgeGyr"] == "":
        t +=1
for each in input_data:
    if each["HostStarTempK"] != "":
        temps.append(int(each["HostStarTempK"]))
    else:
        temps.append(0)

print ("The total number of orphan planets is "+  str(t))
maxi = temps.index(max(temps))
print ("The planet that has the highest temperature is:- "+ input_data[maxi]["PlanetIdentifier"])

years = set()
temp_l = list()
for each in input_data:
    years.add(each["DiscoveryYear"])
for year in years:
    t_l_d =dict()
    t_l_d[year] = list()
    for each in input_data:
        if year == each["DiscoveryYear"]:
            t_l_d[year].append(each["RadiusJpt"])
    temp_l.append(t_l_d)

def groupYear(year):
    small, medium, large = 0 , 0 ,0
    temp_lister = list()
    if year not in years:
        print ("No planet was discovered in this year!")
        return
    for each in temp_l:
        if year in each.keys():
            temp_lister = list(each.values())
    #print (temp_lister)
    for elem in temp_lister[0]:
        if elem == "": pass
        elif int(elem) < 1: small +=1
        elif int(elem) < 2: medium +=1
        else: large +=1
    return small, medium, large

enter_y = input("Please enter the year from " )
trip = groupYear(int(enter_y))

print ("The year has {} small planets {} medium planets and {} large planets".format(trip[0], trip[1], trip[2]))

