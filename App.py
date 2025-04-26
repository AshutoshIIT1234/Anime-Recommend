import pickle
import streamlit as st
import requests
import pandas as pd
import base64
import os
from PIL import Image
Anime_dict=pickle.load(open('Model\Anime_list.pkl', 'rb'))
Anime=pd.DataFrame(Anime_dict)
file_ = open("PikachuSigh.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

col,  = st.columns(1)
with col:

    st.title('konichi wa!') 
  
   



def image_slider_auto(image_paths, interval_ms=3000):
    image_base64s = []
    for path in image_paths:
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            image_base64s.append(f"data:image/png;base64,{encoded_string}")

    image_html = "".join(f'<img src="{img}" style="width: 100%; height: 50%;">' for img in image_base64s)

    slider_html = f"""
    <div id="imageSlider" style="overflow-x: hidden; width: 100%;">
        <div style="display: flex; transition: transform 0.5s ease-in-out;">
            {image_html}
        </div>
    </div>
    <style>
    #imageSlider {{
        position: relative;
    }}
    #imageSlider > div {{
        width: {'{}%'.format(len(image_base64s) *10)}; /* Ensure enough width for all images */
    }}
    #imageSlider > div > img {{
        width: 50%;
        height: auto; /* Maintain aspect ratio */
        display: inline-block;
        margin-right: 10px; /* Adjust spacing between images */
    }}
    </style>
    <script>
    var slider = document.getElementById('imageSlider');
    var sliderInner = slider.querySelector('div');
    var images = sliderInner.querySelectorAll('img');
    var index = 0;
    var interval = {interval_ms};
    var numImages = images.length;

    function nextImage() {{
        index = (index + 1) % numImages;
        sliderInner.style.transform = 'translateX(-' + index * (50) + '%)';
    }}

    setInterval(nextImage, interval);
    </script>
    """
    # Adjust height as needed
    st.components.v1.html(slider_html, width=600, height=400, scrolling=False)
if __name__ == '__main__':
    image_folder = "images_auto_50_percent"
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
        dummy_image1 = Image.new('RGB', (200, 100), color = 'red')
        dummy_image1.save(os.path.join(image_folder, "image1.png"))
        dummy_image2 = Image.new('RGB', (300, 150), color = 'green')
        dummy_image2.save(os.path.join(image_folder, "image2.png"))
        dummy_image3 = Image.new('RGB', (100, 200), color = 'blue')
        dummy_image3.save(os.path.join(image_folder, "image3.png"))
        dummy_image4 = Image.new('RGB', (400, 200), color = 'yellow')
        dummy_image4.save(os.path.join(image_folder, "image4.png"))

    image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if image_files:
        st.title("Welcome to the Anime Recommender System")
        image_slider_auto(image_files)
    else:
        st.warning("No images found in the 'images_auto_50_percent' folder. Please add some.")

selected_Anime_name=st.selectbox(
    'Select a Anime',
    Anime['Name'].values
)
similarity=pickle.load(open('Model\similarity.pkl', 'rb'))
def recommend_Anime(selected_Anime_name):
    index=Anime[Anime['Name']==selected_Anime_name].index[0]
    distances=similarity[index]
    Anime_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_Anime=[]
    for i in Anime_list:
        recommended_Anime.append(Anime.iloc[i[0]].Name)
    return recommended_Anime



if st.button('Show Recommendation'):
    # import the recommendation function

  
    st.write('Recommended Anime for you:')
    recommend_Anime=recommend_Anime(selected_Anime_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_Anime[0])
    with col2:
        st.text(recommend_Anime[1])
   

    with col3:
        st.text(recommend_Anime[2])
        
    with col4:
        st.text(recommend_Anime[3])
       
    with col5:
        st.text(recommend_Anime[4])
    
    

    
