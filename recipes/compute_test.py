# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



from test.run_tests import run_tests




# Write recipe outputs
test = dataiku.Dataset("test")
test.write_with_schema(pd.DataFrame())
