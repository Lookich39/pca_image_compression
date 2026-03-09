# PCA Image Compression Pipeline

Это проект для **сжатия изображений с помощью метода главных компонент (PCA)** с автоматическим подбором оптимального числа компонент с использованием **SSIM (Structural Similarity Index)** и метода локтя.  

Проект поддерживает **JPEG и PNG** изображения и показывает прогресс с помощью **tqdm**.

---

## Возможности

- Сжатие изображений с использованием PCA.
- Автоматический подбор оптимального числа компонент (`k`) с помощью **метода локтя**.
- Поддержка RGB изображений.
- Поддержка форматов: `.jpg`, `.jpeg`, `.png`.
- Вывод прогресс-баров для обработки всех изображений и для каждой кривой SSIM.
- Визуализация кривой SSIM и найденного локтя (опционально).
- Организация входных и выходных изображений через папки `input/` и `output/`.

---

## Установка

1. Клонируйте репозиторий:

```bash
git clone <repo_url>
cd pca_compression
```

2. Клонируйте репозиторий:

```bash
pip install -r requirements.txt
```

## Структура проекта

pca_compression/
input/              # входные изображения  
output/             # сжатые изображения  
compressor.py       # PCA логика  
metrics.py          # Метрики качества (SSIM)  
elbow.py            # Метод локтя (Kneedle)  
visualizer.py       # Визуализация  
main.py             # Pipeline для запуска


## Использование

1. Подготовка

&nbsp;&nbsp;&nbsp;&nbsp;Поместите изображения в папку input/.  
&nbsp;&nbsp;&nbsp;&nbsp;Поддерживаются форматы: .jpg, .jpeg, .png.

2. Запуск pipeline

```bash
python main.py
```
По умолчанию:
Максимальное число компонент: 20
Визуализация кривой SSIM отключена

3. Включение визуализации

```bash
pipeline = PCACompressionPipeline(
    input_dir="input",
    output_dir="output",
    max_components=20,
    visual=True
)

pipeline.run()
```

## License

Copyright В© 2026 Alexey Kudryavtsev. See [LICENSE](LICENSE) for details.
