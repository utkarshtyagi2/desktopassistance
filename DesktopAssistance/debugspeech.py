import pyttsx3
import speech_recognition as sr


def taskCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        # r.energy_threshold = 300
        r.adjust_for_ambient_noise(source,duration=1)
        print("listening....")
        audio= r.listen(source)
        print("listening completed")
    try:
        # print("i think you said"+ r.recognize_google(audio, language="en-in"))
        print("recgnizing....")
        query = r.recognize_google(audio, language='en-in')
        print("user said : query= ",query)
    except Exception as ex:
        print(ex)
        print("say that again please...")
        return "None"
    # except sr.UnknownValueError as identifier:
    #     print("i could not understand auidio")
    # except sr.RequestError as e:
    #     print("jarvis error: {0}".format(e))
    # except sr.WaitTimeoutError:
    #     print("sorry timeout")
    return query


if __name__ == "__main__":
    taskCommand()
