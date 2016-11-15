import bayu

a = bayu.Bayu()
port = 1
while port <= 100:
	print "Port " + str(port)
	print a.isOpen("www.poltekpos.ac.id",port)
	port = port + 1