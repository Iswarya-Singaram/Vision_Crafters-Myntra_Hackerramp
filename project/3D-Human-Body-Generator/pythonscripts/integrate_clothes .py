import bpy
import sys

# Get command-line arguments passed from subprocess.run
argv = sys.argv[sys.argv.index("--") + 1:]

# Example: Parse command-line arguments
clothing_option = argv[0]  # Example: Extract clothing option parameter
other_parameters = argv[1:]  # Example: Extract other parameters as needed

# Example: Apply clothing logic
# Replace this with your actual clothing integration logic
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Example: Load clothing or apply textures/materials to the existing model
# Replace this with your actual clothing loading or material assignment logic
clothing_path = f"./clothes/{/home/iswarya/Downloads/uploads_files_3636200_T-shirt.blend1}.obj"
bpy.ops.import_scene.obj(filepath=clothing_path)

# Example: Adjust clothing position or scale as needed
# Replace this with your actual adjustments based on measurements or options
bpy.context.object.location.x = 1.0
bpy.context.object.scale = (1.2, 1.2, 1.2)

# Example: Save the modified scene
output_path = "./projectexports/generatedbody_with_clothes.glb"
bpy.ops.export_scene.gltf(filepath=output_path)

# Exit Blender gracefully
bpy.ops.wm.quit_blender()
