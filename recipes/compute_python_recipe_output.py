# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Orders_enriched_prepared = dataiku.Dataset("Orders_enriched_prepared")
Orders_enriched_prepared_df = Orders_enriched_prepared.get_dataframe()


python_recipe_output_df = Orders_enriched_prepared_df.describe() # For this sample code, simply copy input to output


# Write recipe outputs
python_recipe_output = dataiku.Dataset("python_recipe_output")
python_recipe_output.write_with_schema(python_recipe_output_df)
print ("hello1")