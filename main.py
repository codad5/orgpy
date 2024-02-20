import typer
from PyInquirer import prompt, print_json

from utils import helper

app = typer.Typer()

ext_to_path_mapping = {}


@app.command()
def hello(dir: str):
    typer.echo(f"Hello {dir}")
    extensions = helper.get_all_existing_ext_in_dir(dir)
    questions = []
    for ext in extensions:
        question = {
            'type': 'input',
            'name': ext,
            'message': "Where do you want to store all your " + ext + " files"
        }
        questions.append(question)
    answer = prompt(questions)
    print_json(answer)


if __name__ == "__main__":
    app()
