import os

# 検索するIPアドレスのリスト
ip_addresses = [
    "110.47.250.103", "126.227.76.24", "38.207.148.123", "147.45.70.100", "199.119.206.28",
    "38.181.70.3", "149.28.194.95", "78.141.232.174", "38.180.128.159", "64.176.226.203",
    "38.180.106.167", "173.255.223.159", "38.60.218.153", "185.108.105.110", "146.70.192.174",
    "149.88.27.212", "154.223.16.34", "38.180.41.251", "203.160.86.91", "45.121.51.2",
    "172.233.228.93", "66.235.168.222", "144.172.79.92"
]

def extract_ip_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in file:
                if any(ip in line for ip in ip_addresses):
                    outfile.write(line)

def process_all_files(directory):
    # ディレクトリ内のすべての.txtファイルを検索
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(directory, filename)
            output_file_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}_extracted.txt")
            extract_ip_lines(input_file_path, output_file_path)

# プログラムが配置されているディレクトリのパスを取得
current_directory = os.path.dirname(os.path.realpath(__file__))
process_all_files(current_directory)
