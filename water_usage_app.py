import streamlit as st
import tiktoken

# --- Token Counter ---
def count_tokens(prompt: str, model: str = "gpt-3.5-turbo") -> int:
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(prompt)
    return len(tokens)

# --- Water Usage Estimator ---
def estimate_water_usage(prompt: str, model: str = "gpt-3.5-turbo") -> float:
    tokens = count_tokens(prompt, model)
    base_water_ml = 20
    water_per_token_ml = 0.5
    estimated_water = base_water_ml + (tokens * water_per_token_ml)
    return round(estimated_water, 2), tokens

# --- Streamlit App ---
st.set_page_config(page_title="AI Water Usage Estimator", page_icon="💧")
st.title("💧 ChatGPT Water Usage Estimator")
st.markdown("Estimate the hidden environmental cost of AI – one prompt at a time!")

# User input
prompt = st.text_area("Enter your ChatGPT prompt below:")

if prompt:
    water_ml, token_count = estimate_water_usage(prompt)
    st.subheader("🌿 Results")
    st.write(f"**Prompt Length (tokens):** {token_count}")
    st.write(f"**Estimated Water Usage:** {water_ml} mL")

    # Fun comparison
    if water_ml < 50:
        st.info("💡 That's about the same as rinsing a toothbrush.")
    elif water_ml < 100:
        st.info("💡 Equivalent to a quick face wash.")
    else:
        st.info("💡 That's more water than it takes to boil a cup of tea!")

# Footer
st.markdown("---")
st.caption("Estimates are approximate based on 2023 research into LLM environmental impact.")