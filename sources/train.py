import sys
import pandas as pd

DATA_PATH = "includes/data.csv"
MAX_DEPTH = 10
LERNING_RATE = 0.01

def compute_t0(data: pd.DataFrame, t0: float, t1: float) -> float:
	"""
	Temporary docstring.
	"""
	data_length: int = data.shape[0]
	derivated_mse_sum: float = sum([
		t1 * x["km"] + t0 - x["price"]
		for _, x in data.iterrows()
	])
	derivated_mse: float = 1 / data_length * derivated_mse_sum
	return LERNING_RATE * derivated_mse

def compute_t1(data: pd.DataFrame, t0: float, t1: float) -> float:
	"""
	Temporary docstring.
	"""
	data_length: int = data.shape[0]
	derivated_mse_sum: float = sum([
		(t1 * x["km"] + t0 - x["price"]) * x["km"]
		for _, x in data.iterrows()
	])
	derivated_mse: float = 1 / data_length * derivated_mse_sum
	return LERNING_RATE * derivated_mse

def main():
	"""
	Temporary docstring.
	"""
	try:
		t0: float = 0
		t1: float = 0
		data = pd.read_csv(DATA_PATH)
		for _ in range(MAX_DEPTH):
			t0_holder = compute_t0(data, t0, t1)
			t1_holder = compute_t1(data, t0, t1)
			t0 = t0_holder
			t1 = t1_holder
		print(f"{t1:.2f}x + {t0:.2f}")
	except Exception as error:
		print("Error:", error, file=sys.stderr)
		sys.exit(1)


if __name__ == "__main__":
	main()
