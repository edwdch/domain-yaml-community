import os

'''
# comments
include:another-file
domain:google.com @attr1 @attr2
keyword:google
regexp:www\.google\.com$
full:www.google.com
'''


def run():
    if not os.path.exists('./data'):
        print("The 'data' directory does not exist.")
        return
    if not os.path.exists('./yaml'):
        os.makedirs('./yaml')

    files = [f for f in os.listdir('./data') if os.path.isfile(os.path.join('./data', f))]

    for file in files:
        try:
            content = get_full_file_content(file)
            if len(content) == 0:
                continue

            tag_mapping = {}

            for line in content:
                tags = [""]
                split_lines = line.split(" ")
                if len(split_lines) > 1:
                    tags.extend(split_lines[1:])

                line = split_lines[0]

                if is_keyword(line):
                    continue
                elif is_full(line):
                    domain = line.replace("full:", "")
                elif is_domain(line):
                    domain = "+." + line.replace("domain:", "")
                elif is_regexp(line):
                    continue
                else:
                    continue

                for tag in tags:
                    if tag not in tag_mapping:
                        tag_mapping[tag] = []
                    tag_mapping[tag].append(domain)

            for tag in tag_mapping:
                new_file_name = os.path.splitext(file)[0] + tag + '.txt'

                with open(os.path.join('./yaml', new_file_name), 'w', encoding='utf-8') as f:
                    f.write('payload:\n')
                    for p in tag_mapping[tag]:
                        f.write('- ' + p + '\n')

        except IOError as e:
            print(f"An IOError occurred while processing '{file}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred while processing '{file}': {e}")


file_content_mapping = {}


def get_full_file_content(filename) -> list[str]:
    if filename not in file_content_mapping:
        with open(os.path.join('./data', filename), 'r', encoding='utf-8') as f:
            lines = f.readlines()

        result = []

        for line in lines:
            line = strip_line(line)
            if line == "":
                continue

            if is_comment(line):
                continue

            if is_include(line):
                include_filename = line.replace("include:", "")
                result.extend(get_full_file_content(include_filename))
            else:
                result.append(line)

        file_content_mapping[filename] = result
    return file_content_mapping[filename]


def strip_line(line: str) -> str:
    if not line or line.strip() == "":
        return ""
    if "#" in line:
        return line.split("#")[0].strip()
    return line.strip()


def is_comment(line: str) -> bool:
    return line.startswith("#")


def is_include(line: str) -> bool:
    return line.startswith("include:")


def is_domain(line: str) -> bool:
    return line.startswith("domain:") or ":" not in line


def is_keyword(line: str) -> bool:
    return line.startswith("keyword:") or "." not in line


def is_regexp(line: str) -> bool:
    return line.startswith("regexp:")


def is_full(line: str) -> bool:
    return line.startswith("full:")


if __name__ == '__main__':
    run()
