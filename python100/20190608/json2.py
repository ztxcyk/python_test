import json

def main():
    Mydict = {
        'name':'wwm',
        'age':26,
        'Subject':'English',
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(Mydict, file)
    except:
        print('文件错误')
    print('数据保存完成')


if __name__ == '__main__':
    main()