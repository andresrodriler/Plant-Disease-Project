"""
Loads PlantVillage, filters to a crop according to configs/<crop>.yaml settings, applies transforms and augmentation, returns train/val/test loaders and the class names

Output, return this so train.py can use it:

get_dataloaders(crop, batch_size=32) -> dict with:
    "train":        DataLoader   # augmented, shuffled
    "val":          DataLoader   # no augmentation, not shuffled
    "test":         DataLoader   # no augmentation, not shuffled
    "class_names":  list[str]    # ordered; index i is label i
    "class_counts": list[int]    # training images per class, same order

"""