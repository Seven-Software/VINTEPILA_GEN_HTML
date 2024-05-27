export_ui:
	pyuic6 'ui/question.ui' -x -o ./question.py
	pyuic6 'ui/main.ui' -x -o ./main.py
