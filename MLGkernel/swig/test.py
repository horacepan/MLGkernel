from MLGK import *

fname = "/home/hopan/MLGkernel/data/MUTAG.txt"
save_name = "m.txt"
eta = 0.01
gamma= 0.001
grow = True
radius = 2
levels = 2

m = MLGdataset(fname, eta, gamma, grow)
m.computeGram(levels, radius)
m.saveGram(save_name)
