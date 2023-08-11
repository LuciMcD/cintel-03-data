from shiny import ui 


def get_iris_outputs():
    return ui.panel_main(
        ui.h2("IRISES!"),
        ui.tags.hr(),
        ui.output_text_verbatim("iris_text"),
        ui.tags.section(
            ui.h3("Irises: Types and Sizes"),
            ui.tags.hr(),
            ui.output_plot("iris_plot"),
            ui.tags.hr(),
            ui.h3("Table of Irises"),
            ui.output_table("iris_filtered_table"),
            ui.tags.hr(),

        ),
    )
