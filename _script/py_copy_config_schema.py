def append_schema_text(yaml_schema_file: str, text_file: str):
    """Append yaml text to .md file."""
    with open(yaml_schema_file, "r") as f:
        text = f.read()
    schema_text = "\n```yaml\n" + text + "\n```\n"
    schema_text = "\n## Schema:\n" + schema_text
    ### append yaml schema
    with open(text_file, "a") as f:
        f.write(schema_text)
    return


def append_example_config(yaml_config_file: str, text_file: str):
    """Append yaml text to .md file."""
    with open(yaml_config_file, "r") as f:
        text = f.read()
    schema_text = "\n```yaml\n" + text + "\n```\n"
    schema_text = "\n## Example configuration:\n" + schema_text
    ### append yaml schema
    with open(text_file, "a") as f:
        f.write(schema_text)
    return


##### ANCHOR: udpate the blog posts
def main():
    ### Append schema to the .md files
    append_schema_text(yaml_schema_file="./alff/data/schema_arg_gendata.yaml", text_file="./_docs/schema/config_gendata.md")
    append_schema_text(yaml_schema_file="./alff/al/schema_arg_active_learn.yaml", text_file="./_docs/schema/config_active_learning.md")
    append_schema_text(yaml_schema_file="./alff/al/schema_arg_finetune.yaml", text_file="./_docs/schema/config_finetune.md")
    append_schema_text(yaml_schema_file="./alff/phonon/schema_arg_phonon.yaml", text_file="./_docs/schema/config_phonon.md")
    append_schema_text(yaml_schema_file="./alff/elastic/schema_arg_elastic.yaml", text_file="./_docs/schema/config_elastic.md")
    append_schema_text(yaml_schema_file="./alff/util/script/ase_script/schema_arg_ase.yaml", text_file="./_docs/schema/config_ase.md")
    append_schema_text(yaml_schema_file="./alff/util/script/schema/schema_arg_machine.yaml", text_file="./_docs/schema/config_machine.md")
    ### Append example configuration to the .md files
    append_example_config(yaml_config_file="./alff/util/script/example_config/example_param_active_learn.yaml", text_file="./_docs/schema/config_active_learning.md")
    append_example_config(yaml_config_file="./alff/util/script/example_config/example_param_ase.yaml", text_file="./_docs/schema/config_ase.md")
    return


if __name__ == "__main__":
    main()
