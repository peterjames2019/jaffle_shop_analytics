import json
import os

def merge_dbt_docs():
    search_str = 'o=[{label:"manifest.json",project:true,path:"manifest.json"},{label:"catalog.json",project:true,path:"catalog.json"}]'
    
    # Notice the encoding='utf-8' added below
    with open('target/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    with open('target/manifest.json', 'r', encoding='utf-8') as f:
        json_manifest = json.load(f)

    with open('target/catalog.json', 'r', encoding='utf-8') as f:
        json_catalog = json.load(f)

    new_str = 'o=[{label:"manifest.json",project:true,binary:' + json.dumps(json_manifest) + '},{label:"catalog.json",project:true,binary:' + json.dumps(json_catalog) + '}]'
    
    new_content = content.replace(search_str, new_str)

    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    merge_dbt_docs()