import subprocess
import os
import shutil


class DBTRunner:

    @staticmethod
    def execute(command="run"):
        
        dbt_exe = shutil.which("dbt")
        if not dbt_exe:
            raise RuntimeError("dbt not found. Activate venv.")

        dbt_project_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../dbt_project")
        )

        print(f"\nRunning dbt {command} from: {dbt_project_dir}\n")
        result = subprocess.run(
            ["dbt"] + command.split(),
            cwd=str(dbt_project_dir),
            capture_output=True,
            text=True
        )

        print("DBT STDOUT:\n", result.stdout)
        print("DBT STDERR:\n", result.stderr)

        if result.returncode != 0:
            raise Exception(f"dbt {command} failed")