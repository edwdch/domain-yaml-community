import os
import json

def generate_icon_json(folder_name, output_file, display_name):
    """Generate JSON file for icons in a specific folder"""
    folder_path = f'./data/orz-3-mini/{folder_name}'
    
    if not os.path.exists(folder_path):
        print(f"Warning: The '{folder_path}' directory does not exist.")
        return
    
    # Get all image files (png, jpg, jpeg, svg)
    image_extensions = {'.png', '.jpg', '.jpeg', '.svg', '.webp'}
    files = sorted([
        f for f in os.listdir(folder_path) 
        if os.path.isfile(os.path.join(folder_path, f)) and 
        os.path.splitext(f)[1].lower() in image_extensions
    ])
    
    # Build JSON structure
    icons_data = {
        "name": display_name,
        "icons": [
            {
                "name": filename,
                "url": f"https://raw.githubusercontent.com/Orz-3/mini/master/{folder_name}/{filename}"
            }
            for filename in files
        ]
    }
    
    # Write JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(icons_data, f, ensure_ascii=False, indent=2)
    
    print(f"Generated {output_file} with {len(files)} icons from {folder_name}/")

def generate_geosite_list():
    """Generate geosite-list.md from domain-list-community data"""
    data_dir = './data/domain-list-community/data'
    if not os.path.exists(data_dir):
        print(f"The '{data_dir}' directory does not exist.")
        return

    files = sorted([f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))])

    category_files = [f for f in files if f.startswith('category-')]
    other_files = [f for f in files if not f.startswith('category-')]

    with open('geosite-list.md', 'w', encoding='utf-8') as f:
        f.write('# Geosite List\n\n')
        f.write(f'Total: {len(files)} files\n\n')
        
        f.write(f'## Category ({len(category_files)})\n\n')
        f.write('| Name | Source |\n')
        f.write('| --- | --- |\n')
        for file in category_files:
            f.write(f'| {file} | [![GitHub](https://img.shields.io/badge/-source-gray?logo=github)](https://github.com/v2fly/domain-list-community/blob/master/data/{file}) |\n')
        
        f.write(f'\n## Others ({len(other_files)})\n\n')
        f.write('| Name | Source |\n')
        f.write('| --- | --- |\n')
        for file in other_files:
            f.write(f'| {file} | [![GitHub](https://img.shields.io/badge/-source-gray?logo=github)](https://github.com/v2fly/domain-list-community/blob/master/data/{file}) |\n')

    print(f"Generated geosite-list.md with {len(files)} entries.")

def run():
    # Generate geosite list
    generate_geosite_list()
    
    # Create icons directory if it doesn't exist
    os.makedirs('icons', exist_ok=True)
    
    # Generate icon JSON files
    generate_icon_json('Alpha', 'icons/orz-3-mini.alpha.json', 'Orz-3 Mini Alpha (All)')
    generate_icon_json('Color', 'icons/orz-3-mini.color.json', 'Orz-3 Mini Color (All)')


if __name__ == '__main__':
    run()
