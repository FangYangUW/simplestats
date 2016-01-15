def mean(vals):
	assert type(vals) is list
	total = sum(vals)
	length = len(vals)
	return total/length
def test_mean():
	assert mean([2,4]) == 3.0
test_mean()
print(mean([2,4]))