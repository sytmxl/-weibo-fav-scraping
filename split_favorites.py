import json
import os

# 配置
input_file = 'favorites.json'
output_dir = 'output'  # 生成文件存放的目录
items_per_file = 20  # 每个文件包含的条目数量

# 读取 JSON 文件
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

status_list = data['data']['status']
print(len(status_list))
# 确保数据列表不是空的
if not status_list:
    print('Status list is empty')
    exit(1)

# 创建输出目录（如果不存在）
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 分割数据并写入文件
total_items = len(status_list)
print(f'Total items to split: {total_items}')

for i in range(0, total_items, items_per_file):
    chunk = status_list[i:i + items_per_file]
    output_file = os.path.join(output_dir, f'favorites_part_{(i // items_per_file) + 1}.json')
    
    output_data = {
        'ok': 1,
        'data': {
            'status': chunk
        }
    }
    
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(output_data, file, ensure_ascii=False, indent=2)
    
    print(f'Successfully wrote {output_file} with {len(chunk)} items')

print('Data splitting completed.')
