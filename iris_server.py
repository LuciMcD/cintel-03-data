
"""
Provide information and photos of the different species of Iris flowers.
"""

import pathlib
from shiny import render, reactive
import pandas as pd
import seaborn as sns


from util_logger import setup_logger

logger, logname = setup_logger(__name__)



def get_iris_server_functions(input, output, session):
    path_to_data = pathlib.Path(__file__).parent.joinpath("data").joinpath("iris.csv")
    original_df = pd.read_csv(path_to_data)
    total_count = len(original_df)

    reactive_df = reactive.Value()

    @reactive.Effect
    @reactive.event(
        input.IRIS_SPECIES_setosa,
        input.IRIS_SPECIES_versicolor,
        input.IRIS_SPECIES_virginica,
    )

    def _():
        df = original_df

        show_species_list = []
        if input.IRIS_SPECIES_setosa():
            show_species_list.append("setosa")
        if input.IRIS_SPECIES_versicolor():
            show_species_list.append("versicolor")
        if input.IRIS_SPECIES_virginica():
            show_species_list.append("virginica")
        show_species_list = show_species_list or ["setosa", "versicolor", "virginica"]
        species_filter = df["species"].isin(show_species_list)
        df = df[species_filter]

        reactive_df.set(df)

    @output
    @render.table
    def iris_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df

    
    @output
    @render.plot
    def iris_plot():
        df = original_df
        plt = sns.scatterplot(
            data=df,
            x="sepal_width", 
            y="sepal_length", 
            hue="species", 
            size='petal_length',
        )
        return plt
    
    @output
    @render.text
    def iris_text():
        message = ("Iris is a flowering plant genus of 310 accepted species with showy flowers. Iris is also widely used as a common name for all Iris species.")
        return message

    return [
        iris_filtered_table,
        iris_plot,
        iris_text
    ]        

    