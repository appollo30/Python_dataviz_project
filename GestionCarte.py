import folium

def mapFromationColor(name):
    if name == "2005":
        return 'blue'
    elif name == "2006":
        return 'gold'
    elif name == "2007":
        return 'green'
    elif name == "2008":
        return 'purple'
    elif name == "2009":
        return 'darkred'
    elif name == "2010":
        return 'brown'
    elif name == "2011":
        return 'gray'
    elif name == "2012":
        return 'orange'
    elif name == "2013":
        return 'black'
    elif name == "2014":
        return 'cadetblue'
    elif name == "2015":
        return 'darkgreen'
    elif name == "2016":
        return 'darkblue'
    elif name == "2017":
        return 'beige'
    elif name == "2018":
        return 'lightred'
    elif name == "2019":
        return 'pastel'
    elif name == "2020":
        return 'magenta'
    elif name == "2021":
        return 'pink'
    else:
        return 'crimson'



def mapTouteFormation(dataframe):
    coordsFrance = (46.539758, 2.430331)
    map = folium.Map(location=coordsFrance, tiles='OpenStreetMap', zoom_start=6)
    for i in dataframe.index:
        if(type((dataframe["lat"][i])) == str):
            dataframe["lat"] = dataframe["lat"].replace([dataframe["lat"][i]],dataframe["lat"][i].replace(",","."))
        if(type((dataframe["long"][i])) == str):
            dataframe["long"] = dataframe["long"].replace([dataframe["long"][i]],dataframe["long"][i].replace(",","."))
        folium.CircleMarker(
                    location=(float(dataframe["lat"][i]),
                            float(dataframe["long"][i])),
                    radius=2,
                    color=mapFromationColor(str(dataframe["an"][i])),
                    fill=True,
                    fill_color=mapFromationColor(str(dataframe["an"][i]))
            ).add_to(map)
    return map


def mapByYear(dataframe, year):
    coordsFrance = (46.539758, 2.430331)
    lstName = dataframe[(dataframe["an"] == year)]
    map2 = folium.Map(location=coordsFrance, tiles='OpenStreetMap', zoom_start=6)
    for i in lstName.index:
        if(type((dataframe["lat"][i])) == str):
            dataframe["lat"] = dataframe["lat"].replace([dataframe["lat"][i]],dataframe["lat"][i].replace(",","."))
        if(type((dataframe["long"][i])) == str):
            dataframe["long"] = dataframe["long"].replace([dataframe["long"][i]],dataframe["long"][i].replace(",","."))
        folium.CircleMarker(
            location=(float(dataframe["lat"][i]),
                            float(dataframe["long"][i])),
            radius=2,
            color=mapFromationColor(str(dataframe["an"][i])),
            fill=True,
            fill_color=mapFromationColor(str(dataframe["an"][i]))
        ).add_to(map2)
    return map2


def createAllMaps(dataframe):
    lstYearData = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    for year in lstYearData:
        map = mapByYear(dataframe, year)
        map.save("./templates/MapYears{}.html".format(year))
    map = mapTouteFormation(dataframe)
    map.save("./templates/MapAllYears.html")
