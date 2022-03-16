# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu


import 





# Write recipe outputs
test = dataiku.Dataset("test")
test.write_with_schema(pd.DataFrame())
