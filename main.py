import cv2
import numpy as np
from pathlib import Path
from tqdm import tqdm

from compressor import PCACompressor
from elbow import ElbowFinder
from metrics import ImageMetrics
from visualizer import ElbowVisualizer


class PCACompressionPipeline:
    """Full pipeline for PCA compression."""

    def __init__(
        self,
        input_dir="input",
        output_dir="output",
        max_components=20,
        visual=False
    ):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.max_components = max_components
        self.visual = visual

        self.output_dir.mkdir(exist_ok=True)

        self.compressor = PCACompressor()
        self.metrics = ImageMetrics()
        self.elbow_finder = ElbowFinder(self.compressor, self.metrics)
        self.visualizer = ElbowVisualizer()

    def process_image(self, image_path):

        img = cv2.imread(str(image_path))

        if img is None:
            print(f"Cannot read image: {image_path}")
            return

        img = img.astype(np.float32) / 255.0

        tqdm.write(f"\nProcessing {image_path.name}")

        # SSIM curve
        ssim_scores = self.elbow_finder.compute_ssim_curve(
            img,
            self.max_components
        )

        best_component = self.elbow_finder.find_elbow(ssim_scores)

        if self.visual:
            self.visualizer.draw(ssim_scores, self.max_components, best_component)

        tqdm.write(f"Optimal components: {best_component}")

        # compression
        compressed_img = self.compressor.compress_image(
            img,
            best_component
        )

        compressed_img = np.clip(
            compressed_img * 255,
            0,
            255
        ).astype(np.uint8)

        output_path = self.output_dir / f"compressed_{image_path.name}"

        cv2.imwrite(str(output_path), compressed_img)

        print(f"Saved: {output_path}")

    def run(self):

        SUPPORTED_FORMATS = [".jpg", ".jpeg", ".png"]

        images = [
            p for p in self.input_dir.iterdir()
            if p.suffix.lower() in SUPPORTED_FORMATS
        ]
        #images = list(self.input_dir.glob("image2.png"))

        if not images:
            print("No images found in input directory")
            return

        for image_path in tqdm(images, desc="Processing images"):
            self.process_image(image_path)


if __name__ == "__main__":

    pipeline = PCACompressionPipeline(
        input_dir="input",
        output_dir="output",
        max_components=20,
        visual=True
    )

    pipeline.run()