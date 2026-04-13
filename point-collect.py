import bpy
import json
import os

# Get the active object
obj = bpy.context.active_object

# Extract vertices in world space
vertices = []
matrix_world = obj.matrix_world

for vert in obj.data.vertices:
    # Convert local coordinates to world coordinates
    world_pos = matrix_world @ vert.co
    vertices.append({
        "x": round(world_pos.x, 4),
        "y": round(world_pos.y, 4),
        "z": round(world_pos.z, 4)
    })

# Define the output path (Change this to your project folder)
output_path = os.path.join(bpy.path.abspath("//"), "lorenz.json")

with open(output_path, 'w') as f:
    json.dump(vertices, f, indent=2)

print(f"Successfully exported {len(vertices)} points to {output_path}")