import streamlit as st
from openai import OpenAI


# 💡 Prompt Agent – Clean Version (No Java, No Errors)

# 🎯 Prompt Templates Dictionary
prompt_templates = {
    "Text-to-Image (Midjourney, Leonardo)": "Describe this idea in a highly visual, photorealistic way: {prompt}. Add cinematic lighting, realistic textures, and dramatic atmosphere.",
    "Text-to-Text (ChatGPT, Gemini)": "Expand this idea into a well-structured, natural-sounding paragraph: {prompt}. Add clarity, vividness, and a relatable tone.",
    "Marketing Copy": "Write a compelling marketing message about: {prompt}. Focus on benefits, emotional appeal, and add a strong call-to-action.",
    "Storytelling": "Transform this into a short, engaging story: {prompt}. Include vivid scenes, character emotions, and a clear arc.",
    "Product Description": "Create a persuasive product description for: {prompt}. Highlight features, benefits, and customer emotions."
}

# ⚙️ Page Config
st.set_page_config(page_title="Prompt Agent", layout="centered")


# 🧠 Header
st.title("🤖 Prompt Agent ⚡ Enhance Your AI Prompts")
st.markdown("Turn your basic idea into a powerful, structured prompt for ChatGPT, Midjourney, Gemini, and more!")

# 📝 User Input
user_prompt = st.text_area("📄 Enter your basic prompt or idea:", placeholder="E.g. a woman walking on the beach")

# 📌 Prompt Type Selection
prompt_type = st.selectbox("⚙️ Select Prompt Type:", list(prompt_templates.keys()))

# 🚀 Enhance Prompt Logic
# 🚀 GPT-Based Enhance Prompt Function (Step 1C)

from openai import OpenAI

import streamlit as st
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def enhance_prompt(prompt, p_type):
    system_prompt = (
    "You are an expert AI prompt engineer and marketing strategist trained on HubSpot's AI playbook. "
    "Your job is to rewrite prompts into high-converting, structured, emotionally persuasive messages. "
    "Use a clear, human tone — avoid robotic phrasing. Focus on outcomes, benefits, action verbs, and goal-driven clarity. "
    "Incorporate natural storytelling, call-to-action language, and use NLP writing style with subtle urgency or inspiration. "
    f"Use the following style framework: {p_type}."
)

    user_message = f"Prompt: {prompt}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.85
    )

    return response.choices[0].message.content.strip()

    
    enhanced = response['choices'][0]['message']['content'].strip()
    return enhanced


# 🎯 Enhance Button
if st.button("📥 Enhance Prompt"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter a basic prompt above.")
    else:
        enhanced = enhance_prompt(user_prompt, prompt_type)
        st.markdown('### 🔥 Optimized Prompt Output:')
        st.text_area("📋 Enhanced Prompt (Copy Below)", enhanced, height=150)
        st.markdown(f"""
                <button onclick="navigator.clipboard.writeText('{enhanced}')" style="margin-top: 10px; padding: 8px 14px; background-color:#4CAF50; color:white; border:none; border-radius:10px; cursor: pointer;">

        """, unsafe_allow_html=True)
        st.success("✅ Prompt enhanced successfully!")
else:
    st.info("⬆️ Enter your prompt and select a type above, then click **Enhance Prompt** to generate your optimized prompt.")
