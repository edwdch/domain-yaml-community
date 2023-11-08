import os


def run():
    # 确保 data 目录存在
    if not os.path.exists('./data'):
        print("The 'data' directory does not exist.")
        return
    if not os.path.exists('./yaml'):
        os.makedirs('./yaml')

    # 获取当前目录下的所有文件
    files = [f for f in os.listdir('./data') if os.path.isfile(os.path.join('./data', f))]

    for file in files:
        # 初始化payload
        payload = []
        try:
            # 读取文件内容
            with open(os.path.join('./data', file), 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # 读取每行内容，组成 yaml 格式
            for line in lines:
                domain = line.strip()
                if not domain:
                    continue
                if '#' in domain:
                    continue
                if len(domain.split(" ")) > 1:
                    domain = domain.split(" ")[0]
                if domain.startswith("full:"):
                    domain = domain.split("full:")[1]

                payload.append(domain)

            # 拼接新的文件名，确保替换掉最后的后缀名
            new_file_name = os.path.splitext(file)[0] + '.txt'

            # 保存至 yaml 目录下
            with open(os.path.join('./yaml', new_file_name), 'w', encoding='utf-8') as f:
                f.write('payload:\n')
                for p in payload:
                    f.write('- ' + p + '\n')

        except IOError as e:
            print(f"An IOError occurred while processing '{file}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred while processing '{file}': {e}")


if __name__ == '__main__':
    run()
