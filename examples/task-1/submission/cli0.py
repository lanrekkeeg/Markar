import click
import requests


@click.group()
def main():
   pass

@main.command()
@click.argument('location')
#@click.pass_context
def current(location):
    """
    Show the current weather for a location using OpenWeatherMap data.
    """

    print(f"The weather in {location} right now: Cold")


    
if __name__ == "__main__":
    main()