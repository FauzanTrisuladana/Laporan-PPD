epochs = 20
history = model.fit(train_generator,
                    epochs=epochs,
                    validation_data=val_generator)
loss, acc = model.evaluate(val_generator, verbose=1)
