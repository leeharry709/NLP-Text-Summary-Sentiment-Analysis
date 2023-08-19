from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import yake
from textblob import TextBlob
import streamlit as st

model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-xsum')
tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-xsum')

# Summarize text with BART
def summarize_text(text, model_name=model):
    tokens = tokenizer(text, truncation=True, padding='longest', return_tensors='pt')
    summary = model.generate(**tokens)

    summary_ids = tokenizer.decode(summary[0])

    keyword_extractor = yake.KeywordExtractor()
    keywords = keyword_extractor.extract_keywords(text)

    sorted_keywords = sorted(keywords, key=lambda x: x[1], reverse=True)
    top_ten_keywords = sorted_keywords[:10]

    sentiment = TextBlob(text).sentiment

    return summary_ids, top_ten_keywords, sentiment

st.set_page_config(page_title='Text Summarization')
st.title('PEGASUS - Text Summarization')

if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role': 'assistant', 'content': 'What can I summarize for you?'}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

if prompt := st.chat_input(placeholder='Enter text for summarization'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    st.chat_message('user').write(prompt)

    with st.chat_message('assistant'):
        summary_ids, top_ten_keywords, sentiment = summarize_text(prompt)
        st.session_state.messages.append({'role': 'assistant', 'content': summary_ids.replace('<pad>', '').replace('</s>', '')})
        st.write(summary_ids.replace('<pad>', '"').replace('</s>', '"'))
        st.write('\n')
        st.write('**Top 10 Keywords:**\n')
        for keyword, score in top_ten_keywords:
            st.write(keyword+': ', round(score, 4))
        st.write('\n')
        st.write('**Sentiment:**')
        st.write('Polarity: ', round(sentiment.polarity, 4))
        st.write('Subjectivity: ', round(sentiment.subjectivity, 4))