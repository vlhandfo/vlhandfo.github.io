from pathlib import Path
import pandas as pd

class Results:
	def __init__(self, file: str | Path) -> None:
		file = Path(file)
		assert file.suffix == ".csv", "Results requires a .csv-file"

		self._df = pd.read_csv(file, index_col="Unnamed: 0")


	def get_results_by_country(self, n: int) -> dict:
		subset = self._df.iloc[:n]
		res = {}
		for _, row in subset.iterrows():
			res[row["Country"]] = res.get(row["Country"], 0) + 1
		return res


	def top_n(self, n: int) -> pd.DataFrame:
		assert n in range(0, len(self._df)), "Invalid number"
		return self._df.iloc[:n]
	

	def countries(self) -> list:
		return set(self._df["Country"])

if __name__ == "__main__":
	# Messing around with functionalities
	r = Results("data-processing/WJPC2023/individuals/results/2023-World_individual-finals.csv")
	print(r.get_results_by_country(10))