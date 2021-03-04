import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureSelector(BaseEstimator, TransformerMixin):

    def __init__(self, feature_names, ts_index):
        self.feature_names = feature_names
        self.index = ts_index

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.set_index(pd.to_datetime(X[self.index]))
        return X[self.feature_names]

class DateTimeExpander(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        dts = pd.Series(X.index).dt
        X["dts_month"] = dts.month.values
        X["dts_hour"] = dts.hour.values
        X["dts_day_of_week"] = dts.dayofweek.values

        return X

from meteocalc import Temp, feels_like
class FeelsLikeExpander(BaseEstimator, TransformerMixin):

    def __init__(self, temp_col, hum_col, windspeed_col, atemp_col):
        self.temp = temp_col
        self.hum = hum_col
        self.windspeed = windspeed_col
        self.atemp_col = atemp_col

    def fit(self, X, y=None):
        return self

    def temp_adjust(self, tup):
            atemp = feels_like(Temp(tup[self.temp],'c'), tup[self.hum], tup[self.windspeed])
            tup[self.atemp_col] = atemp.c
            return tup

    def transform(self,X):
        X = X.apply(self.temp_adjust, axis=1)
        X = X.drop(["temp","hum","windspeed"], axis=1)
        return X


class LagExpander(BaseEstimator, TransformerMixin):

    def __init__(self, lag_col):
        self.lag = lag_col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X[self.lag + "_lag1"] = X[self.lag].shift(1, fill_value=X.cnt[0])
        X[self.lag + "_lag24"] = X[self.lag].shift(24, fill_value=X.cnt[0])

        return X



class TargetDropper(BaseEstimator, TransformerMixin):

    def __init__(self, target_col):
        self.target = target_col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
#         import pdb; pdb.set_trace() # Here's how to enter the debugger in one line.  Don't forget to delete afterwards!
        return X.drop(self.target, axis=1)
