from great_expectations.dataset.pandas_dataset import PandasDataset
from constants import *

# Add the validation as a function instead of a GE expectation because
# the close template is column pair which is still not sufficient
# https://docs.greatexpectations.io/docs/guides/expectations/#creating-custom-expectations


class CustomPandasDataSet(PandasDataset):
    """CustomPandasDataSet
    It extends PandasDataset in great expectation which has
    the default supported expectation functions.
    In this class, we could write functions for custom validations
    """

    def expect_holiday_days_match_exp(self):
        df_copy = self.copy()
        
        for index, row in df_copy.iterrows():
            if row[WORK_EXP_COL] < 1 and row[VOCATION_DAYS_COL] > 5:
                return {'success': False,
                        'result': 'young employee gains more vocation days than allowed.'}
            elif row[VOCATION_DAYS_COL] > 20:
                return {'success': False,
                        'result': 'employee gains more vocation days than allowed.'}
            else:
                return {'success': True,
                    'result': 'no vocation days issues.'}
