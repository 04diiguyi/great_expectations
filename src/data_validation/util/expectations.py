from great_expectations.core.expectation_configuration import (
    ExpectationConfiguration,
)

from constants import *

def add_expt(context, suite, expectation_type, kwargs):
    """
    This is a helper function to create expectation by supplying the suite and the
    context object, and type of expectation type.

    :param context: Expectation context object
    :param suite: Expecattion suite object, in which you need to insert the expectation
    :param expectation_type: Prebuilt/custom expectation type
    :param kwargs: kwargs for the expectation type
    :returns True if it can add successfully
    """
    expectation_configuration = ExpectationConfiguration(
        expectation_type=expectation_type,
        kwargs=kwargs,
    )
    # Note optional comments omitted
    suite.add_expectation(expectation_configuration=expectation_configuration)
    context.save_expectation_suite(expectation_suite=suite, expectation_suite_name=suite.expectation_suite_name)
    return True


def get_data_expectations_column(context, expectation_suite_name):
    """
    Set up expectation configuration for data.
    Args:
      context : great expectations project context
      expectation_suite_name (string): expectation suite name
    Returns:
      suite_raw_data: expectation configuration
    """
    suite_data = context.create_expectation_suite(
        expectation_suite_name=expectation_suite_name, overwrite_existing=True
    )

    # columns need to be exist
    req_columns = [NAME_COL, AGE_COL, WORK_EXP_COL, SEX_COL, NEW_EMP_COL, VOCATION_DAYS_COL]

    for column in req_columns:
        add_expt(context, suite_data, GE_EXPECT_COLUMN_TO_EXIST, {GE_COLUMN: column})
        
    # columns should not be null
    not_null_columns = [NAME_COL, AGE_COL, WORK_EXP_COL, SEX_COL, NEW_EMP_COL, VOCATION_DAYS_COL]

    for column in not_null_columns:
        add_expt(context, suite_data, GE_EXPECT_COLUMN_VALUES_TO_NOT_BE_NULL,
                 {GE_COLUMN: column})

    # columns should match its type
    column_types = [[NAME_COL, "str"], [AGE_COL, "int64"],
                    [WORK_EXP_COL, "int64"], [SEX_COL, "str"],
                    [NEW_EMP_COL, "bool_"], [VOCATION_DAYS_COL, "int64"]]

    for column_type in column_types:
        add_expt(context, suite_data, GE_EXPECT_COLUMN_VALUES_TO_BE_OF_TYPE,
                 {GE_COLUMN: column_type[0], GE_TYPE: column_type[1]})

    return suite_data


rel_tol = 1e-09

# "expect_column_values_to_be_between",
# > 0 && <= 25
expectation_vocation_days = {
    GE_COLUMN: VOCATION_DAYS_COL,
    GE_MIN_VALUE: -rel_tol,
    GE_STRICT_MIN: "true",
    GE_MAX_VALUE: 20 + rel_tol,
    GE_STRICT_MAX: "false",
}

# "expect_column_values_to_be_between",
# >= 0
expectation_work_exp = {GE_COLUMN: WORK_EXP_COL,
                                  GE_MIN_VALUE: 0 - rel_tol, GE_STRICT_MIN: "false"}

# "expect_column_values_to_be_between",
# > 16
expectation_age = {GE_COLUMN: AGE_COL, GE_MIN_VALUE: -rel_tol, GE_STRICT_MIN: "true"}

# "expect_column_distinct_values_to_be_in_set",
expectation_sex = {
    GE_COLUMN: SEX_COL,
    GE_VALUE_SET: ['Male', 'Female', 'Other']
}

def get_data_expectations_special(context, expectation_suite_name):
    """
    Set up expectation configuration for data.
    Args:
      context : great expectations project context
      expectation_suite_name (string): expectation suite name
    Returns:
      suite_data: expectation configuration
    """
    suite_data = context.create_expectation_suite(
        expectation_suite_name=expectation_suite_name, overwrite_existing=True
    )

    add_expt(context, suite_data, GE_EXPECT_COLUMN_VALUES_TO_BE_BETWEEN, expectation_vocation_days)

    add_expt(context, suite_data, GE_EXPECT_COLUMN_VALUES_TO_BE_BETWEEN, expectation_work_exp)

    add_expt(context, suite_data, GE_EXPECT_COLUMN_VALUES_TO_BE_BETWEEN, expectation_age)

    add_expt(context, suite_data, GE_EXPECT_COLUMN_DISTINCT_VALUES_TO_BE_IN_SET, expectation_sex)

    return suite_data
