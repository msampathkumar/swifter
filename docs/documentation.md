# Documentation

## 1. `pandas.Series.swifter.apply`

Efficiently apply any function to a pandas series in the fastest available manner

```python
def pandas.Series.swifter.apply(func, convert_dtype=True, args=(), **kwds)
```

**Parameters:**

`func` : function. Function to apply to each element of the series.

`convert_dtype` : boolean, default True. Try to find better dtype for elementwise function results. If False, leave as dtype=object

`args` : tuple. Positional arguments to pass to function in addition to the value

`kwds` : Additional keyword arguments will be passed as keywords to the function

## 2. `pandas.DataFrame.swifter.apply`

Efficiently apply any function to a pandas dataframe in the fastest available manner.

```python
def pandas.DataFrame.swifter.apply(func, axis=1, broadcast=None, raw=False, reduce=None, result_type=None, args=(), **kwds)
```

**Parameters:**

`func` : function. Function to apply to each column or row.

`axis` : {0 or 'index', 1 or 'columns'}, default 0. **For now, Dask only supports axis=1, and thus swifter is limited to axis=1**. Axis along which the function is applied:

* 0 or 'index': apply function to each column.
* 1 or 'columns': apply function to each row.

`broadcast` : bool, optional. Only relevant for aggregation functions:

False or None : returns a Series whose length is the length of the index or the number of columns (based on the axis parameter)
True : results will be broadcast to the original shape of the frame, the original index and columns will be retained.
Deprecated since version 0.23.0: This argument will be removed in a future version, replaced by result_type='broadcast'.

`raw` : bool, default False

False : passes each row or column as a Series to the function.
True : the passed function will receive ndarray objects instead. If you are just applying a NumPy reduction function this will achieve much better performance.

`reduce` : bool or None, default None. Try to apply reduction procedures. If the DataFrame is empty, apply will use reduce to determine whether the result should be a Series or a DataFrame. If reduce=None (the default), apply's return value will be guessed by calling func on an empty Series (note: while guessing, exceptions raised by func will be ignored). If reduce=True a Series will always be returned, and if reduce=False a DataFrame will always be returned.

Deprecated since pandas version 0.23.0: This argument will be removed in a future version, replaced by result_type='reduce'.

`result_type` : {'expand', 'reduce', 'broadcast', None}, default None. These only act when axis=1 (columns):

'expand' : list-like results will be turned into columns.
'reduce' : returns a Series if possible rather than expanding list-like results. This is the opposite of 'expand'.
'broadcast' : results will be broadcast to the original shape of the DataFrame, the original index and columns will be retained.
The default behaviour (None) depends on the return value of the applied function: list-like results will be returned as a Series of those. However if the apply function returns a Series these are expanded to columns.

New in pandas version 0.23.0.

`args` : tuple. Positional arguments to pass to func in addition to the array/series.

`kwds` : Additional keyword arguments to pass as keywords arguments to func.


**returns:**

The new dataframe/series with the function applied as quickly as possible

## 3. `pandas.DataFrame.swifter.rolling.apply`

Applies over a rolling object on the original series/dataframe in the fastest available manner.

```python
def pandas.DataFrame.swifter.rolling(window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None).apply(func, *args, **kwds)
```

## 4. `pandas.DataFrame.swifter.progress_bar(False).apply`

Enable or disable the TQDM progress bar by setting the enable parameter to True/False, respectively.

```python
def pandas.DataFrame.swifter.progress_bar(enable=True)
```

For example, let's say we have a pandas dataframe df. The following will perform a swifter apply, without the TQDM progress bar.
```python
df.swifter.progress_bar(False).apply(lambda x: x+1)
```

## 5. `pandas.DataFrame.swifter.set_npartitions(npartitions=None).apply`

Specify the number of partitions to allocate to swifter, if parallel processing is chosen to be the quickest apply.
If npartitions=None, it defaults to cpu_count()*2

```python
def pandas.DataFrame.swifter.set_npartitions(npartitions=None)
```

For example, let's say we have a pandas dataframe df. The following will perform a swifter apply, using 2 partitions 
```python
df.swifter.set_npartitions(2).apply(lambda x: x+1)
```

## 6. `pandas.DataFrame.swifter.set_dask_threshold(dask_threshold=1).apply`

Specify the dask threshold (in seconds) for the max allowable time estimate for a pandas apply on the full dataframe
```python
def pandas.DataFrame.swifter.set_dask_threshold(dask_threshold=1)
```

For example, let's say we have a pandas dataframe df. The following will perform a swifter apply, with the threshold set to 3 seconds
```python
df.swifter.set_dask_threshold(dask_threshold=3).apply(lambda x: x+1)
```