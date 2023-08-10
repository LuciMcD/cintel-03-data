from shiny import ui

def get_iris_inputs():
    return ui.panel_sidebar(
        ui.h2("Iris Interaction"),
        ui.tags.hr(),
        ui.h3("Select a species to filter the Table"),
        ui.tags.hr(),
        ui.input_checkbox("IRIS_SPECIES_setosa", "setosa", value=True),
        ui.input_checkbox("IRIS_SPECIES_versicolor", "versicolor", value=True),
        ui.input_checkbox("IRIS_SPECIES_virginica", "virginica", value=True),
        ui.tags.hr(),
        ui.p("Please be patient. Data may take a moment to load"),
        ui.tags.hr(),
    )

