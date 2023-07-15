import bpy

from snap_transform_addon.operator import (
    SnapScaleTransformOperator,
    SnapLocationTransformOperator,
    SnapRotationTransformOperator,
)


def draw_snap_transform_menu(self, context):
    self.layout.separator()
    self.layout.operator(SnapLocationTransformOperator.bl_idname)
    self.layout.operator(SnapRotationTransformOperator.bl_idname)
    self.layout.operator(SnapScaleTransformOperator.bl_idname)


def register():
    bpy.types.VIEW3D_MT_snap.append(draw_snap_transform_menu)


def unregister():
    bpy.types.VIEW3D_MT_snap.remove(draw_snap_transform_menu)
