import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from keras.preprocessing.image import load_img, img_to_array
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization

# Parameters
IMG_DIR = r'height-weight-images/versions/1/'
CSV_PATH = 'data/image_category.csv'
IMG_SIZE = (224, 224)
BATCH_SIZE = 8
EPOCHS = 100

# Load CSV
df = pd.read_csv(CSV_PATH)
filenames = df['Filename'].values
labels = df['Category'].values

# Encode labels
le = LabelEncoder()
labels_encoded = le.fit_transform(labels)
labels_categorical = to_categorical(labels_encoded, num_classes=4)

# Load images

X = []
y = []
missing_files = []
for fname, label_cat in zip(filenames, labels_categorical):
    img_path = os.path.join(IMG_DIR, fname)
    if os.path.exists(img_path):
        img = load_img(img_path, target_size=IMG_SIZE)
        img_arr = img_to_array(img) / 255.0
        X.append(img_arr)
        y.append(label_cat)
    else:
        missing_files.append(img_path)

print(f"Total images loaded: {len(X)}")
if missing_files:
    print(f"Missing image files ({len(missing_files)}):")
    for mf in missing_files[:10]:  # Show only first 10 missing files
        print(mf)
    if len(missing_files) > 10:
        print(f"...and {len(missing_files)-10} more.")

X = np.array(X)
y = np.array(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(4, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))  # 4 classes

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# Train
model.fit(X_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_data=(X_test, y_test))

# Save model
model_save_path = os.path.join('models', 'bmi_category_cnn_sequential.h5')
os.makedirs('models', exist_ok=True)
model.save(model_save_path)
print(f"Model saved as {model_save_path}")
