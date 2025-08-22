# ft_linear_regression

Hi! This is my 42 cursus project, [ft_linear_regression](assets/subject.pdf).
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

The first step is to define our loss function. Here, I am using the Mean Squared Error (MSE) definition.

> [!NOTE]
> The factor $\frac{1}{2n}$ is used instead of $\frac{1}{n}$ to simplify the gradient calculation.

$$
f(x) = \frac{1}{2n} \sum_{i=0}^{n-1} (a \cdot mileage(i) + b - price(i))^2
$$

Now that we have the loss function, we need to compute the partial derivatives with respect to `a` and `b` in order to calculate the gradient and minimize the loss.
$$
u_i = a \cdot mileage(i) + b - price(i)
$$

$$
\frac{\partial f}{\partial a} = 2 \cdot \frac{1}{2n} \sum_{i=0}^{n-1} u_iu_i'
\frac{\partial f}{\partial b} = 2 \cdot \frac{1}{2n} \sum_{i=0}^{n-1} u_iu_i'
$$

$$
\frac{\partial f}{\partial a} = \frac{1}{n} \sum_{i=0}^{n-1} (a \cdot mileage(i) + b - price(i)) \cdot mileage(i)
$$

$$
\frac{\partial f}{\partial b} = \frac{1}{n} \sum_{i=0}^{n-1} a \cdot mileage(i) + b - price(i)
$$

## Result

![Result](assets/result.png)
