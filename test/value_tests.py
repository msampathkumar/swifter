"""
Purpose of this test file is to cover unit test cases for Swifter.
"""
import random
import pandas as pd
import swifter # pylint: disable=unused-import

try:
    from . import base
except ImportError:
    import base

df = pd.DataFrame({
    'x': random.sample(range(100), 5)
})


def square(x):
    return x ** 2


def distance_fns(x):
    return x.sum() - x.min()


def pd_objects_type_checks(obj1, obj2, tag):
    tag = 'Error: {} - Type Check Failed'.format(tag)
    assert type(obj1) is type(obj2), tag


def pd_objects_shape_checks(obj1, obj2, tag):
    tag = 'Error: {} - Shape Mismatch'.format(tag)
    assert obj1.shape == obj2.shape, tag


def pd_objects_dtype_checks(obj1, obj2, tag):
    tag = 'Error: {} - dtypes Mismatch'.format(tag)
    if type(obj1) is pd.Series:
        assert obj1.dtype == obj1.dtype, tag
    else:
        assert (obj1.dtypes.values == obj2.dtypes.values).all(), tag


def pd_objects_value_checks(obj1, obj2, tag):
    tag = 'Error: {} - values Mismatch'.format(tag)
    assert (obj1.values == obj2.values).all(), tag


def pd_objects_checks(obj1, obj2, tag='Swifter Object'):
    pd_objects_type_checks(obj1, obj2, tag)
    pd_objects_shape_checks(obj1, obj2, tag)
    pd_objects_dtype_checks(obj1, obj2, tag)
    pd_objects_value_checks(obj1, obj2, tag)


###########################################################################################

def test_swifter_apply_on_series():
    _pds = df['x']
    pd_value = base.pandas_series_apply(_pds, square)
    swifter_value = base.swifter_series_apply(_pds, square)
    pd_objects_checks(pd_value, swifter_value, 'Swifter Apply on Series')


def test_swifter_apply_on_single_column():
    _df = pd.DataFrame(df)
    tag = 'Swifter Apply on a DataFrame Col'
    pd_result = _df['x'].apply(square)
    swifter_result = _df['x'].swifter.apply(square)
    pd_objects_checks(pd_result, swifter_result, tag)


def test_swifter_apply_on_dataframe():
    _df = pd.DataFrame(df)
    col = 'x'
    tag = 'Swifter apply on whole Dataframe'
    _df['x2'] = base.pandas_dataframe_apply_one_column(_df, square, col)
    _df['x3'] = base.swifter_dataframe_apply_one_column(_df, square, col)
    pd_agg = base.pandas_dataframe_apply(_df, distance_fns)
    swifter_agg = base.swifter_dataframe_apply(_df, distance_fns)
    pd_objects_checks(pd_agg, swifter_agg, tag)


def test_swifter_apply_on_multiple_columns():
    _df = pd.DataFrame(df)
    # setting test data
    tag = 'Swifter apply on multiple df cols'
    col = 'x'
    _df['x20'] = base.pandas_dataframe_apply_one_column(_df, square, col)
    _df['x21'] = _df['x']
    _df['x30'] = base.swifter_dataframe_apply_one_column(_df, square, col)
    _df['x31'] = _df['x']
    # multiple cols
    cols = ['x20', 'x21']
    pd_value = base.pandas_dataframe_apply_multiple_column(_df, square, cols)
    cols = ['x30', 'x31']
    swifter_value = base.pandas_dataframe_apply_multiple_column(_df, square, cols)
    pd_objects_checks(pd_value, swifter_value, tag)


def test_swifter_rolling_apply():
    # TODO
    pass

