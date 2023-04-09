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
    st.write('A list of words is already provided in the input box. You can use this list or replace the list with your own lost of words.')
    
    # Create a multiline text field
    user_input = st.text_area('Input the list of words here', 'writing \ncalves \nbe \nbranded \nhorse \nrandomize \npossibly \nprovision \nhospital \nkept \nscratchy \ncode', height=50)
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
            input_words = user_input.split()
            
            # Lemmatize each word and display the output
            for word in input_words:
                output = [word, lemmatizer.lemmatize(word, pos='n'),
                lemmatizer.lemmatize(word, pos='v')]
                res = formatted_text.format(*output)
                st.text(res)
            st.write('We can see that the noun lemmatizer works differently than the verb lemmatizer when it comes to words like writing or calves. If you compare these outputs to stemmer outputs, you will see that there are differences too. The lemmatizer outputs are all meaningful whereas stemmer outputs may or may not be meaningful.')
            
            
   
# run the app
if __name__ == "__main__":
    app()
