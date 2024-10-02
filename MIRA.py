import pyttsx3, datetime, wikipedia
import speech_recognition as sr
import webbrowser, os, random
import mail as em

speech_engine = pyttsx3.init("sapi5")
voices = speech_engine.getProperty("voices")
speech_engine.setProperty("voice", voices[3].id)


def speak(audio):
    """This function converts text to speech"""
    speech_engine.say(audio)
    speech_engine.runAndWait()


def greetMe():
    """This function greets user"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        print("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

    speak("I am MIRA")
    print("I am MIRA")


def takeCommmand():
    """This function takes voice command from user"""
    """This command takes audio input from user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # this is 'with' block in pyhton
        # source is instance of Microphone class here we are opening, closing and creating object for Microphone class in one command
        print("Listening...")
        r.pause_threshold = 1
        # seconds of non-speaking audio before a phrase is considered complete
        # from the default 0.8 seconds to 1 second to better accommodate pauses by user in between sentences.
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        # here we are calling google's speech to text 'en-in' is used to recognize indian english accent
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Please Speak Again")
        return "None"
    return query


if __name__ == "__main__":

    greetMe()
    # Speak("My name is MIRA, I am Desktop asistant created by Ayush Gupta.")
    # MIRA Modular Intelligence for Routine Automation
    while True:
        query = takeCommmand().lower()
        # logic for executing tasks based on query
        if "quit" in query:
            exit()

        if "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query and "firefox" in query:
            firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
            # Register the browser
            webbrowser.register(
                "firefox", None, webbrowser.BackgroundBrowser(firefox_path)
            )
            # Open Google using the registered browser
            firefox = webbrowser.get("firefox")
            firefox.open("www.youtube.com")

        elif "youtube" in query and "chrome" in query:
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            # Register the browser
            webbrowser.register(
                "chrome", None, webbrowser.BackgroundBrowser(chrome_path)
            )
            # Open Google using the registered browser
            chrome = webbrowser.get("chrome")
            chrome.open("www.youtube.com")

        elif "youtube" in query and "edge" in query:
            edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            # Register the browser
            webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))
            # Open Google using the registered browser
            edge = webbrowser.get("edge")
            edge.open("www.youtube.com")

        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif "google" in query and "firefox" in query:
            firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
            # Register the browser
            webbrowser.register(
                "firefox", None, webbrowser.BackgroundBrowser(firefox_path)
            )
            # Open Google using the registered browser
            firefox = webbrowser.get("firefox")
            firefox.open("www.google.com")

        elif "google" in query and "chrome" in query:
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            # Register the browser
            webbrowser.register(
                "chrome", None, webbrowser.BackgroundBrowser(chrome_path)
            )
            # Open Google using the registered browser
            chrome = webbrowser.get("chrome")
            chrome.open("www.google.com")

        elif "google" in query and "edge" in query:
            edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            # Register the browser
            webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))
            # Open Google using the registered browser
            edge = webbrowser.get("edge")
            edge.open("www.google.com")

        elif "open google" in query:
            speak("Opening google")
            webbrowser.open("www.google.com")

        elif "play music" in query:
            music_dir = r"C:\Users\ayush\Music\My Music\English"
            songs = os.listdir(music_dir)
            print(songs)
            num = random.randint(0, (len(songs) - 1))
            os.startfile(os.path.join(music_dir, songs[num]))

        elif "play" in query:
            music_dir = r"C:\Users\ayush\Music\My Music\English"
            songs = os.listdir(music_dir)
            for i in songs:
                k = i.strip(".mp3")
                name_lis = k.split(" ")
                for j in name_lis:
                    if j.lower() in query:
                        os.startfile(os.path.join(music_dir, i))
                        print(i)
                        break

        if "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak("The time is:")
            speak(strTime)
            strDate = datetime.date.today()
            print(strDate)
            speak("and date is:")
            speak(strDate)

        if "date" in query:
            strDate = datetime.date.today()
            print(strDate)
            speak("today's date is:")
            speak(strDate)
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak("and time is:")
            speak(strTime)

        elif "open code" in query:
            file_path = (r"C:\Users\ayush\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            os.startfile(file_path)

        if "close code" in query:
            try:
                os.system("taskkill /f /im code.exe")
            except Exception as e:
                print("VS Code is not open")

        elif "send email" in query:
            try:
                speak("What shall be the  subject?")
                subject = takeCommmand()
                speak("What shall be content?")
                body = takeCommmand()
                recipients = ["godfatherg324@gmail.com"]
                em.sendEmail(body, recipients, subject)
                speak("Email has been sent")
            except Exception as e:
                print(e)


# add application closing functionality
# add multiple email sending functionality
# format code to enter more functions and classes 
