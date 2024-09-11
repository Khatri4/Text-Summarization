import streamlit as st
import validators
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model='mixtral-8x7b-32768')

st.set_page_config(page_title="Summarizer app for youtube & website")
st.title("Summarizer App")
st.subheader("Summarizer URL")

generic_url = st.text_input("URL", label_visibility="collapsed")

# prompt template
prompt_template = """
Summarize the content of the following material. Highlight the main topics, key points, and important conclusions. Ensure the summary is concise and within 400 words, providing a clear and accurate overview.
Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=['text'])


if st.button("Summarize the content from the YT or Website"):
    # validate all the input
    if not generic_url.strip():
        st.error("Please enter a URL")
    elif not validators.url(generic_url):
        st.error("Please enter valid url. It can may be a YT video or website url")
    else:
        try:
            with st.spinner("Summarizing your content"):
                # loading the website or yt video url
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url,add_video_info=True)
                else:
                    loader = UnstructuredURLLoader(urls=[generic_url], ssl_verify=False,
                                                headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                data = loader.load()

                # chain for summarization
                chain = load_summarize_chain(llm, chain_type='stuff', prompt=prompt)
                output_summary=chain.run(data)

                st.success(output_summary)
        except Exception as e:
            st.exception(f"Exception:{e}")
