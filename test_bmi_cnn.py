import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

# =========================================================
# CONFIGURATION
# =========================================================
MODEL_PATH = os.path.join("models", "bmi_category_cnn_sequential.h5")  # Path to your saved Sequential model
TEST_DIR = os.path.join("data", "test")                   # Folder containing test images by class
IMG_SIZE = (224, 224)                                     # Must match training image size
BATCH_SIZE = 32

# =========================================================
# LOAD TRAINED MODEL
# =========================================================
print("Loading trained Sequential CNN model...")
model = tf.keras.models.load_model(MODEL_PATH)
model.summary()

# =========================================================
# PREPARE TEST DATASET
# =========================================================
print("\nPreparing test dataset...")

test_datagen = ImageDataGenerator(rescale=1.0/255.0)

test_generator = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',  # Use 'binary' if there are only 2 classes
    shuffle=False
)

# =========================================================
# EVALUATE MODEL
# =========================================================
print("\nEvaluating model on test images...")
test_loss, test_acc = model.evaluate(test_generator, verbose=2)

print(f"\nTest Accuracy: {test_acc:.4f}")
print(f"Test Loss: {test_loss:.4f}")

# =========================================================
# CONFUSION MATRIX AND CLASSIFICATION REPORT
# =========================================================
print("\nGenerating classification report...")

# Predict class probabilities
Y_pred = model.predict(test_generator)
y_pred = np.argmax(Y_pred, axis=1)

# True labels
true_classes = test_generator.classes
class_labels = list(test_generator.class_indices.keys())

# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(true_classes, y_pred))

# Classification report
print("\nClassification Report:")
print(classification_report(true_classes, y_pred, target_names=class_labels))
