import numpy as np
from sklearn.decomposition import PCA


class PCACompressor:
    """Performs PCA compression for RGB images."""

    def compress_channel(self, channel, n_components):
        pca = PCA(n_components=n_components)

        compressed = pca.fit_transform(channel)
        reconstructed = pca.inverse_transform(compressed)

        return reconstructed

    def compress_image(self, img, n_components):
        reconstructed = np.zeros_like(img)

        for i in range(3):
            reconstructed[:, :, i] = self.compress_channel(
                img[:, :, i],
                n_components
            )

        return reconstructed