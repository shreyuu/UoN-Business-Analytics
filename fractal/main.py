import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def generate_julia_fractal(width=800, height=800, max_iter=100, a=-0.7, b=0.27):
    """
    Generate Julia set fractal with three iteration levels using cumulative golden ratio terms

    Parameters:
    - width, height: Image dimensions
    - max_iter: Maximum iterations
    - a, b: Parameters where c = a × e^(ib)

    Returns:
    - matrix: Iteration count matrix
    - image: RGB image array
    - counts: Dictionary with count statistics
    """

    # Initialize matrix and image
    matrix = np.zeros((height, width), dtype=int)
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # Complex constant c = a × e^(ib)
    # Using Euler's formula: e^(ib) = cos(b) + i×sin(b)
    c = a * (np.cos(b) + 1j * np.sin(b))

    # Counts for each iteration level
    count1 = 0
    count2 = 0
    count3 = 0

    # Zoom and position settings
    zoom = 1.5
    move_x = 0
    move_y = 0

    # Generate fractal
    for x in range(width):
        for y in range(height):
            # Map pixel to complex plane
            z_real = (x - width / 2) / (0.5 * zoom * width) + move_x
            z_imag = (y - height / 2) / (0.5 * zoom * height) + move_y
            z = complex(z_real, z_imag)

            # Store initial z magnitude and angle for the formula
            z_magnitude = abs(z)
            z_angle = np.angle(z)

            escaped = False
            iter_level = 0

            for iteration in range(max_iter):
                # Determine which equation to use (divide into thirds)
                iter_third = int((iteration / max_iter) * 3)

                # Apply equation based on iteration level
                # All use cumulative terms with golden ratio

                if iter_third == 0:
                    # Level 1: a * e^(ib) + c
                    theta1 = z_angle
                    term1 = z_magnitude * (np.cos(theta1) + 1j * np.sin(theta1))
                    z = term1 + c

                elif iter_third == 1:
                    # Level 2: a * e^(ib) + a * e^(i*0.618*b) + c
                    theta1 = z_angle
                    theta2 = 0.618 * z_angle
                    term1 = z_magnitude * (np.cos(theta1) + 1j * np.sin(theta1))
                    term2 = z_magnitude * (np.cos(theta2) + 1j * np.sin(theta2))
                    z = term1 + term2 + c

                else:
                    # Level 3: a * e^(ib) + a * e^(i*0.618*b) + a * e^(i*1.618*b) + c
                    theta1 = z_angle
                    theta2 = 0.618 * z_angle
                    theta3 = 1.618 * z_angle
                    term1 = z_magnitude * (np.cos(theta1) + 1j * np.sin(theta1))
                    term2 = z_magnitude * (np.cos(theta2) + 1j * np.sin(theta2))
                    term3 = z_magnitude * (np.cos(theta3) + 1j * np.sin(theta3))
                    z = term1 + term2 + term3 + c

                # Update magnitude and angle for next iteration
                z_magnitude = abs(z)
                z_angle = np.angle(z)

                # Check if escaped
                if z_magnitude > 2:
                    escaped = True
                    iter_level = iter_third
                    matrix[y, x] = iteration
                    break

            if not escaped:
                matrix[y, x] = max_iter

            # Count non-escaped points per iteration level
            if not escaped:
                count1 += 1
                count2 += 1
                count3 += 1
            elif iter_level == 0:
                # Escaped in first third
                pass
            elif iter_level == 1:
                count1 += 1
            elif iter_level == 2:
                count1 += 1
                count2 += 1

            # Colorful rendering based on iteration level
            if not escaped:
                # Black for non-escaped points
                image[y, x] = [0, 0, 0]
            else:
                t = matrix[y, x] / max_iter
                iter_third = int((matrix[y, x] / max_iter) * 3)

                if iter_third == 0:
                    # First third - Red theme
                    image[y, x] = [
                        int(255 * (t * 3) ** 0.5),
                        int(100 * t * 3),
                        int(50 * t * 3),
                    ]
                elif iter_third == 1:
                    # Second third - Green theme
                    image[y, x] = [
                        int(50 * t * 3),
                        int(255 * (t * 3) ** 0.5),
                        int(100 * t * 3),
                    ]
                else:
                    # Third third - Blue theme
                    image[y, x] = [
                        int(100 * t * 3),
                        int(50 * t * 3),
                        int(255 * (t * 3) ** 0.5),
                    ]

    counts = {
        "level1": count1,
        "level2": count2,
        "level3": count3,
        "total": width * height,
        "escaped": width * height - count3,
    }

    return matrix, image, counts


def display_results(matrix, image, counts, a, b):
    """
    Display the fractal image, matrix, and statistics
    """

    # Calculate c for display
    c = a * (np.cos(b) + 1j * np.sin(b))

    # Create figure with subplots
    fig = plt.figure(figsize=(16, 12))

    # Plot 1: Fractal image
    ax1 = plt.subplot(2, 2, 1)
    ax1.imshow(image)
    ax1.set_title(
        f"Julia Set Fractal (Cumulative Golden Ratio)\nc = a×e^(ib) = {c.real:.4f} + {c.imag:.4f}i",
        fontsize=14,
        fontweight="bold",
    )
    ax1.axis("off")

    # Plot 2: Matrix visualization (heatmap)
    ax2 = plt.subplot(2, 2, 2)
    im = ax2.imshow(matrix, cmap="hot", interpolation="nearest")
    ax2.set_title("Iteration Count Matrix", fontsize=14, fontweight="bold")
    plt.colorbar(im, ax=ax2, label="Iterations")

    # Plot 3: Statistics
    ax3 = plt.subplot(2, 2, 3)
    ax3.axis("off")

    stats_text = f"""
    ITERATION EQUATIONS (Cumulative Golden Ratio):
    
    Level 1 (Red):    z = a×e^(ib) + c
    
    Level 2 (Green):  z = a×e^(ib) + a×e^(i×0.618b) + c
    
    Level 3 (Blue):   z = a×e^(ib) + a×e^(i×0.618b) + a×e^(i×1.618b) + c
    
    Where: c = a × e^(ib)
           a = {a}
           b = {b}
           c = {c.real:.4f} + {c.imag:.4f}i
           0.618 ≈ 1/φ (inverse golden ratio)
           1.618 ≈ φ (golden ratio)
    
    STATISTICS - Non-Escaped Points:
    
    Level 1: {counts['level1']:,} points ({counts['level1']/counts['total']*100:.2f}%)
    Level 2: {counts['level2']:,} points ({counts['level2']/counts['total']*100:.2f}%)
    Level 3: {counts['level3']:,} points ({counts['level3']/counts['total']*100:.2f}%)
    
    Total Points: {counts['total']:,}
    Escaped Points: {counts['escaped']:,} ({counts['escaped']/counts['total']*100:.2f}%)
    """

    ax3.text(
        0.1,
        0.5,
        stats_text,
        fontsize=10,
        family="monospace",
        verticalalignment="center",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5),
    )

    # Plot 4: Numerical matrix (partial view)
    ax4 = plt.subplot(2, 2, 4)
    ax4.axis("off")

    # Show a small portion of the matrix (first 20x20)
    matrix_sample = matrix[:20, :20]
    matrix_text = "Numerical Matrix (first 20x20):\n\n"
    matrix_text += "\n".join(
        [" ".join([f"{val:3d}" for val in row]) for row in matrix_sample]
    )

    ax4.text(
        0.05,
        0.95,
        matrix_text,
        fontsize=7,
        family="monospace",
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="lightblue", alpha=0.5),
    )

    plt.tight_layout()
    plt.show()


def print_full_matrix(matrix):
    """
    Print the full numerical matrix to console
    """
    print("\n" + "=" * 80)
    print("FULL NUMERICAL MATRIX:")
    print("=" * 80)
    for row in matrix:
        print(" ".join([f"{val:3d}" for val in row]))
    print("=" * 80 + "\n")


# Main execution
if __name__ == "__main__":
    # Parameters
    WIDTH = 400
    HEIGHT = 400
    MAX_ITERATIONS = 100

    # Complex constant c = a + ib
    a = -0.7
    b = 0.27

    print("Generating Julia Set Fractal (Cumulative Golden Ratio)...")
    print(f"Using c = a × e^(ib)")
    print(f"  a = {a}")
    print(f"  b = {b}")
    c_value = a * (np.cos(b) + 1j * np.sin(b))
    print(f"  c = {c_value.real:.4f} + {c_value.imag:.4f}i")
    print(f"Image size: {WIDTH}x{HEIGHT}")
    print(f"Max iterations: {MAX_ITERATIONS}")
    print("\nIterations (Cumulative):")
    print("  Level 1: z = a×e^(ib) + c")
    print("  Level 2: z = a×e^(ib) + a×e^(i×0.618b) + c")
    print("  Level 3: z = a×e^(ib) + a×e^(i×0.618b) + a×e^(i×1.618b) + c")
    print("\nProcessing...\n")

    # Generate fractal
    matrix, image, counts = generate_julia_fractal(WIDTH, HEIGHT, MAX_ITERATIONS, a, b)

    # Print statistics
    print("STATISTICS:")
    print(
        f"  Level 1 non-escaped points: {counts['level1']:,} ({counts['level1']/counts['total']*100:.2f}%)"
    )
    print(
        f"  Level 2 non-escaped points: {counts['level2']:,} ({counts['level2']/counts['total']*100:.2f}%)"
    )
    print(
        f"  Level 3 non-escaped points: {counts['level3']:,} ({counts['level3']/counts['total']*100:.2f}%)"
    )
    print(f"  Total points: {counts['total']:,}")
    print(
        f"  Escaped points: {counts['escaped']:,} ({counts['escaped']/counts['total']*100:.2f}%)"
    )

    # Display results
    display_results(matrix, image, counts, a, b)

    # Uncomment the line below to print the full numerical matrix
    # print_full_matrix(matrix)

    # Save image
    plt.imsave("julia_fractal.png", image)
    print("\nImage saved as 'julia_fractal.png'")

    # Save matrix to file
    np.savetxt("julia_matrix.txt", matrix, fmt="%3d")
    print("Matrix saved as 'julia_matrix.txt'")
