from scripts.template import html
from bs4 import BeautifulSoup


class GenHtml:
    def __init__(self, file_html):
        self.html = html
        self.file_html = file_html

    def write_html(self):
        with open(self.file_html, "w") as file:
            file.write(self.html.prettify())

    def add_questions(self, questions):
        self.html = BeautifulSoup(self.html, "html.parser")
        div = self.html.find("div", {"class": "quiz-container"})
        for page, question in enumerate(questions):
            page += 1
            question_container = self.html.new_tag("div")
            question_container["id"] = f"question{page}"
            question_container["class"] = (
                "question-container" " hidden" if page > 1 else ""
            )
            div.append(question_container)

            questions_info = self.html.new_tag("div")
            questions_info["class"] = "question-info"
            questions_info.string = f"Pergunta {page} de {len(questions)}"
            div.append(questions_info)

            questions_question = self.html.new_tag("div")
            questions_question["class"] = "question"
            questions_question.string = question["question"]
            div.append(questions_question)

            div.append(question_container)

            answers = self.html.new_tag("div")
            answers["class"] = "answers"
            for ask, answer in enumerate(question["asks"]):
                ask += 1
                input_ = self.html.new_tag("input")
                input_["type"] = "radio"
                input_["name"] = f"answer{ask}"
                input_["value"] = ask
                input_["onclick"] = f"checkAnswer(1, {len(questions)}, this)"

                label = self.html.new_tag("label")
                label.string = answer

                label.append(input_)
                answers.append(label)
                div.append(answers)


if __name__ == "__main__":
    questions = [
        {
            "question": "Qual a cor do céu?",
            "asks": ["Azul", "Verde", "Amarelo", "Vermelho"],
        },
        {
            "question": "Qual a cor do mar?",
            "asks": ["1", "2", "3", "4"],
        },
    ]
    gen = GenHtml('/tmp/index.html')
    gen.add_questions(questions)
    gen.write_html()
