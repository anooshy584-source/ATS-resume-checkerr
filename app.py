
import os
import streamlit as st
from groq import Groq
from roadmap import generate_roadmap


st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🎯",
    layout="centered",
)

st.title("🎯 AI Learning Roadmap Generator")
st.write(
    "Create a personalized learning plan based on your goals, "
    "skill level, and available study time."
)

st.divider()


def get_setting(name, default=""):
    """Read a setting from Streamlit Secrets or environment variables."""
    try:
        value = st.secrets.get(name, "")
        if value:
            return str(value).strip()
    except Exception:
        pass

    return os.environ.get(name, default).strip()


api_key = get_setting("GROQ_API_KEY")
model = get_setting(
    "GROQ_MODEL",
    "openai/gpt-oss-120b",
)
)

with st.expander("Check Groq API connection"):
    if not api_key:
        st.warning(
            "API key not found. Add GROQ_API_KEY in your "
            "Streamlit Secrets settings."
        )
    else:
        if st.button("Test API Key"):
            try:
                client = Groq(api_key=api_key)
                client.models.list()
                st.success("API key accepted by Groq.")
            except Exception as e:
                error_type = type(e).__name__

                if error_type == "AuthenticationError":
                    st.error(
                        "Groq rejected the API key. Create a new key "
                        "in Groq Console and replace the saved secret."
                    )
                elif error_type == "RateLimitError":
                    st.error(
                        "Groq rate limit or quota reached. "
                        "Check your Groq Console."
                    )
                else:
                    st.error(f"Connection test failed: {error_type}")
                    st.caption(str(e))


st.subheader("Your Learning Plan")

field = st.text_input(
    "What do you want to learn?",
    placeholder="e.g. Cybersecurity, Python, Web Development",
)

level = st.selectbox(
    "Choose your current skill level",
    ["Beginner", "Intermediate", "Advanced"],
)

weeks = st.number_input(
    "How many weeks do you have?",
    min_value=1,
    max_value=104,
    value=8,
    step=1,
)

hours = st.number_input(
    "How many hours can you study per week?",
    min_value=1,
    max_value=80,
    value=5,
    step=1,
)

if st.button("Generate My Roadmap", type="primary"):
    if not field.strip():
        st.warning("Please enter a learning field.")

    elif not api_key:
        st.error(
            "API key not found. Add GROQ_API_KEY in Streamlit Secrets "
            "and restart the app."
        )

    else:
        try:
            with st.spinner("Preparing your personalized roadmap..."):
                roadmap = generate_roadmap(
                    field=field.strip(),
                    level=level,
                    weeks=int(weeks),
                    hours=int(hours),
                    api_key=api_key,
                    model=model,
                )

            st.success("Your roadmap is ready!")
            st.markdown(roadmap)

            st.download_button(
                label="Download Your Roadmap",
                data=roadmap,
                file_name="learning_roadmap.md",
                mime="text/markdown",
            )

        except Exception as e:
            error_type = type(e).__name__

            if error_type == "AuthenticationError":
                st.error(
                    "Groq rejected the API key. Check your Groq key "
                    "in Streamlit Secrets."
                )

            elif error_type == "RateLimitError":
                st.error(
                    "Groq API rate limit or quota reached. "
                    "Check your Groq Console."
                )

            elif error_type == "APIConnectionError":
                st.error(
                    "Could not connect to Groq. Check your internet "
                    "connection and try again."
                )

            elif error_type == "BadRequestError":
                st.error(
                    "Groq rejected the request. The selected model "
                    "may be unavailable or the request may need changes."
                )
                st.caption(str(e))

            elif error_type == "APIStatusError":
                status_code = getattr(e, "status_code", "unknown")
                st.error(f"Groq returned an API error: {status_code}")
                st.caption(str(e))

            else:
                st.error("Something went wrong while generating the roadmap.")
                st.caption(f"Error type: {error_type}")
                st.caption(str(e))
