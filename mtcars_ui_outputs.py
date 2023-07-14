"""
Purpose: Display outputs for MT Cars dataset.

Choose the correct ui method for the type of output you want to display.
Provide the exact name of the server function that will provide the output.
"""
from shiny import ui


def get_mtcars_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Output (Not Yet Reactive)"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("MT Cars Chart (Seaborn Scatter Plot)"),
            ui.output_plot("mtcars_plot"),
            ui.tags.hr(),
            ui.h3("MT Cars Table"),
            ui.output_text("mtcars_record_count_string"),
            ui.output_table("mtcars_table"),
            ui.tags.hr(),
        ),
    )

def server(input, output, session):
    @output
    @render.text
    def txt():
        return f'cyl: "{input.cyl()}"'


app = App(app_ui, server, debug=True)

