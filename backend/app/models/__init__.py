
# Automatically import all Python files in this directory
from importlib import import_module
import os
import glob

package_dir = os.path.dirname(__file__)
modules = glob.glob(os.path.join(package_dir, "*.py"))

for module_path in modules:
    module_name = os.path.basename(module_path)[:-3]  # strip .py
    if module_name != "__init__":
        import_module(f".{module_name}", package="backend.app.models")