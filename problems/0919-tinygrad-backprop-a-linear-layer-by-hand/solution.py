from tinygrad import Tensor

def linear_backward(grad_output, x, W):
    # TODO: return (grad_input, grad_W, grad_b) for y = x @ W.T + b
    grad_input = grad_output @ W # --> (N, in)
    grad_W = grad_output.T @ x # --> (out, in)
    grad_b = grad_output.sum(axis=0) # --> (out,)

    return grad_input, grad_W, grad_b
