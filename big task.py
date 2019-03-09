######################################################################
##Task to find location of 5 rescue points

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

DATA_FILE = 'tz.csv'

##########################reading from file
df = pd.read_csv(DATA_FILE)
print(df.shape)

##############################filtering the data
a = df[df['title'].str.contains("EMS")]

#############################plotting the data
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.set_title('EMS cases without filtering')
ax.scatter(x=a["lat"],y=a["lng"],label='EMS cases ',color= 'red')
ax.set_xlabel('latitude')
ax.set_ylabel('longitude')
ax.legend(loc='best')
plt.show()

############################eliminating the noise and false reading
meanx = a["lat"].mean()
meany = a["lng"].mean()
stdx = a['lat'].std()
stdy = a['lng'].std()

print(a.shape)
c = a.loc[(a['lat'] >= meanx-3*stdx) & (a['lat'] <= meanx+3*stdx)]
d = c.loc[(c['lng'] >= meany-3*stdy) & (c['lng'] <= meany+3*stdy)]

print(d.shape)
cor = d[["lat" ,"lng"]]

x = cor["lat"]
y = cor["lng"]

print('max and min x is  ',min(x),'    ',max(x))
print('max and min y is  ',min(y),'    ',max(y))


###################################### using clustering algorithm
X = cor
kmeans = KMeans(n_clusters=5, random_state=0,n_init=10, max_iter= 300,precompute_distances = True).fit(X)
print(kmeans.cluster_centers_)

######################### potting emergencyy cases
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.set_title('EMS cases with filteration')
ax.scatter(x=x,y=y,label='EMS cases ',color= 'red')
ax.set_xlabel('latitude')
ax.set_ylabel('longitude')
ax.legend(loc='best')
plt.show()

#########################plotting rescue station with EMS cases
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.set_title('rescue station and EMS cases')
ax.scatter(x=x,y=y,label='EMS cases ',color= 'red')
ax.scatter(x=kmeans.cluster_centers_[:,0],y=kmeans.cluster_centers_[:,1],label='Rescue station')
ax.set_xlabel('latitude')
ax.set_ylabel('longitude')
ax.legend(loc='best')
plt.show()
