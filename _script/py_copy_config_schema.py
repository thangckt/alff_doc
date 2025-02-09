import requests


def read_schema_text(yaml_schema_file: str) -> str:
    """Read text from a file."""
    with open(yaml_schema_file, "r") as f:
        text = f.read()
    text = "```yaml\n" + text + "```\n"
    return text

def append_schema_text(yaml_schema_file: str, text_file: str):
    """Append text to a file."""
    schema_text = read_schema_text(yaml_schema_file)
    with open(text_file, "a") as f:
        f.write(schema_text)
    return







##### ANCHOR: udpate the blog posts
def main():
    ### Post 1
    append_schema_text(yaml_schema_file="./alff/util/script/ase_script/schema_ARG_ASE.yaml", text_file="./_docs/schemas/schema_ase.md")


    return


if __name__ == "__main__":
    main()
