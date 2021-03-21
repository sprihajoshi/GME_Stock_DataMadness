import requests
import json
import requests.auth
import pandas as pd
import time
import numpy as np
client_auth = requests.auth.HTTPBasicAuth('<Add client ID here>', '<Add client secret here>')
post_data = {"grant_type": "password", "username": "<Add Reddit username here", "password": "<Add Reddit password here>"}
headers={"Authorization": "bearer <Insert access token here>","User-Agent": "<Insert name of user-agent here>"}

#Function to search wallstreet bets submissions.
def get_data(after,author,score,utc,continuing):
    #Parameters you can find at https://www.reddit.com/dev/api
    response = requests.get("https://oauth.reddit.com/r/wallstreetbets/search", headers=headers,
                            params={"q": "GME OR gamestop", "limit": 100, "sort": 'top',"after":after})
    response_j = response.content.decode("utf-8")
    response_di = json.loads(response_j)
    for i in range(100):
        try:
            author.append(response_di['data']['children'][i]['data']['author_fullname'])
            score.append(response_di['data']['children'][i]['data']['score'])
            utc.append(response_di['data']['children'][i]['data']['created'])
            next = (response_di['data']['after'])
        except:
            continuing=False
            break
    return next,continuing

author_list=[]
score_list=[]
created_list=[]
next=''
j=0
continuing=True
while continuing==True:
    if j==0:
        j=j+1
        response = requests.get("https://oauth.reddit.com/r/wallstreetbets/search", headers=headers,
                                params={"q": "GME OR gamestop", "limit": 100, "sort": "top"})
        response_j = response.content.decode("utf-8")
        response_d = json.loads(response_j)
        for k in range(100):
            try:
                author_list.append(response_d['data']['children'][k]['data']['author_fullname'])
                score_list.append(response_d['data']['children'][k]['data']['score'])
                created_list.append(response_d['data']['children'][k]['data']['created'])
                next = (response_d['data'][k]['after'])
            except:
                break
        time.sleep(1)
    else:
        next,continuing=get_data(next,author_list,score_list,created_list,continuing)
        time.sleep(1)


print(len(created_list))
data=np.empty([len(created_list),3],dtype=object)
data[:,0]=author_list
data[:,1]=score_list
data[:,2]=created_list
df_popularSub=pd.DataFrame(data,columns=['author','score','utc'])
df_popularSub.to_csv('submissions.csv')



