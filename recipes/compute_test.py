# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from remote_library.test.run_tests import run_tests

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
res = run_tests()
print ("test Res == "res)
# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
#test = dataiku.Dataset("test")
#test.write_with_schema()