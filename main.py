import requests
from datetime import  datetime
ID="graph1"
USER="xxxxxxxx"
TOKEN="xxx"
pixela_endpoint="https://pixe.la/v1/users"
graph=f"{pixela_endpoint}/{USER}/graphs"

graph_config={
    "id":ID,
     "name":"coding_class",
     "unit":"hours",
     "type":"int",
     "color":"ajisai"
}

date12 =datetime(year=2022,month=2,day=21)
print(date12.strftime("%Y-%m-%d"))

headers={
    "X-USER-TOKEN":TOKEN
}
pixel={
    "date": date12.strftime("%Y%m%d"),
    "quantity":"1"
}
graphs_pixel=f"{graph}/{ID}/{date12.strftime('%Y-%m-%d')}"
response=requests.post(url=graphs_pixel,json=pixel,headers=headers)

