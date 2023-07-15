bl_info = {
    "name": "Snap Transform",
    "author": "Ni-g-3l",
    "version": (0, 1),
    "blender": (3, 5, 1),
    "location": "3D View > Snap",
    "description": "Snap selected objects transform to active object",
    "warning": "",
    "doc_url": "https://github.com/Ni-g-3l/blender-snap-transform",
    "category": "Object",
}


def reload_package(module_dict_main):
    import importlib
    from pathlib import Path

    def reload_package_recursive(current_dir, module_dict):
        for path in current_dir.iterdir():
            if "__init__" in str(path) or path.stem not in module_dict:
                continue

            if path.is_file() and path.suffix == ".py":
                importlib.reload(module_dict[path.stem])
            elif path.is_dir():
                reload_package_recursive(path, module_dict[path.stem].__dict__)

    reload_package_recursive(Path(__file__).parent, module_dict_main)


if "bpy" in locals():
    reload_package(locals())

import importlib
from snap_transform_addon import bpy_loader

importlib.reload(bpy_loader)


def register():
    bpy_loader.register()


def unregister():
    bpy_loader.unregister()
