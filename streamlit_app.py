#Input the relevant libraries
import streamlit as st
import altair as alt
import nltk
import nltk.corpus
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Define the Streamlit app
def app():
    
    st.title('NLP Lemmatization')     
    st.subheader('(c) 2023 Louie F. Cervantes M. Eng.')
                 
    st.write('Lemmatization is another way of reducing words to their base forms.')
                 
    st.write('The lemmatization process uses a vocabulary and morphological analysis of words. It obtains the base forms by removing the inflectional word endings such as ing or ed. This base form of any word is known as the lemma.')
    
    st.subheader('List of word to lemmatize')
    st.write('A list of words is already provided in the input box. Ypu can use this list or replace the list with your own.')
    
    # Create a multiline text field
    user_input = st.text_area('Paste the block of text here', 'writing calves be branded horse randomize possibly provision hospital kept scratchy code', height=20)
    from nltk.stem import wordnet
    from nltk.stem import WordNetLemmatizer

    with st.echo(code_location='below'):
        if st.button('Submit'):    
            # Create lemmatizer object
            lemmatizer = WordNetLemmatizer()
            # Create a list of lemmatizer names for display
            lemmatizer_names = ['NOUN LEMMATIZER', 'VERB LEMMATIZER']
            formatted_text = '{:>24}' * (len(lemmatizer_names) + 1)
            res = '\n' + formatted_text.format('INPUT WORD', *lemmatizer_names) + '\n' + '='*75
            st.text(res)
            
            
   
# run the app
if __name__ == "__main__":
    app()
