
import streamlit as st
import pandas as pd
from datetime import datetime

from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase
from src.components.dialog_attendance_results import show_attendance_result


@st.dialog('Voice Attendance')
def voice_attendance_dialog(selected_subject_id):

    st.write(
        'Record audio of students saying "I am present". '
        'Then AI will recognize the students.'
    )

    audio_data = st.audio_input("Record classroom audio")

    if st.button('Analyze Audio', width='stretch', type='primary'):

        # Check whether audio was recorded
        if audio_data is None:
            st.warning("Please record audio before clicking Analyze Audio.")
            return

        with st.spinner('Processing audio data...'):

            # Step 1: Fetch enrolled student IDs
            enrolled_res = (
                supabase.table('subject_students')
                .select('student_id')
                .eq('subject_id', selected_subject_id)
                .execute()
            )

            enrolled_rows = enrolled_res.data

            student_ids = [
                row['student_id']
                for row in enrolled_rows
                if row.get('student_id') is not None
            ]

            if not student_ids:
                st.warning('No students enrolled in this course')
                return

            # Step 2: Fetch student details separately
            students_res = (
                supabase.table('students')
                .select('*')
                .in_('student_id', student_ids)
                .execute()
            )

            enrolled_students = students_res.data

            if not enrolled_students:
                st.warning('No student records found')
                return

            # Step 3: Get students with voice embeddings
            candidates_dict = {
                student['student_id']: student['voice_embedding']
                for student in enrolled_students
                if student.get('voice_embedding')
            }

            if not candidates_dict:
                st.error('No enrolled students have registered voice profiles.')
                return

            # Step 4: Process audio
            audio_bytes = audio_data.read()

            detected_scores = process_bulk_audio(
                audio_bytes,
                candidates_dict
            )

            results = []
            attendance_to_log = []

            current_timestamp = datetime.now().strftime(
                "%Y-%m-%dT%H:%M:%S"
            )

            # Step 5: Prepare attendance results
            for student in enrolled_students:

                student_id = student['student_id']

                score = detected_scores.get(student_id, 0.0)
                is_present = score > 0

                results.append({
                    "Name": student['name'],
                    "ID": student_id,
                    "Source": score if is_present else "-",
                    "Status": (
                        "✅ Present" if is_present
                        else "❌ Absent"
                    )
                })

                attendance_to_log.append({
                    'student_id': student_id,
                    'subject_id': selected_subject_id,
                    'timestamp': current_timestamp,
                    'is_present': bool(is_present)
                })

            st.session_state.voice_attendance_results = (
                pd.DataFrame(results),
                attendance_to_log
            )

    # Step 6: Show attendance confirmation
    if st.session_state.get('voice_attendance_results'):

        st.divider()

        df_results, logs = st.session_state.voice_attendance_results

        show_attendance_result(df_results, logs)
