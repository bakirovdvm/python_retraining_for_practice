import json

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def deepCopy(struct, prName, resultDict):

    if prName in struct:
        struct[prName] = resultDict
        return site

    for subStruct in struct.values():
        if isinstance(subStruct, dict):
            result = deepCopy(subStruct, prName, resultDict)
            if result:
                return site



webSiteQuantity = int(input('Введите количество сайтов: '))
# webSiteQuantity = 2

for _ in range(webSiteQuantity):
    productName = input('Введите название продукта для нового сайта: ')
    keyProduct = {'title': f'Куплю/продам {productName} недорого',
           'h2': f'У нас самая низкая цена на {productName}'}
    # print(deepCopy(site, resultDict, productName))
    for i in keyProduct:
        deepCopy(site, i, keyProduct[i])
    print('Сайт для {}:'.format(productName))
    for i in site:
        print(json.dumps(site[i], ensure_ascii=False, indent=4))



