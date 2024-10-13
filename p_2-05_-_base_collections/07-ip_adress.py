# ip = '128.16.35.a4'
# ip = '240.127.56.340'
# ip = '34.56.42,5'
ip = '128.0.0.255'

ip_list = ip.split('.')
print(ip_list, len(ip_list))

error = 0
if len(ip_list) != 4:
    print('Адрес — это четыре числа, разделённые точками')
    error += 1
else:
    for i in ip_list:
        if i.isdigit():
            if int(i) > 255:
                print(i, 'превышает 255')
                error += 1
                # break
        else:
            print(i, '- это не целое число')
            error += 1
            # break

if error == 0:
    print('IP-адрес корректен')


