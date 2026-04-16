import streamlit as st
from google import genai
from dotenv import load_dotenv
from PIL import Image
from api_calling import for_issue,for_code_solution,solution_for_hints


st.title(':red[**AI Code Debugger App**]', anchor=False)
st.markdown('Upload the image of your code error.')
st.divider()

with st.sidebar:
    files = st.file_uploader('Upload your file or photo', type=('jpg', 'jpeg', 'png'), accept_multiple_files=True)

    # Show image and normal image convert into pill image

    pill_image = []

    for img in files:
        pill_img = Image.open(img)
        pill_image.append(pill_img)

    if files:
        if len(files) > 3:
            st.error('Upload max 3 photos at a time')
        else:
            st.subheader('Uploaded images')

            # image convert into column
            col = st.columns(len(files))

            for i, img in enumerate(files):
                with col[i]:
                    st.image(img)


    select_box = st.selectbox('How to want to solve the problem.', ('Hints', 'Solution with code'), index=None)

    pressed = st.button('Click the button to initiate AI', type='primary')

    # Condition check for select_box and button

if pressed:
    if not files:
        st.error('Please upload at least one photo')
    if not select_box:
        st.error('You must select a one option.')
        
    if files and select_box:
            
        # AI Response section
        # for hints
        if select_box == 'Hints' or 'Solution with code':
            with st.container(border=True):
                st.subheader('The issue:', anchor=False)

                # Spinner and api calling

                with st.spinner('AI is cooking for you...'):
                    hints = for_issue(pill_image)
                    st.markdown(hints)

        # solution for hints
        if select_box == 'Hints':
            with st.container(border=True):
                st.subheader('The solution', anchor=False)

                # spinner and calling api
                with st.spinner('AI is cooking for you...'):
                    solution = solution_for_hints(pill_image)
                    st.markdown(solution)

        # solution for code solution
        elif select_box == 'Solution with code':
            with st.container(border=True):
                st.subheader('The solution', anchor=False)

                # spinner and calling api
                with st.spinner('AI is cooking for you...'):
                    solution = for_code_solution(pill_image)
                    st.markdown(solution)





            