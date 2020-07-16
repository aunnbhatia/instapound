from instabot import Bot
from getpass import getpass
from pprint import pprint
import time
_version = "@1.0.0"
_author = "aunn Bhatia"
_starttime = time.strftime("%r")
print('InstaPound {} ~by{} \n started:--> {}'.format(_version,_author,_starttime))

un,ps = input("@"), getpass("Password: ")
bot = Bot()
bot.login(username = un, password = ps)

def get_uname(uid):
	return bot.get_username_from_user_id(uid)
def get_name(uid):
	return bot.get_user_info(uid)["full_name"]
def get_uid(uname):
	return bot.get_user_id_from_username(uname)
def get_info(uname,opt):
	uid = get_uid(uname)
	# Get User's Basic Info
	if opt == 1:
		basicInfo = bot.get_user_info(uid)
		userInfo = {
			'pk' : basicInfo["pk"],
			'username' : basicInfo["username"],
			'fullName' : basicInfo["full_name"],
			'mediaCount' : basicInfo["media_count"],
			'followerCount' : basicInfo["follower_count"],
			'followingCount' : basicInfo["following_count"],
			'bio' : basicInfo["biography"],
			'isPrivate' : basicInfo["is_private"],
			'isVerified': basicInfo["is_verified"]
			}
		pprint(userInfo)
	# Get User's Followers and Following
	if opt == 2:
		followers_id_list = bot.get_user_followers(get_uid(uname))
		following_id_list = bot.get_user_following(get_uid(uname))
		#Followers Attempt
		print("\n\n\nFollowers Details")
		print("(.) -->  Username    |	Full Name")
		index1 = 1
		for Follower_id in followers_id_list:
			try:
				print("({}) -->  {}	|	{}".format(index1 ,get_uname(Follower_id),get_name(Follower_id) ))
			except:
				print("({})Failed at {}".format(index1, Follower_id))
			index1 +=1
		time.sleep(5)
		#Following Attempt
		index2 = 2
		print('\n\n\nFollowing Details')
		print("(.) -->  Username    |	Full Name")
		for Following_id in following_id_list:
			try:
				print("({}) -->  {}	|	{}".format(index2 ,get_uname(Following_id),get_name(Following_id) ))
			except:
				print("({})Failed at {}".format(index2, Following_id))
			index2 +=1

username1 = input("Username: ")
op = input("Click (1) for Basic info, and (2) for Followers and Followings: ")
get_uid(username1)
if '1' in op:
	get_info(username1,1)
if '2' in op :
	get_info(username1,2)

time.sleep(5)