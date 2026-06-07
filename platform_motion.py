def advance_bouncing_axis(position, velocity, lower_bound, upper_bound, delta_time):
    """Advance one axis and reflect any movement that crosses a bound."""
    if lower_bound > upper_bound:
        raise ValueError("lower_bound must not exceed upper_bound")
    if delta_time < 0:
        raise ValueError("delta_time must not be negative")
    if lower_bound == upper_bound or velocity == 0:
        return lower_bound if lower_bound == upper_bound else position, 0

    position += velocity * delta_time

    while (
        position < lower_bound
        or position > upper_bound
        or (position == lower_bound and velocity < 0)
        or (position == upper_bound and velocity > 0)
    ):
        if position > upper_bound or (position == upper_bound and velocity > 0):
            position = upper_bound - (position - upper_bound)
            velocity = -abs(velocity)
        elif position < lower_bound or (position == lower_bound and velocity < 0):
            position = lower_bound + (lower_bound - position)
            velocity = abs(velocity)

    return position, velocity
