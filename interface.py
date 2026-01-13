import streamlit as st
import time
from main import run_nexus_system, get_system_explanation


st.set_page_config(page_title="NEXUS-AI | Multi-Agent", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    /* Dark Theme background */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    /* Agent Card Styling */
    .agent-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    .planner-header { color: #00D4FF; font-weight: bold; }
    .solver-header { color: #BB86FC; font-weight: bold; }
    .critic-header { color: #CF6679; font-weight: bold; }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        background: linear-gradient(45deg, #00D4FF, #BB86FC);
        color: white;
        border: none;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)


if 'nexus_data' not in st.session_state:
    st.session_state.nexus_data = None


col_h1, col_h2 = st.columns([4, 1])
with col_h1:
    st.title("⚡ NEXUS-AI")
    st.write("Autonomous Decision Engine • Version 2.0")

with st.sidebar:
    st.header("⚙️ Control Panel")
    st.info("System: Online")
    st.write("**Model:** Llama 3.3 (70B)")
    st.write("**Speed:** ~250 tokens/sec")
    st.divider()
    if st.button("Reset Environment"):
        st.session_state.nexus_data = None
        st.rerun()


query = st.text_input("Define the problem statement:", placeholder="Ex: Solve the global microchip shortage logic...")

if st.button("ACTIVATE AGENTS"):
    if query:
        st.session_state.nexus_data = {"task": query}
        

        c1, c2, c3 = st.columns(3)

        planner_box = c1.empty()
        solver_box = c2.empty()
        critic_box = c3.empty()

        for tag, content in run_nexus_system(query):
            if tag == "RES_PLANNER":
                st.session_state.nexus_data["plan"] = content
                planner_box.markdown(f"<div class='agent-card'><span class='planner-header'>📍 PLANNER</span><br><br>{content}</div>", unsafe_allow_html=True)
            
            if tag == "RES_SOLVER":
                solver_box.markdown(f"<div class='agent-card'><span class='solver-header'>🧠 REASONING</span><br><br>{content}</div>", unsafe_allow_html=True)
            
            if tag == "RES_CRITIC":
                st.session_state.nexus_data["critique"] = content
                critic_box.markdown(f"<div class='agent-card'><span class='critic-header'>❌ CRITIC</span><br><br>{content}</div>", unsafe_allow_html=True)
            
            if tag == "ST_REPLAN":
                st.warning("⚠️ Critic Flaw Detected: Re-calculating final solution...")

            if tag == "FINAL":
                st.session_state.nexus_data["final"] = content
                st.divider()
                st.subheader("🏁 Final Validated Result")
                st.success(content)
                st.balloons()

if st.session_state.nexus_data and "final" in st.session_state.nexus_data:
    if st.button("Deep Explain (System Reasoning)"):
        explanation = get_system_explanation(
            st.session_state.nexus_data["task"],
            st.session_state.nexus_data["plan"],
            st.session_state.nexus_data["critique"]
        )
        st.markdown(f"### 🧠 Neural Trace:\n{explanation}")