#!/usr/bin/env python
print('hello')
import meetup.api
import pdb
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

def get_meetup_client():
    client = meetup.api.Client()
    client.api_key = '5f4d182652662a6844781035a77375f'
    return client

def print_meetup_categories(client):
    categories_obj = client.GetCategories()
    categories = categories_obj.results
    pprint(categories)

def get_open_events(client):
    events = client.GetOpenEvents(False,category=1,status="past",page=100,offset=0)
    events_df = pd.DataFrame(events.results)
    events_df =events_df[np.isfinite(events_df['duration'])]
    return events_df

def cluster (events_df):
    events_array = events_df.as_matrix(columns=['duration','yes_rsvp_count'])
    kmeans_result = KMeans(n_clusters=10, random_state=0).fit(events_array)
    return events_array,kmeans_result

def plot_clusters(events_array):
    plt.plot(events_array)
    plt.show()

def read_csv (file_name):
    events_df.to_csv(file_name,encoding='utf-8')

def write_csv (file_name):
    events_df = pd.read_csv(file_name)

def main():
    client = get_meetup_client()
    print_meetup_categories(client)
    events_df = get_open_events(client)
    events_array, kmeans = cluster(events_df)
    plot_clusters(events_array)
    pdb.set_trace()

main()
