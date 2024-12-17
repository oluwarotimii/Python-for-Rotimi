import vobject

schools = {
    "Hillcity School": {
        "address": "Graceland, Hillcity Schools No 7, Babanla Street, Tanke, Oko Erin",
        "phone": "0808 897 2243",
        "email": "",
        "hours": "Open ⋅ Closes 4pm"
    },
    "Silver Maple School": {
        "address": "Aleniboro Community, Warrah Road, adjacent Ilorin West Local Government Secretariat, Ilorin.",
        "phone": "09016730903, 08030558865",
        "email": "info@silvermapleschoolilorin.com",
        "hours": "Open ⋅ Closes 4:30pm"
    },
    "Pearls International School": {
        "address": "No 4, Yusuf Idiaro Road, Off Flower Garden, G.R.A, Ilorin.",
        "phone": "0806 068 2301",
        "email": "",
        "hours": "Open ⋅ Closes 5pm"
    },
    "Trove Schools": {
        "address": "133, Hassana complex, shop 29 Ibrahim Taiwo Road Ilorin, Kwara State, Nigeria",
        "phone": "+234 806 0083 609",
        "email": "support@contspro.com",
        "hours": "Open ⋅ Closes 4pm"
    },
    "Royal Palm International College": {
        "address": "GH6J+V54 Kulende Estate Junction, Sango Rd, opposite Federal Training Centre, Oko Erin 240102, Kwara",
        "phone": "0802 943 2993",
        "email": "",
        "hours": "Open ⋅ Closes 5pm"
    },
    "Aderoju International Schools": {
        "address": "Aderoju Sagaya Road, Off Awolowo road, Tanke Rd, Oko Erin",
        "phone": "0916 666 5360",
        "email": "",
        "hours": "Open ⋅ Closes 5pm"
    },
    "Hajrab International School": {
        "address": "GHC7+3WW Along Harmony, behind Toplad Filling Station, Oko Erin 240101, Kwara",
        "phone": "0803 311 9723",
        "email": "",
        "hours": "Open ⋅ Closes 6pm"
    },
    "Seed of Life Academy": {
        "address": "FJR8+336, Ebr Street, Off F-Division Road, Tipper Garage, Tanke, Ilorin, Kwara 240102",
        "phone": "0816 005 3895",
        "email": "",
        "hours": "Open ⋅ Closes 4pm"
    },
    "Excellent International School": {
        "address": "Kudirat, Kuburat Lawal Drive, Tanke, Kwara",
        "phone": "0803 858 0152",
        "email": "",
        "hours": "Open ⋅ Closes 5pm"
    },
    "Flora Schools": {
        "address": "15, Lobalade, Tanke Rd, Avenu, Ilorin 240222",
        "phone": "0704 803 3692",
        "email": "",
        "hours": "Open ⋅ Closes 3am"
    },
    "Socrates College Ilorin": {
        "address": "FGR7+J8X, Oko Erin 240281, Kwara",
        "phone": "0803 390 2049",
        "email": "",
        "hours": "Open ⋅ Closes 4pm"
    },
    "Rehoboth College": {
        "address": "Chapel Road, Off University Road Tanke Ilorin, Kwara State, Nigeria",
        "phone": "+2347044347820",
        "email": "rehobothcollege2022@gmail.com",
        "hours": "Open ⋅ Closes 4pm"
    },
    "Total Child School": {
        "address": "Km11.5 Araromi Village, Lagos Rd, Ilorin",
        "phone": "0803 564 3153",
        "email": "",
        "hours": "Open 24 hours"
    },
    "Ivyhill Academy": {
        "address": "No 10, Watchtower Avenue, beside Jehovah's Witness, Tanke, Ilorin, Kwara State",
        "phone": "08166364677, 07032414392",
        "email": "ivyhillacademyilorin@gmail.com",
        "hours": "Open ⋅ Closes 4pm",
        "social_links": {
            "facebook": "https://web.facebook.com/Ivyhillacademyilorin",
            "instagram": "https://www.instagram.com/ivyhillacademyilorin"
        }
    },
    "Unilorin Secondary School": {
        "address": "FM62+H6F, Ilorin 240102, Kwara",
        "phone": "0705 154 9666",
        "email": "",
        "hours": "Open ⋅ Closes 4pm"
    },
    "Faith Academy Ilorin": {
        "address": "Ilorin 240101, Kwara",
        "phone": "0803 372 6020",
        "email": "",
        "hours": "Open ⋅ Closes 5pm"
    },
    "Effective International College": {
        "address": "Ilorin 240101, Kwara",
        "phone": "0817 6770 624 | 0816 4457 050",
        "email": "enquiries@effectiveinternationalcollege.com",
        "hours": "Open ⋅ Closes 5pm"
    }
}


def create_vcf(schools, fileName="schools_contact.vcf"):
    # Open the file with utf-8 encoding to handle Unicode characters
    with open(fileName, 'w', encoding='utf-8') as vcf_file:
        for school_name, school_info in schools.items():
            # Create a Vcard for each school
            vcard = vobject.vCard()

            # Add Basic details
            vcard.add('fn').value = school_name

            # Add Address in structured format
            address = vcard.add('adr')
            address.type_param = 'HOME'
            address.street = school_info["address"]  # If the full address can fit in street

            # Phone number
            phone = vcard.add('tel')
            phone.type_param = 'CELL'
            phone.value = school_info['phone']

            # Email address (if exists)
            if school_info['email']:
                email = vcard.add('email')
                email.type_param = 'INTERNET'
                email.value = school_info['email']

            # Business Hours
            note = vcard.add('note')
            note.value = f"Business Hours: {school_info['hours']}"

            # Write the vcard into the vcf file
            vcf_file.write(vcard.serialize())
            vcf_file.write("\n")

    print(f"VCF File '{fileName}' created successfully")



# Call for function to create vCard file
create_vcf(schools)
