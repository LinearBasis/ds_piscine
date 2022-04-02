import os

import pandas as pd

positions = ("Junior", "Middle", "Senior")
def	cut_positions(descr : str) -> str:
	found_words = []
	for i in positions:
		if descr.lower().find(i.lower()) != -1:
			found_words.append(i)
	ans = ""
	for i in found_words:
		if ans != "":
			ans += "/"
		ans += i
	if ans == "":
		ans = "-"
	return ans

df = pd.read_csv("../ex02/hh_sorted.csv")
df.to_csv("", index=False)
