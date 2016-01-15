def mean(vals):
	assert type(vals) is list
	total = sum(vals)
	length = len(vals)
	if length == 0:
		return 0.0
	else:
		return total/length
	
def test_mean():
	assert mean([2,4]) == 3.0
test_mean()

def test_empty_list():
	assert mean([]) == 0.0
test_empty_list()

print(mean([]))