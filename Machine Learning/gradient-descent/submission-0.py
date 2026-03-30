class Solution:
    def get_minimizer(self, i: int, alpha: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = init
        for _ in range(i):
            der = 2*x
            x = x - alpha * der
        return round(x,5)
        pass
