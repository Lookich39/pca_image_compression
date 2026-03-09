from matplotlib import pyplot as plt


class ElbowVisualizer:
    """Visualization for elbow method."""

    @staticmethod
    def draw(ssim_scores, max_components, best_component):

        plt.figure()

        x = range(1, max_components + 1)

        plt.plot(x, ssim_scores)

        plt.annotate(
            f'Best k = {best_component}',
            xy=(best_component, ssim_scores[best_component - 1]),
            xytext=(best_component + 1, ssim_scores[best_component - 1] - 0.02),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=12,
            color='red'
        )

        plt.xticks(x)
        plt.xlabel("Number of components (k)")
        plt.ylabel("SSIM")
        plt.title("Elbow method using SSIM")
        plt.grid(True)

        plt.show()
