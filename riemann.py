import matplotlib.pyplot as plt

def riemann_sum(lower:float, upper:float,delta:int, func) -> float:
    dx = (upper - lower)/delta
    midpoint_delta = dx / 2
    
    riemann_sum_output = 0
    
    for i in range(delta):
        midpoint = lower + (i * dx) + midpoint_delta
        y_delta = func(midpoint)
        riemann_sum_output += (y_delta * dx)

    return riemann_sum_output

if __name__ == '__main__':
    lower = 0
    upper = 10
    delta = 100
    func = lambda x: x * x * x
    output_list = []

    for i in range(5, delta):
        output_list.append(riemann_sum(lower, upper, i, func))

    actual_value = 2500
    output_errors = [abs((i - actual_value)/actual_value) * 100 for i in output_list]
    
    output_indices = list(range(1, len(output_list) + 1))

    plt.figure(figsize=(10, 5))
    plt.plot(output_indices, output_errors)

    plt.title("Riemann Sum - Error Analysis (5 to 100 intervals)")
    plt.xlabel("Riemann Sum - Number of Intervals")
    plt.ylabel("Riemann Sum - Error Rate from Definite Integral (%)")

    plt.grid(True)
    plt.legend()
    plt.savefig("output_illustration.png", dpi=300)
