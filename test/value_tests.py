"""
Purpose of this test file is to cover unit test cases for Swifter.
"""


import pandas as pd
import swifter

from . import base

import random

df = pd.DataFrame({
    'x': random.sample(range(100), 5)
})


def fns(x):
    return x ** 2


def agg_fns(x):
    return x.sum() - x.min()


def standard_pandas_objects_type_checks(obj1, obj2, tag):
    assert type(obj1) is type(obj2), 'Error: {} - Type Check Failed'.format(tag)


def standard_pandas_objects_shape_checks(obj1, obj2, tag):
    assert obj1.shape == obj2.shape, 'Error: {} - Shape Mismatch'.format(tag)


def standard_pandas_objects_dtype_checks(obj1, obj2, tag):
    if type(obj1) is pd.Series:
        assert obj1.dtype == obj1.dtype, 'Error: {} - dtypes Mismatch'.format(tag)
    else:
        assert (obj1.dtypes.values == obj2.dtypes.values).all(), 'Error: {} - dtypes Mismatch'.format(tag)


def standard_pandas_objects_values_checks(obj1, obj2, tag):
    assert (obj1.values == obj2.values).all(), 'Error: {} - values Mismatch'.format(tag)


def standard_pandas_objects_checks(obj1, obj2, tag='Dataframe'):
    standard_pandas_objects_type_checks(obj1, obj2, tag)
    standard_pandas_objects_shape_checks(obj1, obj2, tag)
    standard_pandas_objects_dtype_checks(obj1, obj2, tag)
    standard_pandas_objects_values_checks(obj1, obj2, tag)


def test_swifter_apply_on_series():
    _pds = df['x']
    pd_value = base.pandas_series_apply(_pds, fns)
    swifter_value = base.swifter_series_apply(_pds, fns)
    tag = 'Series apply'
    standard_pandas_objects_checks(pd_value, swifter_value, tag)

#
# def test_swifter_apply_on_single_column():
#     _df = pd.DataFrame(df)
#     _df['x2'] = _df['x'].apply(fns)
#     _df['x3'] = _df['x'].swifter.apply(fns)
#     assert _df['x2'].equals(_df['x3'])


# def test_swifter_apply_on_dataframe():
#     _df = pd.DataFrame(df)
#     col = 'x'
#     _df['x2'] = base.pandas_dataframe_apply_one_column(_df, fns, col)
#     _df['x3'] = base.swifter_dataframe_apply_one_column(_df, fns, col)
#     pd_agg = base.pandas_dataframe_apply(_df, agg_fns)
#     swifter_agg = base.swifter_dataframe_apply(_df, agg_fns)
#     assert type(pd_agg) == type(swifter_agg), 'Dataframe apply - type Mismatch'
#     assert pd_agg.shape == swifter_agg.shape, 'Dataframe apply - shape Mismatch'
#     assert (pd_agg.dtypes.values == swifter_agg.dtypes.values).all(), 'Dataframe apply - dtypes Mismatch'
#     assert (pd_agg.values == swifter_agg.values).all(), 'Dataframe apply - value Mismatch'
#
#
# def test_swifter_apply_on_multiple_columns():
#     _df = pd.DataFrame(df)
#     # create data
#     col = 'x'
#     _df['x20'] = base.pandas_dataframe_apply_one_column(_df, fns, col)
#     _df['x21'] = _df['x']
#     _df['x30'] = base.swifter_dataframe_apply_one_column(_df, fns, col)
#     _df['x31'] = _df['x']
#     # multiple cols
#     cols = ['x20', 'x21']
#     pd_value = base.pandas_dataframe_apply_multiple_column(_df, fns, cols)
#     cols = ['x30', 'x31']
#     swifter_value = base.pandas_dataframe_apply_multiple_column(_df, fns, cols)
#     assert type(pd_value) == type(swifter_value), 'Dataframe apply - type Mismatch'
#     assert pd_value.shape == swifter_value.shape, 'Dataframe apply - shape Mismatch'
#     assert (pd_value.dtypes.values == swifter_value.dtypes.values).all,\
#         'Dataframe apply - dtypes Mismatch'
#     assert (pd_value.values == swifter_value.values).all(), 'Dataframe apply - value Mismatch'
#
