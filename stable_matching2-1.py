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

def stable_matching(ad_preference, viewer_preference):
    # Initialize all viewers and ads as free
    free_ads = list(ad_preference.keys())
    viewer_partner = {}

    # While there are free ads
    while free_ads:
        # Pick an arbitrary free ad
        ad = free_ads[0]
        # Get the list of viewers that this ad prefers
        ad_prefers = ad_preference[ad]

        # Iterate over the ad's preference list
        #  the proposals are made by the ads. This is evident in the loop where the algorithm iterates 
        # over each free ad and checks its most preferred viewer.
        for viewer in ad_prefers:
            # If the viewer is free, pair them with the ad and remove the ad from the free list
            if viewer not in viewer_partner:
                viewer_partner[viewer] = ad
                free_ads.remove(ad)
                break
            else:
                # If the viewer is not free, check if they prefer the new ad over their current partner
                current_partner = viewer_partner[viewer]
                if viewer_preference[viewer].index(ad) < viewer_preference[viewer].index(current_partner):
                    # If they do, unpair the viewer and their current partner and pair the viewer with the new ad
                    viewer_partner[viewer] = ad
                    free_ads.remove(ad)
                    free_ads.append(current_partner)
                    break

    return viewer_partner

stable_match = stable_matching(ad_rank_viewers, viewer_rank_ads)
print(f'Stable matching: {stable_match}')

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

ad_preference = {0: [3, 1, 2, 4], 1: [2, 3, 1, 4], 2: [3, 1, 2, 4], 3: [2, 3, 1, 4]}
viewer_preference = {0: [4, 5, 6, 7], 1: [5, 4, 6, 7], 2: [6, 4, 5, 7], 3: [5, 7, 4, 6]}


# Convert dictionaries to lists
ad_preference_list = [ad_preference[i] for i in sorted(ad_preference.keys())]
viewer_preference_list = [viewer_preference[i] for i in sorted(viewer_preference.keys())]

print("Ad Preference List:", ad_preference_list)
print("Viewer Preference List:", viewer_preference_list)