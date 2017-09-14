import collections

main_data = []
sender_data = dict()
data = False
with open('mbox.txt', 'r') as file:
    file_data = file.readlines()
    for line in file_data:
        if 'Subject:' in line:
            sender_data['subject'] = line.replace('Subject:', '').strip()
        elif 'Author:' in line:
            sender_data['sender'] = line.replace('Author:', '').strip()
            data = True
        elif data:
            sender_data['date'] = line.replace('Date:', '').strip()
            data = False
        if len(sender_data) == 3:
            print("{sender} ({date}): {subject}".format(sender=sender_data['sender'],
                                                        date=sender_data['date'],
                                                        subject=sender_data['subject']), '\n')
            main_data.append(sender_data)
            sender_data = dict()


count = collections.Counter([author['sender'] for author in main_data])
count_dict = dict(count)
for sender, val in count_dict.items():
    print("{sender}: {val}".format(sender=sender, val=val), '\n')