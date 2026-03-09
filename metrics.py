from skimage.metrics import structural_similarity as ssim

class ImageMetrics:
    """Quality metrics for images."""

    @staticmethod
    def ssim_image(original, reconstructed):
        return ssim(
            original,
            reconstructed,
            channel_axis=2,
            data_range=original.max() - original.min()
        )