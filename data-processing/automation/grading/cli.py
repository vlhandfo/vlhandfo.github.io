import sys
import argparse
from template import generate_md_file

def main(argv=None):
	if argv is None:
		argv = sys.argv[1:]
	
	parser = argparse.ArgumentParser(description="Feedback template generator",
					epilog="input: 'test' for using 'test.html' as test input.")

	parser.add_argument("input", help="The assignment as an .html file")
	parser.add_argument("-o", help="The name of the output file", 
					 default="template.md", dest="output")
	parser.add_argument("-n", type=str, default="Feedback", dest="name",
					 help="The name/title of the assignment, ex) Oblig 1a - Feedback")
	parser.add_argument("-d", "--directory", help="The parent directory of the"\
					 "student directory")
	parser.add_argument("-m", "--mail", help="The included contact email",
					default="vlhandfo@ifi.uio.no")
					# default="in1140-hjelp@ifi.uio.no")
	parser.add_argument("-g", "--gif", help="The included gif at the end",
					 default="https://media.giphy.com/media/lS0uOmv9Mg63EWYDHF/giphy.gif")
	
	args = parser.parse_args()

	if args.input == "test":
		args.input = "test.html"
		
	generate_md_file(args.input, args.output, args.name, args.mail, args.gif)
	return args

if __name__ == "__main__":
	main(sys.argv[1:])