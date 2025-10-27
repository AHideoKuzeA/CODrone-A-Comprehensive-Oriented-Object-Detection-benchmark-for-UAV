import os
import cv2
import numpy as np


def draw_boxes(image_path, label_path, output_path=None, class_colors=None, thickness=2):
    """
    Draw oriented bounding boxes (OBB) from DOTA-format annotations.

    Args:
        image_path (str): Path to the input image.
        label_path (str): Path to the  annotation (.txt) file.
        output_path (str, optional): Path to save the output image. If None, only display.
        class_colors (dict[str, tuple[int, int, int]], optional): 
            Mapping of class name to BGR color, e.g. {"plane": (0,255,0)}.
            Defaults to green if not provided.
        thickness (int, optional): Line thickness of the bounding box. Defaults to 2.
    """
    # Load the image
    image = cv2.imread(image_path)

    # Read labels
    with open(label_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()

        # Parse coordinates and reshape to (4, 2)
        coords = np.array(list(map(float, parts[:8]))).reshape(4, 2).astype(np.int32)
        cls_name = parts[8]
        color = class_colors.get(cls_name, (0, 255, 0)) if class_colors else (0, 255, 0)

        # Draw oriented bounding box
        cv2.polylines(image, [coords], isClosed=True, color=color, thickness=thickness)

        # Draw class label text at box center
        cx, cy = np.mean(coords, axis=0).astype(int)
        cv2.putText(
            image, cls_name, (cx, cy),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA
        )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, image)
    # print(f"[INFO] Saved visualization -> {output_path}")


def main():
    """Batch visualization of DOTA-format ground truth annotations."""
    img_dir = "your image directory"
    label_dir = "your label directory"
    output_dir = "your output directory"

    os.makedirs(output_dir, exist_ok=True)

    for img_name in os.listdir(img_dir):
        if not img_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tif')):
            continue

        img_path = os.path.join(img_dir, img_name)
        label_path = os.path.join(label_dir, os.path.splitext(img_name)[0] + ".txt")
        out_path = os.path.join(output_dir, img_name)

        draw_boxes(img_path, label_path, out_path)


if __name__ == "__main__":
    main()
