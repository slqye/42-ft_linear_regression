# ft_linear_regression

Hi! This is my 42 cursus project, ft_linear_regression.
The objective was to implement the gradient descent algorithm from scratch and use it to train a linear regression model that predict a car price based on its mileage.

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

The first step is to define our loss function. Here i am using the MSE definition.

> [!NOTE]
> The factor $\frac{1}{2n}$ is used instead of $\frac{1}{n}$ to simplify the gradient calculation..

$f(x) = \frac{1}{2n} \sum_{i=0}^n (a \cdot mileage(i) + b - price(i))^2$

Now that we have the loss function we need to take the partial derivative of `a` and `b` because we want to calculate the gradient of the loss function to minimise it.
To help with calculations i will define: $u = a \cdot mileage(i) + b - price(i)$

$\frac{\partial f}{\partial a} = 2 \cdot \frac{1}{2n} \sum_{i=0}^n uu'$

$\frac{\partial f}{\partial a} = \frac{1}{n} \sum_{i=0}^n a \cdot mileage(i) + b - price(i) * mileage(i)$

$\frac{\partial f}{\partial b} = 2 \cdot \frac{1}{2n} \sum_{i=0}^n uu'$

$\frac{\partial f}{\partial b} = \frac{1}{n} \sum_{i=0}^n a \cdot mileage(i) + b - price(i)$
