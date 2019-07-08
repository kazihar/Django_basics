from percen import dis_perc

def test_percentest():
	perc = dis_perc(100, 10)
	assert perc == 10
	a = "a"
	b = "b"
	perc = dis_perc(a, b)
	assert perc == "Invalid arguments"
	
