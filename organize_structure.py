import os
import shutil

def create_directory_structure(base_path):
    dirs = [
        'config',
        'datasets/train',
        'datasets/valid',
        'datasets/test',
        'experiments/detect/train/weights',
        'src/opticalapp/spiders',
        'src/opticalapp/utils',
        'src/yolov8',
        'tests'
    ]
    for dir_name in dirs:
        path = os.path.join(base_path, dir_name)
        os.makedirs(path, exist_ok=True)

def move_files(base_path):
    # Move configuration files
    config_files = ['scrapy.cfg', 'data.yaml', 'README.dataset.txt']
    for file_name in config_files:
        src = os.path.join(base_path, 'opticalapp', file_name)
        dst = os.path.join(base_path, 'config', file_name)
        if os.path.exists(src):
            shutil.move(src, dst)

    # Move dataset files
    dataset_folders = ['train', 'valid', 'test']
    for folder in dataset_folders:
        src = os.path.join(base_path, 'opticalapp', 'dataset', folder)
        dst = os.path.join(base_path, 'datasets', folder)
        if os.path.exists(src):
            shutil.move(src, dst)

    # Move experiment results
    experiment_files = ['confusion_matrix_normalized.jpg', 'confusion_matrix.png', 'events.out.tfevents',
                        'F1_curve.png', 'labels_correlogram.jpg', 'labels.jpg', 'P_curve.png', 'PR_curve.png',
                        'R_curve.png', 'results.csv', 'results.png']
    for file_name in experiment_files:
        src = os.path.join(base_path, 'runs', 'detect', 'train', file_name)
        dst = os.path.join(base_path, 'experiments', 'detect', 'train', file_name)
        if os.path.exists(src):
            shutil.move(src, dst)

    # Move weights
    weights_src = os.path.join(base_path, 'runs', 'detect', 'train', 'weights')
    weights_dst = os.path.join(base_path, 'experiments', 'detect', 'train', 'weights')
    if os.path.exists(weights_src):
        shutil.move(weights_src, weights_dst)

    # Move spiders and utils
    spider_files = ['opticalspider.py', 'dessin_tactile.py']
    for file_name in spider_files:
        src = os.path.join(base_path, 'opticalapp', 'spiders', file_name)
        dst = os.path.join(base_path, 'src', 'opticalapp', 'spiders', file_name)
        if os.path.exists(src):
            shutil.move(src, dst)

    utils_files = ['redimensionner_images.py', 'extraire_images.py']
    for file_name in utils_files:
        src = os.path.join(base_path, 'opticalapp', file_name)
        dst = os.path.join(base_path, 'src', 'opticalapp', 'utils', file_name)
        if os.path.exists(src):
            shutil.move(src, dst)

    # Move YOLOv8 related files
    yolov8_files = ['train.py', 'predict.py', 'yolov8n.pt']
    for file_name in yolov8_files:
        src = os.path.join(base_path, 'opticalapp', file_name)
        dst = os.path.join(base_path, 'src', 'yolov8', file_name)
        if os.path.exists(src):
            shutil.move(src, dst)

    # Move test files
    test_files = ['test.csv']
    for file_name in test_files:
        src = os.path.join(base_path, 'opticalapp', file_name)
        dst = os.path.join(base_path, 'tests', file_name)
        if os.path.exists(src):
            shutil.move(src, dst)

def main():
    base_path = os.path.abspath('.')  
    create_directory_structure(base_path)
    move_files(base_path)

if __name__ == "__main__":
    main()