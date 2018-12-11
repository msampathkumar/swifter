import pandas as pd
import swifter

# TODO: base structures


def pandas_series_apply(pds, fns):
    return pds.apply(fns)


def swifter_series_apply(pds, fns):
    return pds.swifter.apply(fns)


def pandas_dataframe_apply(df, fns):
    return df.apply(fns)


def swifter_dataframe_apply(df, fns):
    return df.swifter.apply(fns)


def pandas_dataframe_apply_one_column(df, fns, col):
    return df[col].apply(fns)


def swifter_dataframe_apply_one_column(df, fns, col):
    return df[col].swifter.apply(fns)


def pandas_dataframe_apply_multiple_column(df, fns, cols):
    return df[cols].apply(fns)


def swifter_dataframe_apply_multiple_column(df, fns, cols):
    return df[cols].swifter.apply(fns)


