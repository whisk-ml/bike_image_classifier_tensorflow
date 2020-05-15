import click
import json
from bike_image_classifier_tensorflow.models.model import Model

@click.group()
def cli():
    pass

@cli.command()
@click.argument('x')
def predict(x):
    """
    Generate a model prediction.
    Example usage: bike_image_classifier_tensorflow predict [[1,2],[3,4]]
    """
    model = Model()
    x_parsed = json.loads(x)
    res = model.predict(x_parsed)
    click.echo(res)

if __name__ == "__main__":
    cli()
