import os

def run():
    if not os.path.exists('./data'):
        print("The 'data' directory does not exist.")
        return

    files = sorted([f for f in os.listdir('./data') if os.path.isfile(os.path.join('./data', f))])

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


if __name__ == '__main__':
    run()
