"""
This is a boilerplate pipeline 'download_data'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, node, pipeline

from finance_prediction.pipelines.download_data.nodes import (
    download_data_today,
    save_data,
)


def create_download_data_pipeline_template(**kwargs) -> Pipeline:
    return pipeline(
        pipe=[
            node(
                func=download_data_today,
                inputs='params:symbol',
                outputs='df',
                name='download_data_of_the_day'
            ),
            node(
                func=save_data,
                inputs=["df", "params:symbol", "params:path_data"],
            ),
        ],
        inputs="df",
        outputs=None,
        parameters=["symbol", "path_data"]
    )
