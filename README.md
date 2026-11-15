# Plant-Disease-Project

```
Plant-Disease-Project/
├── app/             # demo app: pick a crop, upload a leaf, see predictions
├── configs/         # per-crop settings (one line to change, shared code)
│   ├── apple.yaml
│   ├── corn.yaml
│   ├── grape.yaml
│   └── tomato.yaml
├── models/          # saved weights + class lists (not committed)
├── data.py          # loads PlantVillage per crop -> dataloaders + class names
├── train.py         # pretrained ResNet18, training, early stopping, test metrics
├── main.py          # entry point
├── .gitignore       # ignores models/, *.pth, data, notebook outputs
└── README.md
```