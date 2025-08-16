import streamlit as st
import time

# Questions and Choices (10 questions)
quiz = [
    {"question": "Which language is used for Data Science?", "choices": ["Java", "Python", "HTML", "C++"], "answer": "Python"},
    {"question": "Who developed Python?", "choices": ["Elon Nusk","Guido van Rossum", "Dennis Ritchie", "Mark Zuckerberg"], "answer": "Guido van Rossum"},
    {"question": "What is 2*5?", "choices": ["7", "10", "20", "12"], "answer": "10"},
    {"question": "Which of these is a Python web framework?", "choices": ["Flutter", "React", "Angular", "Django"], "answer": "Django"},
    {"question": "What does CPU stand for?", "choices": ["Central Program Unit", "Central Processing Unit", "Computer Personal Unit", "Central Performance Unit"], "answer": "Central Processing Unit"},
    {"question": "HTML is used to create what?", "choices": ["Web pages", "Software", "Operating Systems", "Databases"], "answer": "Web pages"},
    {"question": "Which company created the Java programming language?", "choices": ["Apple", "Sun Microsystems", "Google", "Microsoft"], "answer": "Sun Microsystems"},
    {"question": "Which one is a Python data type?", "choices": ["String", "Boolean", "List", "All of the above"], "answer": "All of the above"},
    {"question": "What is the value of pi (approx)?", "choices": ["3.12", "3.14", "3.41", "3.24"], "answer": "3.14"},
    {"question": "Which symbol is used to comment a single line in Python?", "choices": ["//", "#", "/*", "--"], "answer": "#"}
]

# Initialize session state for score and selected answers
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'submitted' not in st.session_state:
    st.session_state.submitted = [False]*len(quiz)
if 'selected' not in st.session_state:
    st.session_state.selected = [None]*len(quiz)
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

st.title("🔢 Advanced Quiz App")
st.write("Test your knowledge! Each correct answer gives you 1 point. Timer included.")

# Timer (show seconds spent on page)
elapsed = int(time.time() - st.session_state.start_time)
st.write(f"⏰ Elapsed Time: {elapsed} seconds")

for idx, item in enumerate(quiz):
    st.subheader(f"Q{idx+1}: {item['question']}")
    selected = st.radio(f"Choices for Q{idx+1}", item["choices"], key=f"radio_{idx}")
    
    if st.button(f"Submit Q{idx+1}", key=f"submit_{idx}"):
        st.session_state.selected[idx] = selected
        if not st.session_state.submitted[idx]:
            st.session_state.submitted[idx] = True
            if selected == item["answer"]:
                st.success("✅ Correct Answer!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! Correct Answer: {item['answer']}")
        else:
            st.info("You already submitted this question.")

# Final Score display
if all(st.session_state.submitted):
    st.write("---")
    st.markdown(f"## 🎉 Final Score: {st.session_state.score}/{len(quiz)}")
    if st.session_state.score == len(quiz):
        st.success("Excellent! All Correct.")
    elif st.session_state.score >= len(quiz)//2:
        st.info("Good Attempt, keep practicing!")
    else:
        st.warning("Try Again!")

# Reset Button
if st.button("Restart Quiz"):
    st.session_state.score = 0
    st.session_state.submitted = [False]*len(quiz)
    st.session_state.selected = [None]*len(quiz)
    st.session_state.start_time = time.time()
    st.rerun()