#!/usr/bin/python3.7


import os
import re
import argparse


def update_phone_number(old_phone_number):
    new_phone_number = ""
    if 2 <= int(old_phone_number[0]) <= 3:
        if int(old_phone_number[2]) == 8:
            new_phone_number = "21" + old_phone_number
        elif int(old_phone_number[2]) == 0:
            new_phone_number = "25" + old_phone_number
        else:
            new_phone_number = "27" + old_phone_number
    else:
        if 0 <= int(old_phone_number[1]) <= 3:
            new_phone_number = "01" + old_phone_number
        elif 4 <= int(old_phone_number[1]) <= 6:
            new_phone_number = "05" + old_phone_number
        elif 7 <= int(old_phone_number[1]) <= 9:
            new_phone_number = "07" + old_phone_number
    return new_phone_number


def create_vcard_update(filepath, filename="contact_update"):
    pattern_with_plus = r"\+?225[-.\s|]?(\d{8}|\d{2}[-.\s]\d{2}[-.\s]\d{2}[-.\s]\d{2})"
    pattern_with_zero_x2 = r"00?225[-.\s|]?(\d{8}|\d{2}[-.\s]\d{2}[-.\s]\d{2}[-.\s]\d{2})"
    pattern_without_internationalization = r"(\d{8}|\d{2}[-.\s]\d{2}[-.\s]\d{2}[-.\s]\d{2})"

    with open(filename + ".vcf", 'w') as new_vcard_file:

        with open(filepath, 'r') as old_vcard_file:

            for line in old_vcard_file.readlines():
                match_object = re.search(pattern_with_plus, line) or re.search(pattern_with_zero_x2, line) or re.search(
                    pattern_without_internationalization, line)

                if match_object is not None:
                    phone_number = line[match_object.start(): match_object.end()][-8:]
                    new_line = re.sub(phone_number, update_phone_number(phone_number), line)
                    new_vcard_file.write(new_line)
                else:
                    new_vcard_file.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help="path to your vcf file")
    parser.add_argument('-o', '--output', help="the name of the output or new vcf name")
    args = parser.parse_args()

    if args.input and args.output and os.path.isfile(args.input):

        if args.input.split('.')[-1] == 'vcf':
            create_vcard_update(args.input, args.output)
        else:
            print("Only vcf file can be handle with this script")
    else:
        print("type \"main.py -h\" to get help")
