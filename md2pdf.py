import subprocess
import shutil
import os
import argparse

def generate_pdf(markdown_file, template_file, output_pdf):
    try:
        # Extract the output file name (without path and extension)
        output_name = "output"

        # Create a copy of the LaTeX template, with a filename based on the jobname
        temp_template = f"{output_name}.tex"
        with open(template_file, 'r') as file:
            template_content = file.read()

        # Replace './example.md' with the actual markdown file path
        template_content = template_content.replace('./example.md', markdown_file)

        # Write the modified content to a new template file
        with open(temp_template, 'w') as file:
            file.write(template_content)

        # Run pdflatex with the copied and modified template file
        cmd = ["pdflatex", "--shell-escape", f"--jobname={output_name}", temp_template]
        subprocess.run(cmd, check=True)

        # Move the output PDF to the desired path
        generated_pdf = f"{output_name}.pdf"
        shutil.copy(generated_pdf, output_pdf)
        print(f"PDF generated and saved to: {output_pdf}")

        # Clean up temporary files (output.* including the LaTeX template and other additional files)
        for ext in ["pdf", "aux", "log", "out", "tex", "luabridge.lua", "debug-extensions.json"]:
            file_to_delete = f"{output_name}.{ext}"
            if os.path.exists(file_to_delete):
                os.remove(file_to_delete)

        # Clean up temporary directories (_markdown_output, _minted-output)
        for directory in [f"_markdown_{output_name}", f"_minted-{output_name}"]:
            if os.path.exists(directory) and os.path.isdir(directory):
                shutil.rmtree(directory)

        print(f"Temporary files and directories cleaned up.")

    except subprocess.CalledProcessError as e:
        print(f"Error while running pdflatex: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Generate PDF from Markdown and LaTeX template")
    parser.add_argument("markdown_file", help="Path to the Markdown file")
    parser.add_argument("template_file", help="Path to the LaTeX template file")
    parser.add_argument("output_pdf", help="Output PDF filename (with path)")

    args = parser.parse_args()

    # Call the function to generate the PDF
    generate_pdf(args.markdown_file, args.template_file, args.output_pdf)
