import numpy as np
from tqdm import tqdm

from compressor import PCACompressor
from metrics import ImageMetrics


class ElbowFinder:
    """Find optimal PCA components using SSIM elbow method."""

    def __init__(self, compressor: PCACompressor, metrics: ImageMetrics):
        self.compressor = compressor
        self.metrics = metrics

    def compute_ssim_curve(self, img, max_components):
        ssim_scores = []

        for k in tqdm(range(1, max_components + 1), desc="Computing SSIM"):
            reconstructed = self.compressor.compress_image(img, k)

            score = self.metrics.ssim_image(img, reconstructed)
            ssim_scores.append(score)

        return np.array(ssim_scores)

    def find_elbow(self, ssim_scores, min_components=7):

        k = np.arange(1, len(ssim_scores) + 1)

        # normalization
        k_norm = (k - k.min()) / (k.max() - k.min())
        ssim_norm = (ssim_scores - ssim_scores.min()) / (ssim_scores.max() - ssim_scores.min())

        diff = ssim_norm - k_norm

        # ignore components < min_components
        diff[:min_components - 1] = -np.inf

        best_component = np.argmax(diff) + 1

        return best_component