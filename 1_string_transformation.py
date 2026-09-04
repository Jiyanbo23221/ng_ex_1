booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

booking = booking.strip()
temp_parts = booking.split('|')

parts = []
for p in temp_parts:
    parts.append(p.strip())

event_code = parts[0]
name_raw = parts[1]
room_raw = parts[2]
time = parts[3]
email = parts[4]
vip_tag = parts[5]

name_parts = name_raw.split('_')
name_new_parts = []
for np in name_parts:
    name_new_parts.append(np.capitalize())
name = '_'.join(name_new_parts)

room = room_raw.upper()

at_pos = email.find('@')
email_domain = email[at_pos + 1:].lower()

vip_count = vip_tag.count('VIP')

valid_event = event_code.startswith('EVT')

has_valid_chars = True
has_underscore = False
for ch in name_raw:
    if not (ch.isalnum() or ch == '_'):
        has_valid_chars = False
    if ch == '_':
        has_underscore = True
valid_username = has_valid_chars and has_underscore

if '-' in room:
    dash_pos = room.find('-')
    prefix = room[:dash_pos]
    suffix = room[dash_pos + 1:]
    if prefix == 'ROOM' and suffix.isdigit():
        valid_room = True
    else:
        valid_room = False
else:
    valid_room = False

time_parts = time.split(':')
if len(time_parts) == 2 and time_parts[0].isdigit() and time_parts[1].isdigit():
    valid_time = True
else:
    valid_time = False

if '@' in email:
    domain_part = email.split('@')[1]
    if '.' in domain_part:
        valid_email = True
    else:
        valid_email = False
else:
    valid_email = False

output = f"""Event code: {event_code}
Name: {name}
Room: {room}
Time: {time}
Email domain: {email_domain}
VIP tag count: {vip_count}
Valid event code: {valid_event}
Valid username: {valid_username}
Valid room: {valid_room}
Valid time: {valid_time}
Valid email: {valid_email}"""

print(output)
