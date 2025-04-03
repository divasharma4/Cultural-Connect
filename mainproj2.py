import tkinter as tk

class Character:
    def __init__(self, name, location, background, fears):
        self.name = name
        self.location = location
        self.background = background
        self.fears = fears
        self.inventory = []
        self.story_progress = []

    def move(self, new_location):
        self.location = new_location

    def make_choice(self, choice):
        self.story_progress.append(choice)

    def add_to_inventory(self, item):
        self.inventory.append(item)


class ShadowOfTheHuntsman:
    def __init__(self, root):
        self.root = root
        self.character1 = Character("Hunter", "Forest Path", "A seasoned hunter, betrayed by a friend and haunted by the ghosts of his past.", "Fear of betrayal and losing his humanity.")
        self.character2 = Character("Mystic", "Village Edge", "A young sorceress, seeking to prove herself, haunted by visions of dark omens.", "Fear of failing those she loves.")
        self.active_character = None

    def clear_window(self):
        """Clears any previous widgets."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_game(self):
        """Start with intro and character selection."""
        self.clear_window()
        self.display_scene(
            "Welcome to 'The Shadow of the Huntsman'. In this dark tale, you will choose between two heroes: The Hunter, seeking redemption from the curse of the Huntsman, or the Mystic, a young sorceress entangled in a web of magic. Your choices will determine their fate. Prepare yourself for a journey of shadows, magic, and mystery.",
            [
                ("Start the Adventure", self.show_character_selection)
            ],
        )

    def show_character_selection(self):
        """Character selection screen."""
        self.clear_window()
        self.display_scene(
            "The forest calls. The Huntsman's shadow lingers over the land. Choose your character to begin the journey:",
            [
                ("Play as the Hunter", lambda: self.select_character(self.character1)),
                ("Play as the Mystic", lambda: self.select_character(self.character2)),
            ],
        )

    def select_character(self, character):
        """Set the active character and start their journey."""
        self.active_character = character
        if character == self.character1:
            self.start_hunter_journey()
        elif character == self.character2:
            self.start_mystic_journey()

    def display_scene(self, text, choices):
        """Display the story text and choices."""
        self.clear_window()

        scene_label = tk.Label(self.root, text=text, font=("Arial", 12), wraplength=1000, justify="center")
        scene_label.pack(pady=30)

        for label, command in choices:
            button = tk.Button(self.root, text=label, command=command, width=50, height=4, font=("Arial", 12))
            button.pack(pady=20)

    # Hunter's Story
    def start_hunter_journey(self):
        self.display_scene(
            "As the Hunter, you walk along the familiar forest path, the smell of pine and damp earth filling your senses. But something is wrong. The air feels colder, the shadows deeper. Rumors of the Huntsman—a shadowy figure who roams these woods—creep into your mind. What do you do?",
            [
                ("Venture deeper into the forest in order to confront the curse.", self.hunter_deeper_forest),
                ("Set up camp, hoping to wait for daylight and gather your thoughts.", self.hunter_set_camp),
            ],
        )

    def hunter_deeper_forest(self):
        self.display_scene(
            "The deeper you go, the more oppressive the atmosphere becomes. The trees groan in the wind as if speaking in forgotten tongues. You sense something watching you, something ancient. Your pulse quickens as a shadow crosses your path. What do you do?",
            [
                ("Approach the shadow", self.hunter_approach_shadow),
                ("Call out into the darkness", self.hunter_call_out),
            ],
        )

    def hunter_set_camp(self):
        self.display_scene(
            "You sit by the fire, watching the night pass. The sounds of the night grow louder, more ominous. What do you do?",
            [
                ("Investigate the noise", self.hunter_investigate_noise),
                ("Wait until dawn", self.hunter_wait_until_dawn),
            ],
        )

    def hunter_approach_shadow(self):
        self.display_scene(
            "You approach the shadow cautiously. The Huntsman’s shadow falls upon you.",
            [
                ("Fight back", self.hunter_fight_back),
                ("Plead for mercy", self.hunter_plead_for_mercy),
            ],
        )

    def hunter_call_out(self):
        self.display_scene(
            "The darkness responds with a chill. The Huntsman is near. What will you do?",
            [
                ("Fight back", self.hunter_fight_back),
                ("Plead for mercy", self.hunter_plead_for_mercy),
            ],
        )

    def hunter_investigate_noise(self):
        self.display_scene(
            "You approach the noise cautiously, but as you step deeper into the woods, you stumble into a pit. Something cold grabs your ankle.",
            [
                ("Fight back", self.hunter_fight_back),
                ("Plead for mercy", self.hunter_plead_for_mercy),
            ],
        )

    def hunter_wait_until_dawn(self):
        self.display_scene(
            "As dawn breaks, you find yourself face-to-face with the Huntsman.",
            [
                ("Attempt to reason with the Huntsman", self.hunter_reason_with_huntsman),
                ("Fight him", self.hunter_fight_huntsman),
            ],
        )

    def hunter_fight_back(self):
        self.end_story("You fight bravely, but the darkness overwhelms you.")

    def hunter_plead_for_mercy(self):
        self.end_story("Your pleas go unanswered. The Huntsman’s shadow consumes you.")

    def hunter_reason_with_huntsman(self):
        self.end_story("The Huntsman listens, but his curse cannot be broken by words.")

    def hunter_fight_huntsman(self):
        self.end_story("Your fight is endless, and the curse claims you.")

    # Mystic's Story
    def start_mystic_journey(self):
        self.display_scene(
            "As the Mystic, you stand at the edge of a village where the earth feels colder than it should. The villagers speak of a great terror—a Huntsman, a creature trapped by a curse. But as you listen to their warnings, you hear the whisper of a deeper magic, one that you cannot ignore. What do you do?",
            [
                ("Enter the forest, seeking to understand the magic behind the curse.", self.mystic_enter_forest),
                ("Stay in the village, hoping to learn more from the villagers.", self.mystic_gather_info),
            ],
        )

    def mystic_enter_forest(self):
        self.display_scene(
            "The forest envelops you in its cool embrace. The air smells of moss and decay. The further you walk, the heavier the weight of ancient magic presses on your chest. A shadow moves swiftly between the trees. You follow, knowing the forest hides secrets that can destroy or save. What do you do?",
            [
                ("Approach the shadow, hoping to learn its secrets.", self.mystic_approach_shadow),
                ("Turn away, fearing what you might find.", self.mystic_fearful_escape),
            ],
        )

    def mystic_gather_info(self):
        self.display_scene(
            "You stay in the village and gather information, but you feel the pull of the forest growing stronger. Eventually, you can no longer ignore it. You head into the forest, but the curse already has its grip on you.",
            [
                ("Go further into the forest", self.mystic_enter_forest)
            ]
        )

    def mystic_approach_shadow(self):
        self.display_scene(
            "The shadow reveals itself to be the Hunter, a stranger to you. He is determined to end the curse, but the shadow of the Huntsman looms over him. Together, you must face the dark magic that binds him. What do you do?",
            [
                ("Join forces with the Hunter, and together break the curse.", self.mystic_join_hunter),
                ("Attempt to banish the curse alone, without the Hunter’s help.", self.mystic_banish_alone),
            ],
        )

    def mystic_fearful_escape(self):
        self.end_story("Fear consumes you, and you flee the forest. But the Huntsman’s curse follows, forever tied to the land. You cannot escape the darkness.")

    def mystic_join_hunter(self):
        self.end_story("Together, you break the curse that binds the forest and free the souls trapped within. But in doing so, you are forever marked by the magic, destined to watch over the forest as its guardian.")

    def mystic_banish_alone(self):
        self.end_story("You try to banish the curse alone, but the magic overwhelms you. The Huntsman’s shadow claims you, and your soul is bound to the forest, forever a part of the curse.")

    def end_story(self, message):
        self.clear_window()
        end_label = tk.Label(self.root, text=message, font=("Arial", 14), wraplength=1000, justify="center")
        end_label.pack(pady=30)

        restart_button = tk.Button(self.root, text="Restart Journey", command=self.start_game, width=40, height=3)
        restart_button.pack(pady=30)

# Initialize the game
def main():
    root = tk.Tk()
    root.title("The Shadow of the Huntsman")
    root.geometry("1000x800")  # Increased window size to fit the larger buttons and text
    game = ShadowOfTheHuntsman(root)
    game.start_game()
    root.mainloop()

if __name__ == "__main__":
    main()
