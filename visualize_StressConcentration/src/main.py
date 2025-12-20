# -*- coding: utf-8 -*-
"""
Created on Sun May  4 13:45:45 2025

@author: Bagus Alifah Hasyim
"""

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

class MeshStressProcessor:
    def __init__(
        self, 
        input_pattern: str = "MeshNumber_*.dat", 
        resource_dir: str = None, 
        output_dir: str = None
    ):
        # Base directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Resolve resource directory
        if resource_dir is None:
            resource_dir = os.path.join(script_dir, "../resources")
        self.resource_dir = os.path.abspath(resource_dir)

        # Resolve output directory
        if output_dir is None:
            output_dir = os.path.join(script_dir, "../res")
        self.output_dir = os.path.abspath(output_dir)

        self.input_pattern = input_pattern
        self.datasets = []

        # Make sure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def read_files(self):
        """
        Reads all matching mesh data files into datasets.
        """
        search_patterns = []

        # If a resource_dir is provided, search there
        if self.resource_dir:
            search_patterns.append(os.path.join(self.resource_dir, self.input_pattern))

        # Always search the current working directory as well
        # search_patterns.append(os.path.join(os.getcwd(), self.input_pattern))

        files = []
        for pattern in search_patterns:
            files.extend(glob.glob(pattern))

        files = sorted(set(files))

        if not files:
            raise FileNotFoundError(
                f"No files found for pattern: {self.input_pattern}\nChecked patterns: {search_patterns}"
            )

        print("Found files:")
        for f in files:
            print(f" - {f}")

        for idx, file in enumerate(files, start=1):  # start=1 for mesh variation index
            df = pd.read_csv(file, delim_whitespace=True, header=None)
            df.columns = ["path_length", "stress"]
            self.datasets.append({
                "label": f"Mesh Number {idx}",  # Label as index
                "path_length": df["path_length"],
                "stress": df["stress"]
            })

    def plot_individual(self, line_width=1.8, font_name="Times New Roman", font_size=12):
        """
        Plots and saves individual stress distribution plots for each dataset.
        """
        # Apply font family globally for this figure
        plt.rcParams["font.family"] = font_name

        for data in self.datasets:
            plt.figure()
            plt.plot(data["path_length"], data["stress"], label=data["label"], linewidth=line_width)

            plt.xlabel("Path length", fontsize=font_size)
            plt.ylabel("S$_{22}$ nominal stress", fontsize=font_size)
            plt.title(f"Stress Distribution - {data['label']}", fontsize=font_size)
            plt.legend(fontsize=font_size)
            plt.grid(True, linestyle="--", alpha=0.6)
            plt.tight_layout()

            # Save with a clean filename based on the label
            save_path = os.path.join(self.output_dir, f"{data['label'].replace(' ', '_')}.png")
            plt.savefig(save_path, dpi=300)
            print(f"Saved: {save_path}")
            plt.close()

    def plot_combined(self, line_width=2.0, font_name="Times New Roman"):
        """
        Plots and saves a combined stress distribution plot for all datasets.
        """
        plt.figure(figsize=(10, 6))
        
        # Apply font globally for this figure
        plt.rcParams["font.family"] = font_name

        # Define a list of line styles to cycle through
        line_styles = ['--', '-.', '-', ':']

        for idx, data in enumerate(self.datasets):
            style = line_styles[idx % len(line_styles)]  # Cycle through styles
            plt.plot(data["path_length"], data["stress"], label=data["label"],
                    linewidth=line_width, linestyle=style)

        plt.xlabel("Path length (mm)", fontsize=18)
        plt.ylabel(r"Stress Concentration Factor $K_t = \sigma_{max} / \sigma_{nom}$", fontsize=18)
        plt.title("Combined Stress Distribution", fontsize=24)
        plt.legend(prop={"family": font_name, "size": 16})
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()

        combined_save_path = os.path.join(self.output_dir, "Combined_Stress_Distribution.png")
        plt.savefig(combined_save_path, dpi=300)
        plt.show()
        print(f"Saved: {combined_save_path}")
        plt.close()
        
    def plot_first_values(self, divisor=1.0, font_name="Times New Roman"):
        """
        Extracts the first stress value from each dataset,
        divides it by a constant (divisor),
        and plots it against the number of elements (real mesh size).
        """
        if not self.datasets:
            raise RuntimeError("No datasets loaded. Run read_files() first.")

        # mapping mesh index -> elements
        mesh_info = {
            1: 116,     # Mesh1
            2: 180,     # Mesh2
            3: 352,     # Mesh3
            4: 676,     # Mesh4
            5: 1552,    # Mesh5
            6: 4948,    # Mesh6
            7: 16424,   # Mesh7
            8: 97042,   # Mesh8
        }

        mesh_elements = []
        first_values = []

        for idx, data in enumerate(self.datasets, start=1):
            if idx not in mesh_info:
                continue  # skip if we don't know the element count

            first_val = data["stress"].iloc[0] / divisor
            mesh_elements.append(mesh_info[idx])
            first_values.append(first_val)

        # Plot
        plt.figure(figsize=(8, 5))
        plt.rcParams["font.family"] = font_name
        plt.plot(mesh_elements, first_values, marker="o", linestyle="-", linewidth=2)

        plt.xlabel("Number of Mesh Elements", fontsize=14)
        plt.ylabel(r"$K_t$", fontsize=14)
        plt.title("Stress Concentration Value vs Mesh Density", fontsize=16)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()

        save_path = os.path.join(self.output_dir, "First_Stress_vs_Mesh.png")
        plt.savefig(save_path, dpi=300)
        plt.show()
        print(f"Saved: {save_path}")
        plt.close()


def main():
    # Explicitly set resource_dir to your resources folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    resource_dir = os.path.join(script_dir, "../resources")  # adjust as needed
    picture_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(picture_dir, "../res")  # adjust as needed
    processor = MeshStressProcessor(resource_dir=resource_dir, output_dir=results_dir)
    processor.read_files()
    processor.plot_individual()
    processor.plot_combined()
    processor.plot_first_values(divisor=1.0)


if __name__ == "__main__":
    main()



