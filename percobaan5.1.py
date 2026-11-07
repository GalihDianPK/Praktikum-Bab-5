import cv2
import numpy as np

# ==============================
# Konfigurasi
# ==============================
INPUT_PATH = "foto1.png"  # Ganti dengan lokasi gambar Anda
THRESHOLD_VALUE = 127

EDGE_KERNEL = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1],
])


def load_image(path):
    """Membaca gambar dari path; error jika gagal."""
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Gambar tidak ditemukan: {path}")
    return img


def extract_rgb(img_bgr):
    """Mengubah urutan channel BGR (OpenCV) menjadi RGB."""
    b, g, r = cv2.split(img_bgr)
    return cv2.merge([r, g, b])


def to_grayscale(img_bgr):
    """Konversi gambar ke grayscale."""
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)


def binarize(gray, threshold=THRESHOLD_VALUE):
    """Threshold & binarisasi sederhana."""
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    return binary


def convolve(gray, kernel=EDGE_KERNEL):
    """Konvolusi dengan kernel (default: edge detection)."""
    return cv2.filter2D(gray, -1, kernel)


def main():
    img = load_image(INPUT_PATH)

    rgb_image = extract_rgb(img)
    print("RGB Extraction selesai.")

    gray = to_grayscale(img)
    print("Grayscale selesai.")

    binary = binarize(gray)
    print("Threshold & Binarization selesai.")

    convolved = convolve(gray)
    print("Convolution selesai.")

    # Simpan hasil preprocessing
    outputs = {
        "hasil_rgb.jpg": rgb_image,
        "hasil_gray.jpg": gray,
        "hasil_binary.jpg": binary,
        "hasil_convolution.jpg": convolved,
    }
    for filename, result in outputs.items():
        cv2.imwrite(filename, result)
    print("Semua hasil berhasil disimpan.")


if __name__ == "__main__":
    main()
