import great_expectations as gx

class GERunner:
    def __init__(self, context_root_dir="great_expectations", datasource_name="sqlite_db"):
        self.context = gx.get_context(context_root_dir=context_root_dir)

        if hasattr(self.context, "data_sources"):
            self.datasource = self.context.data_sources.get(datasource_name)
        else:
            self.datasource = self.context.sources.get(datasource_name)

    def _get_or_create_table_asset(self, table_name: str):
        asset_name = f"{table_name}_asset"
        assets_by_name = {a.name: a for a in self.datasource.assets}
        return assets_by_name.get(asset_name) or self.datasource.add_table_asset(
            name=asset_name,
            table_name=table_name,
        )

    def validate_table_with_suite(self, table_name: str, suite_name: str):
        asset = self._get_or_create_table_asset(table_name)
        batch_request = asset.build_batch_request()
        suite = self.context.suites.get(name=suite_name)

        validator = self.context.get_validator(
            batch_request=batch_request,
            expectation_suite=suite,
        )

        result = validator.validate()
        return bool(result.success), result