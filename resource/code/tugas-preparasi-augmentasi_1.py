base_path = "/content/drive/My Drive/Kuliah/Penambangan Data/Intel Image Classification"
train_path = base_path + "/seg_train/seg_train"
val_path = base_path + "/seg_test/seg_test"

IMAGE_SIZE = 150
BATCH_SIZE = 64

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale = 1./255, rotation_range=20, zoom_range=0.2, horizontal_flip=True)
val_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale = 1./255)

train_generator = train_datagen.flow_from_directory(
    train_path,
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=True)

val_generator = val_datagen.flow_from_directory(
    val_path,
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=False)
