#!/usr/bin/env python3.10
import discord_scripts as disc
import datetime as dt
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

melvor_server = ""  # redacted

headers = {
	"Authorization": ""  # redacted
}


if __name__ == "__main__":
	members = disc.get_member_list(server_id=melvor_server, headers=headers)
	join_times = disc.get_join_dates(members, server_id=melvor_server, headers=headers)
	join_dates = list( dt.datetime.strptime(t[:10], "%Y-%m-%d") for t in join_times )

	t_0 = dt.datetime(2020, 1, 1)
	t_1 = dt.datetime.now()
	t_dates = np.array([ t_0 + dt.timedelta(days=i) for i in range((t_1-t_0).days) ])
	j_dates = np.cumsum([ join_dates.count(d) for d in t_dates ], dtype=np.double)

	plt.scatter(t_dates, j_dates) 
	plt.show()

