# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['Meoinfo']

# %% ../nbs/00_core.ipynb 3
from pandas import DataFrame
from fastcore.utils import *


class Meoinfo:

    def __init__(self,
                train_data: DataFrame,            # training dataset
                test_data: DataFrame,             # test dataset, originated from random test/train split
                oot_data: DataFrame,              # out of time dataset
                baseline_y_true_name: str,        # name of the target variable
                baseline_y_prob_name: str,        # name of the probability column of the baseline model
                features: list,                   # list of features
                bad_rate_limit: float = 0,        # the maximum bad rate limit that credit policy should alllow
                scenario: str = "variables",      # "variables" or "score"
                test: str = "all",                # which test to run within the scenario
                weights_name: str = None,         # name of the columns that contains negated inference weights
                baseline_rating_name: str = None, # baseling rating name
                blend_rating_name: str = None,    # blend rating name
                n_features_to_select: int = 10,   # number of features to select from features list
                algorithm: str = "catboost",      # the algorithm to use
                search_params: dict = None        # grid search params
    ):
        store_attr()
        __repr__ = basic_repr('algorithm')

        
