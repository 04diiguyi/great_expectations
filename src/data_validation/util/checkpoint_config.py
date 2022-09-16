def get_checkpoint_config(check_point_name, expectation_suite_name):
    """
    Set up checkpoint configuration.
    Args:
      check_point_name (string): checkpoint name
      expectation_suite_name (string): expectation suite name
    Returns:
      checkpoint_config: checkpoint configuration
    """
    checkpoint_config = {
        "name": check_point_name,
        "config_version": 1,
        "class_name": "SimpleCheckpoint",
        "expectation_suite_name": expectation_suite_name,
    }

    return checkpoint_config
