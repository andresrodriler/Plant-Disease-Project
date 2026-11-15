""" 
Builds the pretrained model, class-weighted loss, early stopping, use resnet18 swap last layer, saves the model and class list

Input, from data.py:
    d = get_dataloaders(crop)
    num_classes   = len(d["class_names"])
    class weights = total / (num_classes * count), computed from d["class_counts"]

Output, so the demo app can load it:
    models/<crop>.pth            model.state_dict()
    models/<crop>_classes.json   d["class_names"], in order

"""

