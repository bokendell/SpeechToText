import streamlit as st
from transcribe import *
from chatGPT import *
import time

st.header("Trascribe Audio")

fileObject = st.file_uploader(label = "Please upload your file" )
if fileObject:
    token, t_id = upload_file(fileObject)
    result = {}
    #polling
    sleep_duration = 1
    percent_complete = 0
    progress_bar = st.progress(percent_complete)
    st.text("Currently in queue")
    while result.get("status") != "processing":
        percent_complete += sleep_duration
        time.sleep(sleep_duration)
        progress_bar.progress(percent_complete/10)
        result = get_text(token,t_id)

    sleep_duration = 0.01

    for percent in range(percent_complete,101):
        time.sleep(sleep_duration)
        progress_bar.progress(percent)

    with st.spinner("Processing....."):
        while result.get("status") != 'completed':
            result = get_text(token,t_id)

    prompt = "Summarize and list the key points from the following text that was transcribed during a college class lecture: "
    prompt += result['text']

    chatGPTResponse = get_completion(prompt)

    st.balloons()
    st.header("Summarized Text")
    st.subheader(chatGPTResponse)