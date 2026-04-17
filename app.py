import streamlit as st
from PIL import Image
from api_calling import for_hints,for_solution



st.title("Code Debugger")
st.markdown("Give screenshots of your code,AI will debug and fix your code")
st.divider()

more_than_three_image=False
no_image=False
no_option=False

with st.sidebar:
    st.header("Control")
    images=st.file_uploader("Drop your screenshots",
        type=["jpg","jpeg","png"],
        accept_multiple_files=True)
    
    if(not images):
        no_image=True
    elif(len(images)>3):
        more_than_three_image=True
    else:
        cols=st.columns(len(images))
        for i,per_image in enumerate(images):
            with cols[i]:
                st.image(per_image,use_container_width=True)

    option=st.selectbox("What do you want",
    ["Hints","Solution with code"],
    index=None)
    if(option==None):
        no_option=True
    button=st.button("Press",type="primary")


if button:
    if no_image:
        st.error("You have to upload at least one image")
    if more_than_three_image:
        st.error("You cannot upload more than three images")
    if no_option:
        st.error("You have to select atleast one option")


    if no_image==False and more_than_three_image==False and no_option==False:

        pil_images=[]
        for img in images:
            pil_img=Image.open(img)
            pil_images.append(pil_img)


        with st.container(border=True):
            with st.spinner("AI is working for you"):
                if option=="Hints":
                    ai_hint=for_hints(pil_images)
                    st.markdown(ai_hint)
                else:
                    ai_solution=for_solution(pil_images)
                    st.markdown(ai_solution)



    

