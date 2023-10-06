""" Generates Feedback Templates using CLI

Takes in the information for the feedback template and puts in nicely in a .md
file. 

`generate_md_file()` also used for generating feedback for all student 
subdirectories in a given assignment. 
"""

from bs4 import BeautifulSoup
from pathlib import Path
import warnings

# I know this is bad, but .ipynb to .html causes problems
warnings.filterwarnings("ignore")  

def _check_input(filename: str) -> str:
	"""Validates input filepath"""
	#TODO
	path = Path(filename)
	return filename 

def _check_output(filename: str) -> str:
	"""Validates out filepath"""
	#TODO
	if filename.endswith(".md"):
		return filename
	
	filename += ".md"
	return filename
	

def generate_md_file(input_file: str, output_file: str, title: str,
					 epost: str, gif: str, pts: int=100):

	input_file = _check_input(input_file)
	output_file = _check_output(output_file)

	with open(input_file) as f:
		soup = BeautifulSoup(f.read(), "html")

	tasks = soup.find_all('h1')

	with open(output_file, "w") as out:
		out.write(f"# {title}\n")
		out.write("## Generelt \n")
		out.write("Alt i alt har du levert en kjempe god oppgave!\n\n")
		
		for task in tasks:
			out.write("## " + task.text[:-1] + "\n\n-\n\n")

		out.write("---\n\n")
		out.write(f"## Totalt: (###/{pts} poeng)\n\n")
		out.write(f"![gif]({gif})\n\n")
		out.write(f"Send mail til [{epost}](mailto:mail) hvis du lurer på noe 😄\n")
		out.write("Lykke til på neste oblig!")

	return input_file, output_file
