#!/usr/bin/env python
print('hello')
import meetup.api
import pdb
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

# client = meetup.api.Client()
# client.api_key = '5f4d182652662a6844781035a77375f'
# categories_obj = client.GetCategories()
# categories = categories_obj.results
# pprint(categories)
# events = client.GetOpenEvents(False,category=1,status="past",page=100,offset=0)
#
# events_df = pd.DataFrame(events.results)
# events_df.to_csv('test_events.csv',encoding='utf-8')

events_df = pd.read_csv('test_events.csv')

events_array = events_df.as_matrix(columns=['duration','yes_rsvp_count'])
kmeans = KMeans(n_clusters=10, random_state=0).fit(events_array)

plt.plot(events_array)
plt.show()

pdb.set_trace()
