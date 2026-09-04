def calculate_flight_time(weight_grams):
    """
    Calculate the drone's active flight time based on payload weight.

    Parameters:
        weight_grams: Payload weight in grams.

    Returns:
        Flight time in minutes.
    """
    if weight_grams < 0:
        raise ValueError("Payload weight cannot be negative.")

    flight_time = 180 - (0.1 * weight_grams)

    return max(0, flight_time)


def flight_time_table(max_weight_grams, step_grams):
    """
    Create a list of payload weights and their flight times.

    Parameters:
        max_weight_grams: Maximum payload weight in grams.
        step_grams: Amount to increase the weight each step.

    Returns:
        A list of (weight, flight_time) pairs.
    """
    table = []

    for weight in range(0, max_weight_grams + 1, step_grams):
        table.append((weight, calculate_flight_time(weight)))

    return table