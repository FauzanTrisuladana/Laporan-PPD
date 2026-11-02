for _ in range(5):
    img, label = next(train_generator)
    print(img.shape)
    plt.imshow(img[0])
    plt.show()
