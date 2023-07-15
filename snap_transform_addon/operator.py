import bpy


class SnapTransformOperator:
    def create_constraint(self, context, constraint_name):

        for obj in context.selected_objects:

            if obj == context.active_object:
                continue

            constraint = obj.constraints.new(type=constraint_name)
            constraint.target = context.active_object


class SnapRotationTransformOperator(bpy.types.Operator, SnapTransformOperator):

    bl_idname = "object.snap_active_object_rotation"
    bl_label = "Snap Active Object Rotation"

    SNAP_TRANSFORM_CONSTRAINT_NAME = "COPY_ROTATION"

    def execute(self, context):
        self.create_constraint(context, self.SNAP_TRANSFORM_CONSTRAINT_NAME)
        return {"FINISHED"}


class SnapLocationTransformOperator(bpy.types.Operator, SnapTransformOperator):

    bl_idname = "object.snap_active_object_location"
    bl_label = "Snap Active Object Location"

    SNAP_TRANSFORM_CONSTRAINT_NAME = "COPY_LOCATION"

    def execute(self, context):
        self.create_constraint(context, self.SNAP_TRANSFORM_CONSTRAINT_NAME)
        return {"FINISHED"}


class SnapScaleTransformOperator(bpy.types.Operator, SnapTransformOperator):

    bl_idname = "object.snap_active_object_scale"
    bl_label = "Snap Active Object Scale"

    SNAP_TRANSFORM_CONSTRAINT_NAME = "COPY_SCALE"

    def execute(self, context):
        self.create_constraint(context, self.SNAP_TRANSFORM_CONSTRAINT_NAME)
        return {"FINISHED"}
