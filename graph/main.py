import pandas as pd

if __name__=="__main__":
    joins = pd.read_csv("data/join.csv")
    companys = pd.read_csv("data/company.csv")
    lines = pd.read_csv("data/line.csv")
    stations = pd.read_csv("data/station.csv")
    
    stid = stations["station_cd"]
    n = len(stations)
    print(n)
    