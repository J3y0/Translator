from bs4 import BeautifulSoup
import requests
import deepl
import re
import os


def deepl_translation(user_input, LANG_IN, LANG_OUT):
    path = os.path.dirname(os.path.abspath(__file__))
    auth_key = open(path + "/auth.txt","r").read().rstrip()
    translator = deepl.Translator(auth_key)
    # print("Auth checked !")
    translation = translator.translate_text(    user_input,
                                                source_lang=LANG_IN,
                                                target_lang=LANG_OUT) # Formality option is available
    return translation



if __name__ == "__main__":
    deepl_lang_in = {
        "FR":"French",
        "ES":"Spanish",
        "EN":"English",
        "IT":"Italian",
        "DE":"German"}

    deepl_lang_out = {
        "FR":"French",
        "ES":"Spanish",
        "EN-GB":"British english",
        "EN-US":"American english",
        "IT":"Italian",
        "DE":"German"}

    print("Welcome to this translator program !")

    print("Reminder !")
    for keys,values in deepl_lang_in.items():
        print(f" - {keys}:{values}")
    LANG_IN = input("In which language are you writing ?")

    print("Reminder !")
    for keys,values in deepl_lang_out.items():
        print(f" - {keys}:{values}")
    LANG_OUT = input("And you want to translate it in ?")

    sentence = input("Enter your sentence: ")
    print(deepl_translation(sentence, LANG_IN, LANG_OUT))


    print("Press any key to leave...")
    os.system('read -n1')
