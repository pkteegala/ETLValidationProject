
class GE_Helper:

 @staticmethod
 def validate_expectations(context,model_name):
        
    success, result = context.ge_runner.validate_table_with_suite(
        table_name=model_name,
        suite_name=model_name,
    )

    context.ge_success = success
    context.ge_result = result

    if not success:

        failed_expectations = []

        for r in result.results:
            if not r.success:
                failed_expectations.append({
                    "expectation": r.expectation_config.type,
                    "column": r.expectation_config.kwargs.get("column"),
                    "details": r.result
                })

        raise AssertionError(
            f"\nGE validation failed for '{model_name}'\n"
            f"Success Percent: {result.statistics.get('success_percent')}\n"
            f"Failed Expectations:\n{failed_expectations}"
        )