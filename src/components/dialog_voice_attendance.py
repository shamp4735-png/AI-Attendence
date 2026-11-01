import streamlit as st

from src.pipeline.voice_attendance import process_voice_attendance
from src.database.config import supabase

st.dialog('voice Attendence')

def voice_attendance_dialog(selected_subject_id):
    st.write('Record audio of student saying I am present. Then AI will recognize the students')


    audio_data = None

    audio_data = st.audio_input("Record classroom audio")


    if st.button('Analyze Audio', width='stretch', type='primary'):
    
            with st.spinner('Processing audio...'):
                enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id',selected_subject_id ).execute()
                enrolled_students = enrolled_res.data
                
                if not enrolled_students:
                    st.warning('No students enrolled in this course')
                    return
                condidates_dict = {
                     s['student'] ['student_id'] : s['students'] ['voice_embedding']
                     for s in enrolled_students if s['student'].get('voice_embedding')
                }

                if not condidates_dict:
                     st.error('No enrolled students have voice profiless registred')
                     return

                audio_bytes = audio_data.read()

                detected_scores = process_voice_attendance(audio_bytes, condidates_dict)

                