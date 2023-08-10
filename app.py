"""
Purpose: Use Python to create a continuous intelligence and 
interactive analytics dashboard using Shiny for Python.

Each Shiny app has two parts: 

- a user interface app_ui object (similar to the HTML in a web page) 
- a server function that provides the logic for the app (similar to JS in a web page).

"""
import shinyswatch
from shiny import App, ui, render

from iris_server import get_iris_server_functions
from iris_ui_inputs import get_iris_inputs
from iris_ui_outputs import get_iris_outputs



from util_logger import setup_logger

logger, logname = setup_logger(__name__)

app_ui = ui.page_navbar(
    shinyswatch.theme.solar(),
    ui.nav(
        "Home",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.h2("Let's get some information."),
                ui.tags.hr(),
                ui.input_text("name_input", "What's your name?", placeholder="Your Name"),
                ui.input_text(
                    "season_input",
                    "What's your favorite season?",
                    placeholder="My favorite season is...",
                ),
                ui.input_text("allergy_input", "Do you have allergies?", placeholder="Yes or No"),
                ui.tags.hr(),
            ),
            ui.panel_main(
                ui.h2("New Tabs (see above)"),
                ui.tags.hr(),
                ui.tags.ul(
                    ui.tags.li("To read about the different species of Irises click the link above."),
                    ui.tags.li("The Classmate's App tab will take you to an app I admire"),
                    ui.tags.li("The How to Video will help you with growing your own Irises"),
                ),
                ui.tags.hr(),
                ui.h2("Main Panel with Reactive Output"),
                ui.tags.hr(),
                ui.output_text_verbatim("welcome_output"),
                ui.output_text_verbatim("insights_output"),
                ui.output_text_verbatim("third_output"),
                ui.tags.hr(),
            ),
        ),
    ),
   
    ui.nav("Irises",
       ui.layout_sidebar(
           get_iris_inputs(),
           get_iris_outputs(),
       ),
    ),
  


    ui.nav(ui.a("About", href="https://github.com/LuciMcD")),
    ui.nav(ui.a("GitHub", href="https://github.com/LuciMcD/cintel-03-data")),
    ui.nav(ui.a("Classmate's App", href="https://bethharvey.shinyapps.io/cintel-05-live-updates/")),
    ui.nav(ui.a("How To Video", href="https://www.youtube.com/watch?v=XI3iMgfIXlY")),
    title=ui.h1("McDaniel Dashboard"),
)

def server(input, output, session):
    """Define functions to create UI outputs."""

    @output
    @render.text
    def welcome_output():
        user = input.name_input()
        welcome_string = f"Bless you, {user}!"
        return welcome_string

    @output
    @render.text
    def insights_output():
        answer = input.season_input()
        season_string = f"Your favorite season is {answer}. Thats's great for you!"
        return season_string
    
    @output
    @render.text
    def third_output():
        choice = input.allergy_input()
        third_string = f"{choice}. Allergies are NOT fun."
        return third_string

    
   
    get_iris_server_functions(input, output, session)

app = App(app_ui, server)
