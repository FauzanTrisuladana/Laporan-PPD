for image_batch, label_batch in train_generator:
    break

print(f"Image batch shape: {image_batch.shape}")
print(f"Label batch shape: {label_batch.shape}")

IMG_SHAPE = (IMAGE_SIZE, IMAGE_SIZE, 3)

num_classes = 2
