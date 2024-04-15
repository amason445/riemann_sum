def riemann_sum(lower:float, upper:float,delta:int, func) -> float:
    dx = (upper - lower)/delta
    midpoint_delta = dx / 2
    
    output = []
    
    for i in range(delta):
        midpoint = lower + (i * dx) + midpoint_delta
        y_delta = func(midpoint)
        output.append(y_delta)

    return sum(output)

if __name__ == '__main__':
    lower = 0
    upper = 10
    delta = 100
    func = lambda x: x * x

    output = riemann_sum(lower, upper, delta, func)

    print(output)
