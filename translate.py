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



def wr_print_content(wrd_class):
    for each in wrd_class:

        french = each.find(class_="FrWrd")
        
        if french != None:
            print("+----------------------------+")
            print("|          FRANCAIS          |")
            print("+----------------------------+")
            print(french.find("strong").text)
            meaning = french.next_sibling

            if meaning != None:
                print("+----------------------------+")
                print("|           MEANING          |")
                print("+----------------------------+")
                print(meaning.text)

        english = each.find(class_="ToWrd")

        if english != None:
            print("+----------------------------+")
            print("|           ENGLISH          |")
            print("+----------------------------+")
            english.em.decompose() # Remove the noun/verb part
            print(english.text)

        from_example = each.find(class_="FrEx")

        if from_example != None:
            print("+----------------------------+")
            print("|           EXAMPLE          |")
            print("+----------------------------+")
            print(from_example.text)

        to_example = each.find(class_="ToEx")

        if to_example != None:
            print(to_example.text)


if __name__ == "__main__":
    print("Welcome to this translator program !")
    print("Do you want to translate a word (1) or a sentence (2)?")
    choice = int(input())
    while 0 >= choice or choice >= 3:
        print("Error ! Try again...")
        choice = int(input())

    if choice == 1:
        word = input("Enter your word: ")

        ######## BUILDING THE PAYLOAD ###########
        wr_url = "https://www.wordreference.com/"
        lang_combination = "fren"
        wr_payload = wr_url + lang_combination + "/" + word


        ######## SENDING THE PAYLOAD ############
        session = requests.Session()
        response = session.get(wr_payload)
        print(f"Sending the request to {wr_payload} ...")

        data = response.text
        # print(data)
        soup = BeautifulSoup(data, "html5lib")
        util = soup.find(id="centercolumn")

        ####### RECEIVING THE RESPONSE ##########

        # Pronunciation ? Marche pour le fr (mais on s'en branle donc faire une condition pour savoir si c'est en anglais)
        pronon = util.find("span", title="Prononciation")
        print(pronon.contents[0])

        translation_even = util.find("table", class_="WRD").find_all(class_="even")
        translation_odd = util.find("table", class_="WRD").find_all(class_="odd")
        wr_print_content(translation_even)
        wr_print_content(translation_odd)


    elif choice == 2:
        sentence = input("Enter your sentence: ")
        LANG_IN = "FR"
        LANG_OUT = "EN-GB"
        print(deepl_translation(sentence, LANG_IN, LANG_OUT))


    print("Press any key to leave...")
    os.system('read -n1')
