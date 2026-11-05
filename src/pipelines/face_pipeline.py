

import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector() 


    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)

    encodings= []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) #128 embedding

        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource
def get_trained_model():
    X = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embedding = student.get('face_embedding')
        student_id = student.get('student_id')

        if embedding is not None and student_id is not None:
            X.append(np.array(embedding, dtype=float))
            y.append(int(student_id))

    # No face embeddings available
    if len(X) == 0:
        return None

    # SVC needs at least two different students
    if len(set(y)) < 2:
        return None

    clf = SVC(
        kernel='linear',
        probability=True,
        class_weight='balanced'
    )

    # Train the classifier
    clf.fit(X, y)

    return {
        'clf': clf,
        'X': X,
        'y': y
    }

def train_classifier():
    st.cache_resource.clear()

    model_data = get_trained_model()

    if model_data is None:
        return False

    return True

def predict_attendance(class_image_np):

    encodings = get_face_embeddings(class_image_np)

    detected_student = {}

    model_data = get_trained_model()

    if model_data is None:
        return detected_student, [], len(encodings)

    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['y']

    all_students = sorted(set(y_train))

    for encoding in encodings:

        predicted_id = int(clf.predict([encoding])[0])

        student_indices = [
            i for i, student_id in enumerate(y_train)
            if student_id == predicted_id
        ]

        best_match_score = min(
            np.linalg.norm(X_train[i] - encoding)
            for i in student_indices
        )

        resemblance_threshold = 0.6

        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True

    return detected_student, all_students, len(encodings)