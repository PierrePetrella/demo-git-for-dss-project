# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Orders = dataiku.Dataset("Orders")
Orders_df = Orders.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_2_df = Orders_df # For this sample code, simply copy input to output


# Write recipe outputs
test_2 = dataiku.Dataset("test_2")
test_2.write_with_schema(test_2_df)
