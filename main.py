import typer
from PyInquirer import prompt, print_json

from utils import helper

app = typer.Typer()


# sortby would be either "ext" or size


@app.command()
def start(dir: str, sortby: str = "ext"):
    if not helper.is_dir_exists(dir):
        typer.echo(f"Directory {dir} does not exist")
        return
    typer.echo(f"Hello {dir}")
    if sortby == "ext":
        sort_by_ext(dir)
    else:
        sort_by_size(dir)


def sort_by_ext(dir: str):
    extensions = helper.get_all_existing_ext_in_dir(dir)
    questions = []
    for ext in extensions:
        if ext == "":
            continue
        question = {
            'type': 'input',
            'name': ext,
            'message': "Where do you want to store all your " + ext + " files"
        }
        questions.append(question)
    answer = ask_questions(questions)
    print(answer)
    helper.move_by_ext(dir, answer)


def ask_questions(questions, include_default=True):
    if include_default:
        questions.append({
            "type": "input",
            "name": "default",
            "message": "Enter the default directory",
            "default": "."
        })
    answers = {
        "default": ""
    }
    for question in questions:
        answer = prompt(question)
        if "--end" in answer.values():
            default = ask_questions([{
                "type": "input",
                "name": "default",
                "message": "Enter the default directory",
                "default": "."
            }], False)
            default = default["default"]
            answer = {"default": default}
            answers.update(answer)
            break
        elif "--pass" in answer.values():
            continue
        answers.update(answer)
    return answers


def sort_by_size(dir):
    pass


if __name__ == "__main__":
    app()
