# Predict the Output
# Without running it, predict what this prints, then verify:
# nums = [1, 2, 3, 4, 5]
# r = list(map(lambda x: x * 2, filter(lambda x: x > 2, nums)))
# print(r)
# Tests: reading nested map/filter — filter runs first, then map transforms what's left

nums = [1, 2, 3, 4, 5]
r = list(map(lambda x: x * 2, filter(lambda x: x > 2, nums)))
print(r)