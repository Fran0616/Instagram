pip install instaloader #imput the module, provides us with an API for scraping instagram
import instaloader
# Create an instance of Instaloader class
bot = instaloader.Instaloader() #Instaloader is a tool to download pictures (or videos) along with their captions and other metadata from Instagram.
# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'justinbieber')
print(type(profile))
print("Username: ", profile.username) #print username
print("User ID: ", profile.userid) #print userid
print("Number of Posts: ", profile.mediacount) # number of post
print("Followers: ", profile.followers) #number of followers
print("Followees: ", profile.followees) #people following you count
print("Bio: ", profile.biography,profile.external_url) #bio info


Output
#<class 'instaloader.structures.Profile'>
#Username:  justinbieber
#User ID:  6860189
#Number of Posts:  7403
#Followers:  281319318
#Followees:  736
#Bio:  JUSTICE the album out now
#@drewhouse @inbetweenersnft https://justinbieber.lnk.to/honest/
