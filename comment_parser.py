from pprint import pprint

import praw
import pandas as pd
import numpy as np
reddit=praw.Reddit(
    client_id='<client id here>',
    client_secret='<client secret here',
    user_agent='<user agent name here>',
)
df_subid=pd.read_csv('submission_ids_DD.csv')
first_sub=df_subid.columns[0]
submission=reddit.submission(first_sub)
starting=False
subid=[]
body=[]
id=[]
link_id=[]
parent_id=[]
subreddit=[]
utc=[]
i=0
while i <df_subid.shape[0]:
    if starting:
        sub=df_subid.iat[i,0]
        submission = reddit.submission(sub)
        submission.comments.replace_more(limit=0)
        for top_level_comment in submission.comments:
            subid.append(sub)
            body.append(top_level_comment.body)
            id.append(top_level_comment.id)
            link_id.append(top_level_comment.link_id)
            parent_id.append(top_level_comment.parent_id)
            subreddit.append(top_level_comment.subreddit)
            utc.append(top_level_comment.created_utc)
        i=i+1
        print(i)
    else:
        starting=True
        submission.comments.replace_more(limit=0)
        for top_level_comment in submission.comments:
            subid.append(first_sub)
            body.append(top_level_comment.body)
            id.append(top_level_comment.id)
            link_id.append(top_level_comment.link_id)
            parent_id.append(top_level_comment.parent_id)
            subreddit.append(top_level_comment.subreddit)
            utc.append(top_level_comment.created_utc)

print(len(utc))
data=np.empty([len(utc),7],dtype=object)
data[:,0]=subid
data[:,1]=body
data[:,2]=id
data[:,3]=link_id
data[:,4]=parent_id
data[:,5]=subreddit
data[:,6]=utc
df_popularSub=pd.DataFrame(data,columns=['sub_id','body','id','link_id','parent_id','subreddit','utc'])
df_popularSub.to_csv('DDsubmissions.csv')


