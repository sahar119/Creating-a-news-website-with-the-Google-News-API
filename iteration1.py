import requests
import streamlit as st
import streamlit.components.v1 as stc
from pretty_notification_box import notification_box
import time

# News API configuration
API_KEY = '***************************************'
API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
COUNTRY_CODE = 'us'

def get_news():
    params = {
        'country': COUNTRY_CODE,
        'apiKey': API_KEY
    }
    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()
    return data['articles']

    
    
st.title('Latest News')

st.sidebar.markdown("""<div style="background-color:#FF5733;color:#FFFFFF;padding:10px;border-radius:5px;"><strong>⚠️Doomscrolling Warning:</strong>  Are you doomscrolling? What about taking a short screen break and looking away from your computer? There might be many more news updates, but you still deserve time to rest.!</div>""", unsafe_allow_html=True)


    

def mir():

    articles = get_news()
    for article in articles:
        st.write('## ' + article['title'])
        st.write(article['description'])
        st.write(article['source']['name'])
        st.write(article['url'])
        st.image(article['urlToImage']) 
        st.markdown('---')
        
                                                                                                                                                                                                  
mir()


styles = {'material-icons':{'color': 'red'},
          'title': {'font-weight':'bold'},
          'notification-content-container': {'':''},
          'title-text-url-container': {'',''},
          'notification-text-link-close-container': {'',''},
          'external-link': {'',''},
          'close-button': {'',''}}


def doom():
     time.sleep(30)                                                                                                
     notification_box(icon='warning', title='Warning', textDisplay='This is a Doomscrolling Warning', externalLink='view more details', url='https://www.sciencealert.com/here-s-what-doomscrolling-is-doing-to-your-brain-and-how-to-fix-the-problem', styles=None, key='foo')
        
doom() 



                