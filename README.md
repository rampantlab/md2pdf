# md2pdf

`md2pdf.py` is a Python script that converts a Markdown file to a PDF using a LaTeX template. It runs inside a Docker container and leverages TeX Live for the LaTeX-based PDF generation.

## Features

* Converts Markdown files to PDF using a LaTeX template.
* Leverages `pandoc` for Markdown to LaTeX conversion and `pdflatex` for PDF generation.
* Customizable LaTeX templates for consistent formatting.
* Easily run within a Docker container for consistency across environments.

## Docker Hub Image

This tool is available as a Docker image on Docker Hub. You can pull the latest version of the image from [resistor52/md2pdf](https://hub.docker.com/r/resistor52/md2pdf):

```bash
docker pull resistor52/md2pdf:latest
```

## Usage

You can generate a PDF from a Markdown file using the following command:

```bash
docker run --rm -v $(pwd):/data resistor52/md2pdf /data/example/example.md /data/templates/template.tex /data/example/output.pdf
```

### Arguments

The script requires three arguments:

1. `markdown_file`: The path to the input Markdown file.
2. `template_file`: The path to the LaTeX template file.
3. `output_pdf`: The path where the generated PDF should be saved.

## Using the Bash Script: `markdown2pdf.sh`

For convenience, a bash script (`markdown2pdf.sh`) is provided. This script accepts two arguments: the path to a Markdown file and the path to the output PDF. It simplifies the process by automatically handling file copying and Docker execution with the default `template.tex`.

### Example Usage:

```bash
./markdown2pdf.sh /path/to/markdown.md /path/to/output.pdf
```

This command will generate a PDF using the provided Markdown file and save the output to the specified location.

### Creating a Handy Alias:

You can create an alias to the `markdown2pdf.sh` script for easier use. For example, if the repository is cloned into a folder referred to as `$CODE_WORKSPACE`, you can set up an alias like this:

```bash
alias md2pdf='"$CODE_WORKSPACE/md2pdf/markdown2pdf.sh"'
```

Once the alias is set up, you can simply use:

```bash
md2pdf /path/to/markdown.md /path/to/output.pdf
```

### Debugging Volume Mounts

If you encounter issues with volume mounting, you can override the `ENTRYPOINT` and inspect the mounted directories:

```bash
docker run --rm -v $(pwd):/data --entrypoint bash resistor52/md2pdf -c "ls -R /data"
```

This will list the contents of the `/data` directory inside the container, helping you verify the correct files are mounted.

## Customizing the LaTeX Template

The LaTeX template file allows you to control the appearance of the generated PDF. You can modify the template as needed for your project's requirements. Make sure to pass the correct template path when running the container.
