from project_config import get_project_config_pipeline
from source_config_local_data import get_runtime_datasource_config
from ruamel import yaml
from great_expectations.data_context import BaseDataContext


def getContext():
    """
    Set up great expectation project configuration with in memory data source.
    Returns:
      curr_context: project configuration context for the pipeline
    """
    project_config = get_project_config_pipeline()

    # create in memory data source
    datasource_name = "fs_datasource"
    execution_engine = "PandasExecutionEngine"

    datasource_config = get_runtime_datasource_config(datasource_name, execution_engine)

    curr_context = BaseDataContext(project_config=project_config)
    curr_context.test_yaml_config(yaml.dump(datasource_config))

    curr_context.add_datasource(**datasource_config)

    return curr_context
