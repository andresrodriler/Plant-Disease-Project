"""
Loads PlantVillage, filters to a crop according to configs/<crop>.yaml settings, applies transforms and augmentation, returns train/val/test loaders and the class names

Output, return this so train.py can use it:

get_dataloaders(crop, batch_size=32) -> dict with:
    "train":        DataLoader   # augmented, shuffled
    "val":          DataLoader   # no augmentation, not shuffled
    "test":         DataLoader   # no augmentation, not shuffled
    "class_names":  list[str]    # ordered; index i is label i
    "class_counts": list[int]    # training images per class, same order

Notes (details that keep data.py and train.py in sync):
    - Each batch is (images, labels). images: float tensor [batch, 3, 224, 224],
    ImageNet-normalized (mean 0.485, 0.456, 0.406; std 0.229, 0.224, 0.225).
    labels: long tensor [batch].
    - Use the official train/test split. Make val from train, grouped by leaf_id,
    so photos of the same leaf stay in one split.
    - Build class_names with sorted() so label numbers never change between runs.
    - Also provide get_eval_transform() (resize + normalize, no augmentation)
    so the demo app preprocesses photos the same way as val/test.
    
"""