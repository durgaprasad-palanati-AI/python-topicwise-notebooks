from pkg1 import tpack
tp=tpack("durga")
tp.tpackmet()
#it is from tpack2.py durga

from pkg1.tpack1 import tpack
tp=tpack("durga")
tp.tpackmet()
#it is from tpack1.py durga

from pkg1.tpack2 import tpack
tp=tpack("durga")
tp.tpackmet()
#it is from tpack2.py durga

import pkg1.tpack1 as pt1
tp=pt1.tpack("durga")
tp.tpackmet()
#it is from tpack1.py durga

import pkg1.tpack2 as pt2
tp=pt2.tpack("durga")
tp.tpackmet()
#it is from tpack2.py durga

from pkg1 import name,age

tp=name("durga")
tp.tpackmet()
#it is from tpack3.py durga

tp=age("30")
tp.tpackmet()
#it is from tpack3.py 30


from pkg1 import *

tp=name("durga")
tp.tpackmet()
#it is from tpack3.py durga

tp=age("30")
tp.tpackmet()
#it is from tpack3.py 30

tp=tpack("durga")
tp.tpackmet()
#it is from tpack2.py durga
