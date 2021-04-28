from covid import Covid
from fastapi import FastAPI

app = FastAPI()

covid = Covid(source="worldometers")

#Total Page Route
active = "{:,}".format(covid.get_total_active_cases())
confirmed = "{:,}".format(covid.get_total_confirmed_cases())
recovered = "{:,}".format(covid.get_total_recovered())
deaths = "{:,}".format(covid.get_total_deaths())

#India Data
ind_cases = covid.get_status_by_country_name("india")
#Route 
@app.get("/")
async def root():
    return { "status" : "Working" ,
             "follow" : "github.com/gourab28"
           }
    
@app.get("/world")
async def root():
    return {"active_cases" : active ,
            "confirmed" : confirmed ,
            "recovered" : recovered ,
            "deaths" : deaths ,
            }
            
@app.get("/india")
async def root():
  return ind_cases