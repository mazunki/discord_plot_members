#!/usr/bin/env python3
import requests as req

def get_member_list(server_id, headers):
	query = f"https://discord.com/api/v9/guilds/{server_id}/members"
	response = req.get(query, headers=headers)
	if response.status_code != 200:
		return
	res_json = response.json()

	for key, value in res_json.items():
		yield value


def get_member_join_dates(server_id, headers):
	query = f"https://discord.com/api/v9/guilds/{server_id}/members"
	response = req.get(query, headers=headers)
	if response.status_code != 200:
		return
	res_json = response.json()

	for member in res_json():
		if (joined := member.get("joined_at", None)):
			yield dt.datetime.strptime(joined[:10], "%Y-%m-%d")
 

def get_join_dates(user_ids, server_id, headers):
	for user_id in user_ids:
		query = f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&guild_id={server_id}"
		response = req.get(query, headers=headers)
		if not response.ok:
			print(f"failure on {user_id}")
			continue
		res_json = response.json()
		if (gm := res_json.get("guild_member", None)):
			yield gm.get("joined_at", "unknown")

