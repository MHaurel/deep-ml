import torch

def grad_of_quadratic(x_value: float) -> float:
    # TODO: build a tracked leaf for x, compute f(x), run backprop, return df/dx as a float
    x_tensor = torch.tensor(x_value, requires_grad=True)
    f_x = x_tensor**2 + 3*x_tensor + 2
    f_x.backward()
    return x_tensor.grad.item()
