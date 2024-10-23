import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers



## Function to get response from Llama 2 model

def llama_response(input_text, no_of_words, blog_type):

    ### llama 2 model
    llm=CTransformers(model='model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
  

    ## Prompt Template
    template="""
        write a blog for {blog_type} job profile for a paticluar topic {input_text}
        within {no_of_words} words.
             """


    prompt=PromptTemplate(input_variables=["blog_type", "input_text", "no_of_words"],
                          template=template)


    ## Generate the response from the llama model
    response=llm(prompt.format(blog_type=blog_type, input_text=input_text, no_of_words=no_of_words))
    print(response)
    return response



st.set_page_config(page_title="Generate Blogs",
                   page_icon= '🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the blog topic")


## creating 2 more columns for additional 2 fields

col1,col2=st.columns([5,5])


with col1:
    no_of_words = st.text_input('No of words')
with col2:
    blog_type=st.selectbox('Who is the blog written for', 
                            ('Researchers', 'Data Scientist', 'Common People', 'Data Engineers', 'Machine Learning Engineers'), index=0)


submit=st.button("Generate")


## Final response
if submit:
    st.write(llama_response(input_text, no_of_words, blog_type))