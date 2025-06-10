import streamlit as st
import random
import uuid

st.set_page_config(page_title="🧬 Digital Cell Simulator")

st.title("🧬 Digital Cell Simulator")

# Available specializations
specializations = ["Energy", "Mathematics", "Physics", "Biology", "AI"]

# Knowledge base
global_knowledge = [
    "Solar energy generation",
    "Efficient energy storage",
    "Energy consumption analysis"
]

class DigitalCell:
    def __init__(self, generation):
        self.id = str(uuid.uuid4())[:8]
        self.generation = generation
        self.specialization = random.choice(specializations)
        self.knowledge = global_knowledge.copy()
        self.knowledge.append(f"New tech in {self.specialization}")
        self.optimized_knowledge = self.optimize_knowledge()
        self.logical_question = f"How can we improve {self.specialization.lower()} using existing knowledge?"

    def optimize_knowledge(self):
        return self.knowledge[-4:]  # Last 4 items only

    def display(self):
        st.markdown(f"**Cell ID:** `{self.id}` | **Generation:** {self.generation}")
        st.markdown(f"**Specialization:** `{self.specialization}`")
        st.markdown("**Knowledge:**")
        st.json(self.knowledge)
        st.markdown("**Logical Question:**")
        st.write(self.logical_question)
        st.markdown("**Optimized Knowledge:**")
        st.json(self.optimized_knowledge)
        st.markdown("---")

# Create cells
if st.button("Generate New Cells"):
    for _ in range(3):  # Generate 3 cells
        cell = DigitalCell(generation=1)
        cell.display()
