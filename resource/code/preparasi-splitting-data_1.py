data_path = "/content/drive/My Drive/Kuliah/Penambangan Data/CNN"

IMAGE_SIZE = 224 #model input size
BATCH_SIZE = 64

datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale = 1./255,
    validation_split=0.2)

train_generator = datagen.flow_from_directory(
    data_path,
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size = BATCH_SIZE,
    subset='training')

val_generator = datagen.flow_from_directory(
    data_path,
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size = BATCH_SIZE,
    subset='validation')
