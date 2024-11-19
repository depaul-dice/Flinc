import pandas as pd    # Pandas is used for data frames

# Function to read a tab delimited USGS streamflow file obtained from https://waterdata.usgs.gov/nwis/
def read_usgs_streamflow_file(filename):

    file=open(filename,"r")
    # Skip the first 30 lines of header
    for i in range(30):
        file.readline()
    dates=[]
    flows=[]
    while True:
        line=file.readline()
        if len(line)==0:
            break
        words=line.split()
        dates.append(words[2])
        flows.append(float(words[3]))

    flowdata=pd.DataFrame(data={'date': dates,'flow': flows})
    flowdata['date']=pd.to_datetime(flowdata['date'])
    return flowdata

import urllib.request  # To retrieve data from the internet

# Function to read data from a snotel site
def read_snotel(id,state,enddate):
# See https://wcc.sc.egov.usda.gov/reportGenerator/ to figure out how to construct the URL below

    st1="https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/customMultiTimeSeriesGroupByStationReport/daily/start_of_period/"
    st2=":SNTL|id=%22%22|name/1972-05-01,"
    st3="/stationId,name,WTEQ::value"
    url=st1+str(id)+":"+state+st2+enddate+st3

    urllib.request.urlretrieve(url,"snotel.txt")
    snow=pd.read_csv("snotel.txt",skiprows=60,names=["date","swe"])
    snow['date']=pd.to_datetime(snow['date'])
    return snow
