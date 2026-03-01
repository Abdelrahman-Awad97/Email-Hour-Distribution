
email_time = {}

user_file = input('Please Enter the Value: ').strip()
if len(user_file) < 1:
    user_file = 'mbox.txt'

with open(f'email-hour-distribution\{user_file}', 'r', encoding='UTF-8') as f:
    for line in f:
        if not line.startswith('From '):
            continue
        line = line.rstrip().split()
        time = line[5].split(':')
        hour = time[0]
        email_time[hour] = email_time.get(hour,0) + 1

# sorting & constructing
for k, v in sorted(email_time.items()):
    print(k, v)