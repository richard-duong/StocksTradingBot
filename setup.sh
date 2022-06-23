#!/bin/bash
venv_directory="venv/"
secrets_file=".env"

if [ ! -d "$venv_directory" ];
then
	echo "Creating virtual environment in \`venv/\` ...";	
	python3 -m venv venv || python -m venv venv || echo "Is pip and virtual environment installed? If not, follow these steps: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/"
fi

echo "Installing requirements.txt..."
venv/bin/pip install -r requirements.txt || exit 1;

if [ ! -f "$secrets_file" ];
then
	echo "Creating a secret api key file called \`.env\`";
	cp resources/secrets_template .env;
fi

echo "You're set! Type \`source venv/bin/activate\` to activate the virtual environment and you're free to run any scripts!"
