from great_expectations.data_context.types.base import (
    DataContextConfig,
)

import os


def get_project_config_local(expectations_store_dir, validations_store_dir, checkpoint_store_dir, data_docs_sites_dir):
    """
    Set up project configuration.
    Args:
      expectations_store_dir (string): expectations store directory
      validations_store_dir (string): validations store directory
      checkpoint_store_dir (string): checkpoint store directory
      data_docs_sites_dir (string): data docs sites directory
    Returns:
      project_config: project configuration
    """
    project_config = DataContextConfig(
        config_version=3,
        config_variables_file_path=None,
        plugins_directory=None,
        stores={
            "expectations_store": {
                "class_name": "ExpectationsStore",
                "store_backend": {
                    "class_name": "TupleFilesystemStoreBackend",
                    "base_directory": expectations_store_dir,
                },
            },
            "validations_store": {
                "class_name": "ValidationsStore",
                "store_backend": {
                    "class_name": "TupleFilesystemStoreBackend",
                    "base_directory": validations_store_dir,
                },
            },
            "evaluation_parameter_store": {
                "class_name": "EvaluationParameterStore"
            },
            "checkpoint_store": {
                "class_name": "CheckpointStore",
                "store_backend": {
                    "class_name": "TupleFilesystemStoreBackend",
                    "base_directory": checkpoint_store_dir,
                },
            },
        },
        expectations_store_name="expectations_store",
        checkpoint_store_name="checkpoint_store",
        validations_store_name="validations_store",
        evaluation_parameter_store_name="evaluation_parameter_store",
        data_docs_sites={
            "local_site": {
                "class_name": "SiteBuilder",
                "show_how_to_buttons": "true",
                "store_backend": {
                    "class_name": "TupleFilesystemStoreBackend",
                    "base_directory": data_docs_sites_dir
                },
                "site_index_builder": {
                    "class_name": "DefaultSiteIndexBuilder"
                }
            },
        },
        anonymous_usage_statistics={
            "enabled": True
        }
    )

    return project_config


def get_project_config_pipeline():
    """
    Create great expectation configuration with folder locations.
    Returns:
      project_config: project configuration for the pipeline
    """
    current_path = os.getcwd()

    # create great expectation project config and context
    expectations_store_dir = os.path.join(current_path, "great_expectations", "expectations")
    validations_store_dir = os.path.join(current_path, "great_expectations", "validations")
    checkpoint_store_dir = os.path.join(current_path, "great_expectations", "checkpoints")
    local_site_datadoc_dir = os.path.join(current_path, "great_expectations", "uncommitted/data_docs/local_site/")

    project_config = get_project_config_local(
        expectations_store_dir, validations_store_dir, checkpoint_store_dir, local_site_datadoc_dir)

    return project_config
