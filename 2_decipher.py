encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

raw_parts = encoded.split('[')

fragments = []
for part in raw_parts:
    if ']' in part:
        content = part.split(']')[0]
        if '::' in content:
            sub_parts = content.split('::')
            if len(sub_parts) == 3:
                num_str = sub_parts[0]
                text = sub_parts[1]
                status = sub_parts[2]
                if status == 'ok' and num_str.isdigit():
                    fragments.append((int(num_str), text))

decoded_parts = []
for num, text in fragments:
    decoded = ''
    for ch in text:
        if ch == '_':
            decoded += ' '
        else:
            idx = alphabet.index(ch)
            new_idx = idx - num
            if new_idx < 0:
                new_idx = new_idx + 26
            decoded += alphabet[new_idx]
    decoded_parts.append((num, decoded))

decoded_parts.sort()

final_message = ''
for i in range(len(decoded_parts)):
    final_message += decoded_parts[i][1]

print(final_message)
