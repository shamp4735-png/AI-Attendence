
import streamlit as st
import numpy as np
from PIL import Image

from src.pipelines.face_pipeline import (
    get_face_embeddings,
    train_classifier
)

from src.database.db import update_student_face_embedding

st.title("Repair Student Face ID")

st.write("Update the face embedding for SM1 (Student ID: 2).")

photo = st.camera_input("Capture SM1's face")

if st.button("Update Face ID", type="primary"):

    if photo is None:
        st.warning("Please capture a face first.")

    else:
        img = np.array(Image.open(photo))

        with st.spinner("Processing face..."):
            encodings = get_face_embeddings(img)

            if len(encodings) == 0:
                st.error("No face detected. Please try again.")

            elif len(encodings) > 1:
                st.error("Multiple faces detected. Only one face is allowed.")

            else:
                face_embedding = encodings[0].tolist()

                response = update_student_face_embedding(
                    2,
                    face_embedding
                )

                if response:
                    model_trained = train_classifier()

                    st.success("SM1's face embedding updated successfully!")

                    if model_trained:
                        st.success("Face recognition model trained successfully!")
                    else:
                        st.warning(
                            "Face updated, but at least two valid student "
                            "profiles are required to train SVC."
                        )
                else:
                    st.error("Could not update the student record.")
