import os
from PIL import Image

def check_images(root_dir):
    bad_files = []
    total = 0
    for category in os.listdir(root_dir):
        cat_path = os.path.join(root_dir, category)
        if not os.path.isdir(cat_path):
            continue
        for fname in os.listdir(cat_path):
            fpath = os.path.join(cat_path, fname)
            total += 1
            try:
                with Image.open(fpath) as img:
                    img.verify()
            except Exception as e:
                bad_files.append((fpath, str(e)))
    print(f"Checked {total} files.")
    if bad_files:
        print(f"Found {len(bad_files)} invalid image files:")
        for f, err in bad_files:
            print(f"{f}: {err}")
    else:
        print("All images are valid.")

if __name__ == "__main__":
    check_images("data/test")
