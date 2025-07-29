import pdb

def setup_pdb(pdb):
    pdb.set_trace = lambda: pdb.Pdb().set_trace(sys._getframe().f_back)
    pdb.default_pdb.set_sticky_by_default(True)

# Enable sticky mode by default
class Config(pdb.DefaultConfig):
    sticky_by_default = True

