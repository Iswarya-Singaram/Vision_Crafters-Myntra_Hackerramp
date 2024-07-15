'''
blenderPath = r""
projectPath = r""
scriptPath = r""'''
import subprocess

def run_blender(blenderPath, projectPath, scriptPath, measures):
    # Add the projectPath to measures if needed
    subprocess.run([blenderPath,
                    "--background",
                    projectPath,
                    "--python", scriptPath,
                    "--"] + measures)

def execute(obj):
    blenderPath = r"/usr/bin/blender"  # Update this path
    projectPath = r"./blenderfiles/humanproject.blend"  # Update this path
    scriptPath = r"./pythonscripts/bodyEditor.py"  # Update this path
    measures = [str(value) for value in obj.values()]  # Assuming obj is a dict

    run_blender(blenderPath, projectPath, scriptPath, measures)

def try_on_clothes(obj):
    blenderPath = r"/usr/bin/blender"  # Update this path
    projectPath = r"./blenderfiles/final_model.glb.blend"  # Update this path
    scriptPath = r"./pythonscripts/bodyEditor.py"  # Update this path
    measures = [str(value) for value in obj.values()]  # Assuming obj is a dict

    run_blender(blenderPath, projectPath, scriptPath, measures)
