import streamlit as st
import sqlite3
import pandas as pd


db_path = 'C:\Database\Sqldb\question_bank.db'  # Replace with your database path
# Database connection


def get_grades():
    conn = sqlite3.connect(db_path)  # Replace with your database path
    cursor = conn.cursor()
    query = "SELECT DISTINCT grade_id FROM Grade order by grade_id"
    cursor.execute(query)
    grades = cursor.fetchall()
    conn.close()
    return [s[0] for s in grades]
# Streamlit UI
st.title("Practice Questions Generator")
st.write("Select grade, subject and choose topic and subtopics to generate practice questions.")

grades = get_grades()
grade = st.selectbox("Select Grade", grades)  # Replace with dynamic grades from your database
# Fetch subjects dynamically based on the selected grade
def get_subjects(grade):
    conn = sqlite3.connect(db_path)  # Replace with your database path
    cursor = conn.cursor()
    query = "SELECT DISTINCT subject_name FROM Question WHERE grade_id = ?"
    cursor.execute(query, (grade,))
    subjects = cursor.fetchall()
    conn.close()
    return [s[0] for s in subjects]

subjects = get_subjects(grade)
subject = st.selectbox("Select Subject", subjects)

def get_topics(grade,subject):
    conn = sqlite3.connect(db_path)  # Replace with your database path
    cursor = conn.cursor()
    query = "SELECT DISTINCT topic_name FROM Question WHERE grade_id = ? and subject_name = ?"
    cursor.execute(query, (grade,subject))
    topics = cursor.fetchall()
    conn.close()
    return [s[0] for s in topics]

topics = get_topics(grade,subject)
selected_topic = st.selectbox("Select a Topic", topics)


def get_subtopic(grade,subject,selected_topic):
    conn = sqlite3.connect(db_path)  # Replace with your database path
    cursor = conn.cursor()
    query = "SELECT DISTINCT subtopic_name FROM Question WHERE grade_id = ? and subject_name = ? and topic_name = ?"
    cursor.execute(query, (grade,subject,selected_topic))
    sub_topics = cursor.fetchall()
    conn.close()
    return [s[0] for s in sub_topics]

def get_questions(grade,subject,topic, subtopics):
    conn = sqlite3.connect(db_path)  # Replace with your database path
    cursor = conn.cursor()
    placeholders = ', '.join(['?'] * len(subtopics))
    query = f"""
        SELECT question_text ,question_id    
        FROM Question
        WHERE grade_id = ? and subject_name = ? and topic_name = ? 
    """
    #######and subtopic_name IN ({placeholders})
    #cursor.execute(query, [topic] + subtopics)
    #cursor.execute(query, (grade,subject,topic, placeholders))
    cursor.execute(query, (grade,subject,topic))
    questions = cursor.fetchall()
    conn.close()
    return [{"question_text": q[0], "question_id": q[1]} for q in questions]

def get_options(question_id):
    conn = sqlite3.connect(db_path)  # Replace with your database path
    cursor = conn.cursor()
    query = "SELECT option_a, option_b, option_c, option_d FROM Question WHERE question_id = ?"
    cursor.execute(query, (question_id,))
    options = cursor.fetchall()
    print(options)
    options_list = options[0]
    # Create DataFrame
    
    print(options_list)
    conn.close()
    return options_list

# Subtopic selection
if selected_topic:
    subtopics = get_subtopic(grade,subject,selected_topic)
    #available_subtopics = subtopics.get(selected_topic, [])
    selected_subtopics = st.multiselect("Select up to 3 Subtopics", subtopics, max_selections=3)

    # Fetch and display questions
    if st.button("Fetch Questions"):
        if selected_subtopics:
            questions = get_questions(grade, subject, selected_topic, selected_subtopics)

            if questions:
                st.write("### Questions:")
                for i, question in enumerate(questions, 1):
                    st.write(f"{i}. {question['question_text']}")
                    options = get_options(question['question_id'])
                    print(options)
                    #df = pd.DataFrame(options, columns=["Option A", "Option B", "Option C", "Option D"])
                    
                    if options:
                        #st.radio(f"Options {i}", ["Option A", "Option B", "Option C", "Option D"], key=f"question_{i}")
                        selected_answer = st.radio(f"Answers", options)
                        #############st.write(f"Options: A) {options[0]}, B) {options[1]}, C) {options[2]}, D) {options[3]}")   
                        #st.write(f"Options: A) {options[0]}, B) {options[1]}, C) {options[2]}, D) {options[3]}")
                    else:
                        st.write("No options available for this question.")
                    
                print(questions)

           