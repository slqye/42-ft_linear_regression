import sys
import pandas as pd

DATASET_PATH = "includes/data.csv"
MAX_DEPTH = 1000
MIN_STEP = 0.0001
LEARNING_RATE = 0.1

def normalize_dataset(dataset: pd.DataFrame) -> None:
	"""
	Temporary docstring.
	"""
	for column in dataset.columns:
		values = dataset[column]
		dataset[column] = (values - values.min()) / (values.max() - values.min())

def compute_t0_step(dataset: pd.DataFrame, t0: float, t1: float) -> float:
	"""
	Temporary docstring.
	"""
	data_length: int = dataset.shape[0]
	derivated_mse_sum: float = sum([
		(t1 * x["km"] + t0) - x["price"]
		for _, x in dataset.iterrows()
	])
	derivated_mse: float = 1 / data_length * derivated_mse_sum
	return LEARNING_RATE * derivated_mse

def compute_t1_step(dataset: pd.DataFrame, t0: float, t1: float) -> float:
	"""
	Temporary docstring.
	"""
	data_length: int = dataset.shape[0]
	derivated_mse_sum: float = sum([
		((t1 * x["km"] + t0) - x["price"]) * x["km"]
		for _, x in dataset.iterrows()
	])
	derivated_mse: float = 1 / data_length * derivated_mse_sum
	return LEARNING_RATE * derivated_mse

def output_result(t0: float, t1: float) -> None:
	"""
	Temporary docstring.
	"""
	with open("training.out", "w", encoding="utf-8") as file:
		file.write(f"{str(t1)}\n{str(t0)}")

def main():
	"""
	Temporary docstring.
	"""
	try:
		t0: float = 0
		t1: float = 0
		dataset: pd.DataFrame = pd.read_csv(DATASET_PATH)
		dataset_min: list[float] = [dataset[x].min() for x in dataset.columns]
		dataset_max: list[float] = [dataset[x].max() for x in dataset.columns]
		normalize_dataset(dataset)
		for _ in range(MAX_DEPTH):
			t0_step = compute_t0_step(dataset, t0, t1)
			t1_step = compute_t1_step(dataset, t0, t1)
			if abs(t0_step) <= MIN_STEP and abs(t1_step) <= MIN_STEP:
				break
			t0 -= t0_step
			t1 -= t1_step
		t1_holder = (t1 * (dataset_max[1] - dataset_min[1])) / (dataset_max[0] - dataset_min[0])
		t0_holder = t0 * (dataset_max[1] - dataset_min[1]) + dataset_min[1] - t1_holder * dataset_min[0]
		t0, t1 = t0_holder, t1_holder
		output_result(t0, t1)
	except Exception as error:
		print("Error:", error, file=sys.stderr)
		sys.exit(1)


if __name__ == "__main__":
	main()
