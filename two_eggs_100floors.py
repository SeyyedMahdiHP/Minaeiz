# this is two eggs and 100 floor problem


def trace_floor_with_eggs(minimum_number_drops, maximum_number_drops, floors):
    if floors <= 0:
        return minimum_number_drops
    minimum_number_drops += 1
    return trace_floor_with_eggs(minimum_number_drops, maximum_number_drops - 1, floors - maximum_number_drops)


print("minimum number of drop: %d" % trace_floor_with_eggs(0, 14, 100))
