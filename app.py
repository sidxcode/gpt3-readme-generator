import streamlit as st
import openai

openai.api_key = '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'


@st.cache(allow_output_mutation=True)
def ask(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']


file_data = ""

st.set_page_config(page_title="GPT3 ReadMe Generator 🤖",
                   page_icon=":robot:")

st.title("GPT3 ReadMe Generator 🤖")
st.markdown("----")

instructions = st.empty()
with instructions.container():
    st.subheader("Instructions")
    st.markdown("- Use the file uploader to select the code files that you want to generate a readme for. You can upload multiple files at once.")
    st.markdown(
        "- Once you have uploaded the files, click on the Preview button.")
    st.markdown(
        "- The app will generate a readme in Markdown format using OpenAI's API, and display it on the page.")
    st.markdown(
        "- You can download the generated readme by clicking the Download Markdown button.")
    st.markdown("----")

st.subheader("Upload the code files 📩")
uploaded_files = st.file_uploader(
    'None',  accept_multiple_files=True, key="file_upload", label_visibility="hidden")

if uploaded_files is not None:
    for i in range(0, len(uploaded_files)):
        file_data += "\nFile Name: " + \
            uploaded_files[i].name + "\nCode:\n" + \
            uploaded_files[i].read().decode()

st.empty()

if st.button("Preview"):
    response_markdown = ask(
        f"{file_data}\n\nRead the code and generate a readme file in .md format (introduction, motivation, code style, tech/framework/library used, installation, usage, contribution, limitation, license and all other relevant information)")
    instructions.empty()
    st.subheader("💻 ReadMe Preview:")
    st.markdown("----")
    st.markdown(response_markdown)
    st.markdown("----")
    st.download_button("Download Markdown",
                       response_markdown, file_name="name.md")
    st.markdown("----")
