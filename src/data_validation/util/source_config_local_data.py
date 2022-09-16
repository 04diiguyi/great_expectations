def get_runtime_datasource_config(datasource_name, execution_engine):
    """
    Set up local data source configuration.
    Args:
      datasource_name (string): datasource name
      execution_engine (string): the method to read data
    Returns:
      datasource_config: data source configuration
    """
    datasource_config = {
        "name": datasource_name,
        "class_name": "Datasource",
        "execution_engine": {"class_name": execution_engine},
        "data_connectors": {
            "default_runtime_data_connector_name": {
                "class_name": "RuntimeDataConnector",
                "batch_identifiers": ["default_identifier_name"],
            },
        }
    }

    return datasource_config
