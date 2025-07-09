import streamlit as st
import wikipedia
import cv2
import matplotlib.pyplot as plt
import numpy as np
from speech_module import recognize_speech, speak_text  # <- use your module

# ========== Simple Assistant
class SimpleAssistant:
    def __init__(self):
        self.history = []

    def smart_answer(self, question):
        try:
            summary = wikipedia.summary(question, sentences=2)
        except:
            summary = "Sorry, I couldn't find a good answer for that. Can you rephrase?"
        self.history.append((question, summary))
        return summary

assistant = SimpleAssistant()

# ========== Face detection
def analyze_face_basic():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    emotion = "No face detected"
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        emotion = "Face detected" if len(faces) > 0 else "No face detected"
    cap.release()
    return emotion

# ========== Visual aids
def show_chart(topic):
    if "probability" in topic or "data" in topic or "trend" in topic:
        st.subheader("📊 Related Chart")
        x = np.arange(1,6)
        y = np.random.randint(5,15, size=5)
        fig, ax = plt.subplots()
        ax.bar(x, y, color='#4db6ac')
        ax.set_title("Sample Data / Probability Chart")
        st.pyplot(fig)

def show_diagram(topic):
    if "flip flop" in topic:
        st.subheader("🖼 SR Flip Flop Diagram")
        st.image("sr_flip_flop.png", use_column_width=True)
    elif "neural network" in topic:
        st.subheader("🧠 Neural Network Diagram")
        st.image("perceptron_diagram.png", use_column_width=True)

# ========== Custom styling
st.markdown("""
    <style>
        body {
            color: #eee !important;
            background-color: #0e1117 !important;
        }
        .card {
            background-color: #1c1f24;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }
        .highlight {
            background-color: #263238;
            border-left: 6px solid #4db6ac;
            color: #fafafa;
            padding: 15px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ========== Sidebar
st.sidebar.markdown("### 📝 Q&A History")
if assistant.history:
    for q, a in assistant.history[::-1]:
        with st.sidebar.expander(f"❓ {q}"):
            st.markdown(f"<div style='color:#ccc'>{a}</div>", unsafe_allow_html=True)
else:
    st.sidebar.info("Ask something to start building history!")

# ========== Main layout
st.markdown("<h1 style='text-align: center; color: #90caf9;'>🚀 AI Classroom Assistant</h1>", unsafe_allow_html=True)

# --- Ask anything ---
col1, col2 = st.columns([2,1])
with col1:
    st.subheader("💬 Ask Me Anything")
    question = st.text_input("Type your question here:")
    if st.button("🎤 Speak Your Question"):
        spoken_text = recognize_speech()
        question = spoken_text
        st.success(f"Recognized: {spoken_text}")
    if st.button("💡 Get Answer"):
        answer = assistant.smart_answer(question)
        st.success(f"**AI:** {answer}")
        speak_text(answer)
        show_chart(question.lower())
        show_diagram(question.lower())
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='card' style='text-align:center;'>
            <h3>🤖 About</h3>
            <p>Ask by typing or speaking. I’ll answer & show visual aids.</p>
            <p>Try: <i>"Probability trends"</i> or <i>"SR Flip Flop"</i></p>
        </div>
    """, unsafe_allow_html=True)

# --- Engagement check ---
col3, col4 = st.columns([1,2])
with col3:
    st.subheader("🧑‍🎓 Engagement")
    if st.button("📷 Check Webcam"):
        result = analyze_face_basic()
        if "No face" in result:
            st.error("No face detected. Possibly distracted.")
        else:
            st.success("Face detected. Attentive!")
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class='highlight'>
            <h4>🎯 Why engagement checks?</h4>
            <p>Face checks detect attention. Fewer faces = slow down, repeat; more faces = continue.</p>
        </div>
    """, unsafe_allow_html=True)
st.markdown("<center><small style='color:grey;'>Built with ❤️ using Streamlit — by Krish&Aonusha </small></center>", unsafe_allow_html=True)
