import matplotlib.pyplot as plt
import numpy as np

def shadow_profile_of_shape(vertices, num_lines=100, scan_area=(-2, 2), num_rotations=360):
    """
    Calculate the shadow profile of an amoeba-like shape as it rotates.
    
    Parameters:
    - vertices: The vertices of the shape (nx2 numpy array).
    - num_lines: Number of evenly spaced vertical lines in the scan area.
    - scan_area: Tuple representing the x-range of the scan area (-2, 2 by default).
    - num_rotations: Number of rotations (360 for 1 degree per step).
    
    Returns:
    - shadow_matrix: A 100x360 matrix containing the shadow profiles for each rotation.
    """
    # Calculate the vertical line positions (evenly spaced along the x-axis)
    line_positions = np.linspace(scan_area[0], scan_area[1], num_lines)
    
    # Total height of the lines in the scan area (4 units from y=-2 to y=2)
    line_length = scan_area[1] - scan_area[0]

    # Initialize the matrix to store shadow profiles (100 lines x 360 degrees)
    shadow_matrix = np.zeros((num_lines, num_rotations))
    
    # Loop over each degree of rotation
    for deg in range(num_rotations):
        # Convert degree to radians
        theta = np.radians(deg)
        
        # Create a rotation matrix
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                    [np.sin(theta),  np.cos(theta)]])
        
        # Rotate the vertices of the shape
        rotated_vertices = np.dot(vertices, rotation_matrix.T)
        
        # Loop through each vertical line and calculate shadow
        for i, x_pos in enumerate(line_positions):
            # Find y-values of the shape at the current x-position (intersections)
            x_vals = rotated_vertices[:, 0]
            y_vals = rotated_vertices[:, 1]
            
            # Find all vertices where the x-position is within the current line's tolerance
            within_line = np.isclose(x_vals, x_pos, atol=(scan_area[1] - scan_area[0]) / num_lines)
            
            if np.any(within_line):
                # Get the corresponding y-values that fall within the line
                y_on_line = y_vals[within_line]
                
                # Calculate the total distance that the shape blocks the line
                shadow_length = np.max(y_on_line) - np.min(y_on_line)
                
                # Normalize the shadow length by the total line length (which is 4 units)
                normalized_shadow = shadow_length / line_length
                
                # Store the normalized shadow length in the matrix
                shadow_matrix[i, deg] = normalized_shadow

    return shadow_matrix

# Example usage:
num_vertices = 100  # Number of vertices for the amoeba-like shape
angle_step = 2 * np.pi / num_vertices
angles = np.linspace(0, 2*np.pi - angle_step, num_vertices)

# Create a base radius with noise for protrusions
base_radii = 1 + 0.2 * np.random.randn(num_vertices)

# Add more pronounced, irregular protrusions
for i in range(num_vertices):
    if i % 12 == 0:
        base_radii[i] = base_radii[i] + 0.5 + 0.5 * np.random.rand()
    elif i % 12 == 6:
        base_radii[i] = base_radii[i] + 0.3 + 0.3 * np.random.rand()

# Generate the vertices of the amoeba-like shape
vertices = np.zeros((num_vertices, 2))
for i in range(num_vertices):
    vertices[i, :] = [base_radii[i] * np.cos(angles[i]), base_radii[i] * np.sin(angles[i])]

# Call the shadow profile function
shadow_matrix = shadow_profile_of_shape(vertices)

vals = np.zeros(360)
for i in range(shadow_matrix.shape[0]):
    vals = shadow_matrix[50,:]
vals /= 100
angls = np.linspace(0, 2 * np.pi, len(vals))
print(len(vals))
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angls, vals)
ax.set_title(f'Polar Plot of Shadow')
plt.show()
