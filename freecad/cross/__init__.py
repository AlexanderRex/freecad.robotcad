"""Entry point of the CROSS workbench."""

import FreeCAD as fc

from .ros.utils import add_ros_library_path
from .version import __version__
from .wb_globals import g_ros_distro

add_ros_library_path(g_ros_distro)

# Must be imported after the call to `add_ros_library_path`.
from .ros.utils import is_ros_found  # noqa: E402.

import os

# init debug for VS Code
if os.environ.get('FREECADCROSS_DEBUG'):
    # how to use:
    # FREECADCROSS_DEBUG=1 command_to_run_freecad
    # Dont forget install debugpy if set debug env
    import debugpy
    debugpy.configure(python="python3")
    debugpy.listen(5678)
    debugpy.trace_this_thread(True)
    debugpy.debug_this_thread()

if is_ros_found():
    fc.addImportType('URDF files (*.urdf *.xacro)', 'import_urdf')
