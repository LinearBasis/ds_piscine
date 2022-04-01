import os

import pandas as pd

positions = ("junior", "middle", "senior")
def	cut_positions(descr : str) -> str:
	found_words = []
	for i in positions:
		if descr.lower().find(i) != -1:
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
print(df["name"].apply(cut_positions))
