import flet as ft
import random

def main(page:ft.Page):
    page.title = "Typing Master"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    words = [
    "hippopotomonstrosesquipedaliophobia",
    "floccinaucinihilipilification",
    "antidisestablishmentarianism",
    "pseudopseudohypoparathyroidism",
    "supercalifragilisticexpialidocious",
    "incomprehensibilities",
    "electroencephalographically",
    "psychoneuroendocrinological",
    "thyroparathyroidectomized",
    "counterrevolutionaries",
    "uncharacteristically",
    "indistinguishability",
    "disproportionableness",
    "mischaracterization",
    "institutionalization",
    "photosynthetically",
    "microarchitectures",
    "intercontinentalism",
    "compartmentalization",
    "hypercholesterolemia"
]
    
    random.shuffle(words)
    total_words = 15
    index = 0
    mistakes = 0
    correct = 0

    word_label = ft.Text(words[index], size=24)
    status_label = ft.Text("")
    progress_label = ft.Text(f"0 / {total_words}")
    accuracy_label = ft.Text("Accuracy: 0%")

    input_field = ft.TextField(label="Type the word")

    def check_word(e):
        nonlocal index, mistakes, correct
        
        user_word = input_field.value

        if user_word == words[index]:
            status_label.value = "Correct!"
            status_label.color = ft.colors.GREEN
            correct += 1
        else:
            status_label.value = "Incorrect!"
            status_label.color = ft.colors.RED
            mistakes += 1

        index += 1