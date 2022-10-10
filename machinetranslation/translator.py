import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = ['apikey']
url = ['url']

authenticator = IAMAuthenticator('j9Zmi1MnbnweGGe_c5Js0QCXMw0RojdTmrt3MVz5CjoJ')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/d451c919-e6bf-4aa9-8d44-fc50aadb0eaf')

def englishToFrench(englishText):
    translation = language_translator.translate(
        text=englishText, model_id='en-fr').get_result() 
    frenchText=translation['translations'][0]['translation'] 
    return frenchText

def frenchToEnglish(frenchText):
    translation = language_translator.translate(
        text=frenchText, model_id='fr-en').get_result() 
    englishText=translation['translations'][0]['translation'] 
    return englishText

if __name__ == '__main__':
    print(frenchToEnglish('bonjour comment vas-tu?'))
    print(englishToFrench('hello how are you?'))