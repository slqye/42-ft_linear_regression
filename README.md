![Banner](assets/banner.png)

Hi! This is my 42 cursus project, ft_linear_regression. The objective was to implement the gradient descent algorithm from scratch and use it to train a model.

## Usage

> [!NOTE]
> To run the program from source, you need to have `uv` installed on your system.
> https://docs.astral.sh/uv/getting-started/installation/

To train the model
```bash
uv run sources/train.py
```

To make predictions
```bash
uv run sources/predict.py
```

To plot the model
```bash
uv run sources/bonus.py
```

## Explanations

First we need to define the loss function, here i'm using the MSE definition
$$
f(x) = \frac{1}{n}\sum_{i=0}^n (a \cdot \text{mileage}(x) + b - \text{price}(x))^{2}
$$
