from pyodide.http import pyxhr as requests

url = 'https://football-frenzy.s3.eu-north-1.amazonaws.com/api'


year = input("Enter year: ")
h = int(input("Home score: "))
a = int(input("Away score: "))

season = requests.get(url + "/" + year).json()                                                       

for day in season["gamedays"]:                                                                    
    data = requests.get(url + "/" + year + "/" + day).json()                                
    
    for game in data["games"]:                                                              
        home = game["score"]["home"]                                                       
        away = game["score"]["away"]

        if home["goals"] == h and away["goals"] == a:                                                
            t1 = home["team"].split()[0]                                                         
            t2 = away["team"].split()[0]                                                           

            rad = f"[{day}/{year}] ({h}) {t1} - {t2} ({a})"                                                 
            print(rad.replace("å", "a").replace("ä", "a").replace("ö", "o"))          
            print()
