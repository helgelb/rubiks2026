set shell := ["bash", "-cu"]

src_dir := "src"

help:
	@just --list

process:
	cd {{src_dir}} && python process.py

query:
	cd {{src_dir}} && python support/query_output.py

test:
	cd {{src_dir}} && pytest -q

demo:
	cd {{src_dir}} && bash run_demo.sh

container-build:
	cd {{src_dir}} && docker build -t rubiks-demo .

container-run:
	cd {{src_dir}} && docker run --rm -v "$PWD/output:/app/output" rubiks-demo
