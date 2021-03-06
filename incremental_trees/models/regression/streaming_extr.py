import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import ExtraTreeRegressor

from incremental_trees.add_ins.regressor_additions import RegressorAdditions
from incremental_trees.add_ins.regressor_overloads import RegressorOverloads


class StreamingEXTR(RegressorAdditions, RegressorOverloads, ExtraTreesRegressor):
    def __init__(self,
                 n_estimators_per_chunk: int = 1,
                 n_estimators='warn',
                 max_n_estimators=np.inf,
                 criterion="mse",
                 max_depth=None,
                 min_samples_split=2,
                 min_samples_leaf=1,
                 min_weight_fraction_leaf=0.,
                 max_features="auto",
                 max_leaf_nodes=None,
                 min_impurity_decrease=0.,
                 min_impurity_split=None,
                 bootstrap=False,
                 oob_score=False,
                 n_jobs=None,
                 random_state=None,
                 verbose=0,
                 warm_start=True,
                 dask_feeding: bool = True,
                 spf_n_fits: int = 100,
                 spf_sample_prop: float = 0.1):
        super(ExtraTreesRegressor, self).__init__(
            base_estimator=ExtraTreeRegressor(),
            n_estimators=n_estimators_per_chunk,
            estimator_params=("criterion", "max_depth", "min_samples_split",
                              "min_samples_leaf", "min_weight_fraction_leaf",
                              "max_features", "max_leaf_nodes",
                              "min_impurity_decrease", "min_impurity_split",
                              "random_state"),
            bootstrap=bootstrap,
            oob_score=oob_score,
            n_jobs=n_jobs,
            random_state=random_state,
            verbose=verbose,
            warm_start=warm_start)

        self._fit_estimators = 0
        self.max_n_estimators = max_n_estimators
        self.n_estimators_per_chunk = n_estimators
        self.criterion = criterion
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.min_weight_fraction_leaf = min_weight_fraction_leaf
        self.max_features = max_features
        self.max_leaf_nodes = max_leaf_nodes
        self.min_impurity_decrease = min_impurity_decrease
        self.min_impurity_split = min_impurity_split

        # Set additional params.
        self.set_params(n_estimators_per_chunk=n_estimators_per_chunk,
                        max_n_estimators=max_n_estimators,
                        spf_n_fits=spf_n_fits,
                        spf_sample_prop=spf_sample_prop,
                        dask_feeding=dask_feeding)
