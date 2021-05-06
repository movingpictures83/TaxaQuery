# TaxaQuery
# Language: Python
# Input: TXT
# Output: CSV 
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that takes a CSV file of taxa abundances (rows are samples
columns are taxa).  It returns a CSV file containing statistics on all
taxa whose name matches a user-specified pattern, including percentage.

The plugin accepts as input a TXT file, where the first line is the 
input CSV file and the second line is the pattern to match.
