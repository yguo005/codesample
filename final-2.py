# CS 5002 Final Project Matching ads and viewers
# 04/12/2023 Yunyu Guo

import pandas as pd


viewers = pd.read_csv('viewers.csv')
ads = pd.read_csv('ads.csv')
# how well the viewers match the advertiser's needs
def rank_viewers(ad, viewers):
    ad_id = ad['AdId'].values[0]
    # get the row from the ads.csv file
    ad_row = ad.loc[ad['AdId'] == ad_id]

    # create new column Score in viewers data
    # increment score when attributes match
    # conditions: age between 25 to 40, score +1; 
    # target daily internet usage between 3 to 4, score +1; 
    # targetgender = gender, score +1; 
    # target income between 40000 to 75000, score + 1
    viewers['Score'] = 0
    viewers.loc[(viewers['Age'] >=25) & (viewers['Age'] <= 40), 'Score'] += 1
    viewers.loc[(viewers['DailyInternetUsage'] >= 3) & (viewers['DailyInternetUsage'] <= 4), 'Score'] += 1
    viewers.loc[viewers['Gender'] == ad_row['TargetGender'].values[0],'Score'] += 1
    viewers.loc[(viewers['Income'] >= 40_000) & (viewers['Income'] <= 75_000),'Score'] += 1

    # rank viewers based on score
    ad_sorted_viewers = viewers.sort_values('Score', ascending=False)
    # return a list of viewer IDs from most to least compatible
    return ad_sorted_viewers['ViewerId'].tolist()

# choose ad id 3 to rank the viewers
chose_ad = ads.loc[ads['AdId'] == 3]
ad3_rank_viewers = rank_viewers(chose_ad, viewers)
print(f" Ad3's rankings of viewers: {ad3_rank_viewers}")

# how well the ads match the viewer’s preferences
# The conditions are: target age between 3 to 13, score + 1; 
# targe travel = travel, score + 1; 
# targe gender = gender, score +1; 
# TargetCar = car, score +1; 
# target kid > = 2, score +1.
def rank_ads(viewer, ads):
    viewer_id = viewer['ViewerId'].values[0]
    viewer_row = viewer.loc[viewer['ViewerId'] == viewer_id]

    ads['Score'] = 0
    ads.loc[(ads['TargetAge'] >= 3) & (ads['TargetAge'] <= 13), 'Score'] += 1
    ads.loc[ads['TargetTravel'] == viewer_row['Travel'].values[0], 'Score'] += 1
    ads.loc[ads['TargetGender'] == viewer_row['Gender'].values[0], 'Score'] += 1
    ads.loc[ads['TargetCar'] == viewer_row['Car'].values[0],'Score'] += 1
    ads.loc[ads['TargetKid'] >= 2, 'Score'] += 1

    ads = ads.sort_values('Score', ascending=False)
    return ads['AdId'].tolist()

# choose viewer id 2 to rank ads
chose_viewer = viewers.loc[viewers['ViewerId'] == 2]
# rank ads based on the selected viewer preferences
viewer2_rank_ads = rank_ads(chose_viewer, ads)
print(f" Viewer2's rankings of ads: {viewer2_rank_ads}")

# create rankings for each ad
ad_rank_viewers = {ad_id: rank_viewers(ads.loc[ads['AdId'] == ad_id], viewers) for ad_id in ads['AdId']}
print(f'ad_preference: {ad_rank_viewers}')
# create rankings for each viewer
viewer_rank_ads = {viewer_id: rank_ads(viewers.loc[viewers['ViewerId'] == viewer_id], ads) for viewer_id in viewers['ViewerId']}
print(f'viewer_prefernence: {viewer_rank_ads}')



# use stable match to match ads and viewers
N = 4
 
# This function returns true if 
# viewer 'v' prefers ad 'a1' over ad 'a'
def viewer_prefera1_overA(prefer, v, a, a1):
     
    # Check if v prefers a over their 
    # current match a1
    for i in range(N):
         
        # If a1 comes before a in list of v, 
        # then v prefers their current match,
        # don't do anything
        # extracts the i-th preference of viewer v from the preference list
        if (prefer[v][i] == a1):
            return True
 
        # If a comes before a1 in v's list, 
        # then free viewer's current match 
        # and match viewer with a
        if (prefer[v][i] == a):
            return False
 
# Prints stable matching for N ads and N viewers
# ads are numbered as 0 to N-1. 
# viewers are numbered as N to 2N-1.
def stableMatch(prefer):
     
    # Stores matching of viewer. This is our output 
    # array that stores passing information. 
    # The value of vPair[i] indicates the ad 
    # assigned to viewer N+i. Note that the viewer numbers 
    # between N and 2*N-1. The value -1 indicates 
    # that (N+i)'th viewer is free
    vPair = [-1 for i in range(N)]
 
    # An array to store availability of ads. 
    # If aFree[i] is false, then ad 'i' is free,
    # otherwise match.
    aFree = [False for i in range(N)]
 
    freeCount = N
 
    # While there are free ads
    while (freeCount > 0):
         
        # Pick the first free ad (we could pick any)
        # aFree[a] is False, it means that ad a is free.
        a = 0
        while (a < N):
            if (aFree[a] == False):
                break
            a += 1
 
        # One by one go to all viewer according to 
        # ad's preferences. Here ad is the picked free ad
        # prefer[a] gives the list of preferences for ad a. The value at index i represents the viewer v
        i = 0
        while i < N and aFree[a] == False:
            v = prefer[a][i]
 
            # The viewer of preference is free, 
            # v and a become matched (Note that 
            # the match maybe changed later). 
            #  vPair[v - N] == -1 it checks if the viewer v is currently unassigned
            # viewer indices are typically represented by numbers starting from N and going up to 2N-1next N indices are used for viewers.
            # vPair[v - N] = a
            # vPair[v - N] = a This line updates the vPair list to assign ad a to viewer v
            if (vPair[v - N] == -1):
                vPair[v - N] = a
                aFree[a] = True
                freeCount -= 1
 
            else: 
                 
                # If v is not free
                # Find current match of v
                a1 = vPair[v - N]
 
                # If v prefers a over current match a1,
                # then break the match between v and a1 and
                # math a with v.
                if (viewer_prefera1_overA(prefer, v, a, a1) == False):
                    vPair[v - N] = a
                    aFree[a] = True
                    # updates the aFree list to indicate that the ad a is no longer free. 
                    aFree[a1] = False
            i += 1
            # move to the next preference of viewer v
 
           
   
    print("Viewer", "Ad")
    for i in range(N):
        print(i + N, "\t", vPair[i])
 


def main():
#create viewers data
    viewers = pd.DataFrame({
        'ViewerId': [1, 2, 3, 4],
        'Age': [22, 35, 42, 60],
        'DailyInternetUsage': [2, 5, 4, 1],
        'Gender': ['Female', 'Male', 'Female', 'Male'],
        'Income': [45000, 60000, 75000, 25000],
        'Travel': ['America', 'Asia', 'Europe','Africa'],
        'Car': ['Sport','SUV','Minivan','Sedan']
        })
    viewers.to_csv('viewers.csv', index=False)

# create ads data
    ads = pd.DataFrame({
        'AdId': [1, 2, 3, 4],
        'TargetAge': [5, 12, 25, 60],
        'TargetGender': ['Female', 'Male', 'Female', 'Male'],
        'TargetTravel': ['Asia', 'America', 'Europe','Africa'],
        'TargetCar':['Sport','Sedan','SUV','Minivan'],
        'TargetKid': [1, 2, 3, 4]
        })
    ads.to_csv('ads.csv', index=False)

# the ad preference: {1: [3, 1, 2, 4], 2: [2, 3, 1, 4], 3: [3, 1, 2, 4], 4: [2, 3, 1, 4]}
# the viewer preference: {1: [1, 2, 3, 4], 2: [2, 1, 3, 4], 3: [3, 1, 2, 4], 4: [2, 4, 1, 3]}
# the first 4 sublists represent the preferences of 4 ads (numbered 0 to 3)
# the last four sublists represent the preferences of 4 viewers (numbered 4 to 7)
prefer = [[2, 0, 1, 3], [1, 2, 0, 3],
          [2, 0, 1, 3], [1, 2, 0, 3],
          [4, 5, 6, 7], [5, 4, 6, 7],
          [6, 4, 5, 7], [5, 7, 4, 6]]

 
stableMatch(prefer)
        

  

if __name__ == "__main__":
    main()

