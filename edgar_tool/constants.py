from typing_extensions import Literal

SUPPORTED_OUTPUT_EXTENSIONS = [".csv", ".jsonl", ".json"]
TEXT_SEARCH_BASE_URL = "https://efts.sec.gov/LATEST/search-index?"
TEXT_SEARCH_SPLIT_BATCHES_NUMBER = 2
TEXT_SEARCH_CSV_FIELDS_NAMES = [
    "root_form",
    "form_name",
    "filed_at",
    "reporting_for",
    "entity_name",
    "ticker",
    "company_cik",
    "company_cik_trimmed",
    "place_of_business",
    "incorporated_location",
    "file_num",
    "film_num",
    "file_num_search_url",
    "filing_details_url",
    "filing_document_url",
]
RSS_FEED_CSV_FIELDS_NAMES = [
    "company_name",
    "cik",
    "trimmed_cik",
    "ticker",
    "published_date",
    "title",
    "link",
    "description",
    "form",
    "filing_date",
    "file_number",
    "accession_number",
    "acceptance_date",
    "period",
    "assistant_director",
    "assigned_sic",
    "fiscal_year_end",
    "xbrl_files",
]

"""All mappings below are from the SEC EDGAR website's search form.
The keys are the values that the CLI uses, and the values are those
that the search form uses. All values are shown in the order they
appear in the SEC EDGAR search drop down."""
PEO_IN_AND_INC_IN_TO_SEC_FORM_ID = {
    # US States
    "AL": "AL",
    "AK": "AK",
    "AZ": "AZ",
    "AR": "AR",
    "CA": "CA",
    "CO": "CO",
    "CT": "CT",
    "DE": "DE",
    "DC": "DC",
    "FL": "FL",
    "GA": "GA",
    "HI": "HI",
    "ID": "ID",
    "IL": "IL",
    "IN": "IN",
    "IA": "IA",
    "KS": "KS",
    "KY": "KY",
    "LA": "LA",
    "ME": "ME",
    "MD": "MD",
    "MA": "MA",
    "MI": "MI",
    "MN": "MN",
    "MS": "MS",
    "MO": "MO",
    "MT": "MT",
    "NE": "NE",
    "NV": "NV",
    "NH": "NH",
    "NJ": "NJ",
    "NM": "NM",
    "NY": "NY",
    "NC": "NC",
    "ND": "ND",
    "OH": "OH",
    "OK": "OK",
    "OR": "OR",
    "PA": "PA",
    "RI": "RI",
    "SC": "SC",
    "SD": "SD",
    "TN": "TN",
    "TX": "TX",
    "UT": "UT",
    "VT": "VT",
    "VA": "VA",
    "WA": "WA",
    "WV": "WV",
    "WI": "WI",
    "WY": "WY",
    # Canadian Provinces
    "AB": "A0",
    "BC": "A1",
    "CAN": "Z4",  # Canada (Federal Level)
    "MB": "A2",
    "NB": "A3",
    "NL": "A4",
    "NS": "A5",
    "ON": "A6",
    "PE": "A7",
    "QC": "A8",
    "SK": "A9",
    "YT": "B0",
    # Countries
    "AFG": "B2",
    "ALA": "Y6",
    "ALB": "B3",
    "DZA": "B4",
    "ASM": "B5",
    "AND": "B6",
    "AGO": "B7",
    "AIA": "1A",
    "ATA": "B8",
    "ATG": "B9",
    "ARG": "C1",
    "ARM": "1B",
    "ABW": "1C",
    "AUS": "C3",
    "AUT": "C4",
    "AZE": "1D",
    "BHS": "C5",
    "BHR": "C6",
    "BGD": "C7",
    "BRB": "C8",
    "BLR": "1F",
    "BEL": "C9",
    "BLZ": "D1",
    "BEN": "G6",
    "BMU": "D0",
    "BTN": "D2",
    "BOL": "D3",
    "BIH": "1E",
    "BWA": "B1",
    "BVT": "D4",
    "BRA": "D5",
    "IOT": "D6",
    "BRN": "D9",
    "BGR": "E0",
    "BFA": "X2",
    "BDI": "E2",
    "KHM": "E3",
    "CMR": "E4",
    "CPV": "E8",
    "CYM": "E9",
    "CAF": "F0",
    "TCD": "F2",
    "CHL": "F3",
    "CHN": "F4",
    "CXR": "F6",
    "CCK": "F7",
    "COL": "F8",
    "COM": "F9",
    "COG": "G0",
    "COD": "Y3",
    "COK": "G1",
    "CRI": "G2",
    "CIV": "L7",
    "HRV": "1M",
    "CUB": "G3",
    "CYP": "G4",
    "CZE": "2N",
    "DNK": "G7",
    "DJI": "1G",
    "DMA": "G9",
    "DOM": "D8",
    "ECU": "H1",
    "EGY": "H2",
    "SLV": "H3",
    "GNQ": "H4",
    "ERI": "1J",
    "EST": "1H",
    "ETH": "H5",
    "FLK": "H7",
    "FRO": "H6",
    "FJI": "H8",
    "FIN": "H9",
    "FRA": "I0",
    "GUF": "I3",
    "PYF": "I4",
    "ATF": "2C",
    "GAB": "I5",
    "GMB": "I6",
    "GEO": "2Q",
    "DEU": "2M",
    "GHA": "J0",
    "GIB": "J1",
    "GRC": "J3",
    "GRL": "J4",
    "GRD": "J5",
    "GLP": "J6",
    "GUM": "GU",
    "GTM": "J8",
    "GGY": "Y7",
    "GIN": "J9",
    "GNB": "S0",
    "GUY": "K0",
    "HTI": "K1",
    "HMD": "K4",
    "VAT": "X4",
    "HND": "K2",
    "HKG": "K3",
    "HUN": "K5",
    "ISL": "K6",
    "IND": "K7",
    "IDN": "K8",
    "IRN": "K9",
    "IRQ": "L0",
    "IRL": "L2",
    "IMN": "Y8",
    "ISR": "L3",
    "ITA": "L6",
    "JAM": "L8",
    "JPN": "M0",
    "JEY": "Y9",
    "JOR": "M2",
    "KAZ": "1P",
    "KEN": "M3",
    "KIR": "J2",
    "PRK": "M4",
    "KOR": "M5",
    "KWT": "M6",
    "KGZ": "1N",
    "LAO": "M7",
    "LVA": "1R",
    "LBN": "M8",
    "LSO": "M9",
    "LBR": "N0",
    "LBY": "N1",
    "LIE": "N2",
    "LTU": "1Q",
    "LUX": "N4",
    "MAC": "N5",
    "MKD": "1U",
    "MDG": "N6",
    "MWI": "N7",
    "MYS": "N8",
    "MDV": "N9",
    "MLI": "O0",
    "MLT": "O1",
    "MHL": "1T",
    "MTQ": "O2",
    "MRT": "O3",
    "MUS": "O4",
    "MYT": "2P",
    "MEX": "O5",
    "FSM": "1K",
    "MDA": "1S",
    "MCO": "O9",
    "MNG": "P0",
    "MNE": "Z5",
    "MSR": "P1",
    "MAR": "P2",
    "MOZ": "P3",
    "MMR": "E1",
    "NAM": "T6",
    "NRU": "P5",
    "NPL": "P6",
    "NLD": "P7",
    "ANT": "P8",
    "NCL": "1W",
    "NZL": "Q2",
    "NIC": "Q3",
    "NER": "Q4",
    "NGA": "Q5",
    "NIU": "Q6",
    "NFK": "Q7",
    "MNP": "1V",
    "NOR": "Q8",
    "OMN": "P4",
    "PAK": "R0",
    "PLW": "1Y",
    "PSE": "1X",
    "PAN": "R1",
    "PNG": "R2",
    "PRY": "R4",
    "PER": "R5",
    "PHL": "R6",
    "PCN": "R8",
    "POL": "R9",
    "PRT": "S1",
    "PRI": "PR",
    "QAT": "S3",
    "REU": "S4",
    "ROU": "S5",
    "RUS": "1Z",
    "RWA": "S6",
    "BLM": "Z0",
    "SHN": "U8",
    "KNA": "U7",
    "LCA": "U9",
    "MAF": "Z1",
    "SPM": "V0",
    "VCT": "V1",
    "WSM": "Y0",
    "SMR": "S8",
    "STP": "S9",
    "SAU": "T0",
    "SEN": "T1",
    "SRB": "Z2",
    "SYC": "T2",
    "SLE": "T8",
    "SGP": "U0",
    "SVK": "2B",
    "SVN": "2A",
    "SLB": "D7",
    "SOM": "U1",
    "ZAF": "T3",
    "SGS": "1L",
    "ESP": "U3",
    "LKA": "F1",
    "SDN": "V2",
    "SUR": "V3",
    "SJM": "L9",
    "SWZ": "V6",
    "SWE": "V7",
    "CHE": "V8",
    "SYR": "V9",
    "TWN": "F5",
    "TJK": "2D",
    "THA": "W1",
    "TLS": "Z3",
    "TGO": "W2",
    "TKL": "W3",
    "TON": "W4",
    "TTO": "W5",
    "TUN": "W6",
    "TUR": "W8",
    "TKM": "2E",
    "TCA": "W7",
    "TUV": "2G",
    "UGA": "W9",
    "UKR": "2H",
    "ARE": "C0",
    "GBR": "X0",
    "UMI": "2J",
    "URY": "X3",
    "UZB": "2K",
    "VUT": "2L",
    "VEN": "X5",
    "VNM": "Q1",
    "VGB": "D8",
    "VIR": "VI",
    "WLF": "X8",
    "ESH": "Y1",
    "YEM": "T7",
    "ZMB": "Y4",
    "ZWE": "Y5",
    "XX": "XX",
}

TEXT_SEARCH_LOCATIONS_MAPPING = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District of Columbia",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "X1": "United States",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming",
    "A0": "Alberta, Canada",
    "A1": "British Columbia, Canada",
    "Z4": "Canada (Federal Level)",
    "A2": "Manitoba, Canada",
    "A3": "New Brunswick, Canada",
    "A4": "Newfoundland, Canada",
    "A5": "Nova Scotia, Canada",
    "A6": "Ontario, Canada",
    "A7": "Prince Edward Island, Canada",
    "A8": "Quebec, Canada",
    "A9": "Saskatchewan, Canada",
    "B0": "Yukon, Canada",
    "B2": "Afghanistan",
    "Y6": "Aland Islands",
    "B3": "Albania",
    "B4": "Algeria",
    "B5": "American Samoa",
    "B6": "Andorra",
    "B7": "Angola",
    "1A": "Anguilla",
    "B8": "Antarctica",
    "B9": "Antigua and Barbuda",
    "C1": "Argentina",
    "1B": "Armenia",
    "1C": "Aruba",
    "C3": "Australia",
    "C4": "Austria",
    "1D": "Azerbaijan",
    "C5": "Bahamas",
    "C6": "Bahrain",
    "C7": "Bangladesh",
    "C8": "Barbados",
    "1F": "Belarus",
    "C9": "Belgium",
    "D1": "Belize",
    "G6": "Benin",
    "D0": "Bermuda",
    "D2": "Bhutan",
    "D3": "Bolivia",
    "1E": "Bosnia and Herzegovina",
    "B1": "Botswana",
    "D4": "Bouvet Island",
    "D5": "Brazil",
    "D6": "British Indian Ocean Territory",
    "D9": "Brunei Darussalam",
    "E0": "Bulgaria",
    "X2": "Burkina Faso",
    "E2": "Burundi",
    "E3": "Cambodia",
    "E4": "Cameroon",
    "E8": "Cape Verde",
    "E9": "Cayman Islands",
    "F0": "Central African Republic",
    "F2": "Chad",
    "F3": "Chile",
    "F4": "China",
    "F6": "Christmas Island",
    "F7": "Cocos (Keeling) Islands",
    "F8": "Colombia",
    "F9": "Comoros",
    "G0": "Congo",
    "Y3": "Congo, the Democratic Republic of the",
    "G1": "Cook Islands",
    "G2": "Costa Rica",
    "L7": "Cote D'ivoire ",
    "1M": "Croatia",
    "G3": "Cuba",
    "G4": "Cyprus",
    "2N": "Czech Republic",
    "G7": "Denmark",
    "1G": "Djibouti",
    "G9": "Dominica",
    "G8": "Dominican Republic",
    "H1": "Ecuador",
    "H2": "Egypt",
    "H3": "El Salvador",
    "H4": "Equatorial Guinea",
    "1J": "Eritrea",
    "1H": "Estonia",
    "H5": "Ethiopia",
    "H7": "Falkland Islands (Malvinas)",
    "H6": "Faroe Islands",
    "H8": "Fiji",
    "H9": "Finland",
    "I0": "France",
    "I3": "French Guiana",
    "I4": "French Polynesia",
    "2C": "French Southern Territories",
    "I5": "Gabon",
    "I6": "Gambia",
    "2Q": "Georgia (country)",
    "2M": "Germany",
    "J0": "Ghana",
    "J1": "Gibraltar",
    "J3": "Greece",
    "J4": "Greenland",
    "J5": "Grenada",
    "J6": "Guadeloupe",
    "GU": "Guam",
    "J8": "Guatemala",
    "Y7": "Guernsey",
    "J9": "Guinea",
    "S0": "Guinea-bissau",
    "K0": "Guyana",
    "K1": "Haiti",
    "K4": "Heard Island and Mcdonald Islands",
    "X4": "Holy See (Vatican City State)",
    "K2": "Honduras",
    "K3": "Hong Kong",
    "K5": "Hungary",
    "K6": "Iceland",
    "K7": "India",
    "K8": "Indonesia",
    "K9": "Iran, Islamic Republic of",
    "L0": "Iraq",
    "L2": "Ireland",
    "Y8": "Isle of Man",
    "L3": "Israel",
    "L6": "Italy",
    "L8": "Jamaica",
    "M0": "Japan",
    "Y9": "Jersey",
    "M2": "Jordan",
    "1P": "Kazakhstan",
    "M3": "Kenya",
    "J2": "Kiribati",
    "M4": "Korea, Democratic People's Republic of ",
    "M5": "Korea, Republic of",
    "M6": "Kuwait",
    "1N": "Kyrgyzstan",
    "M7": "Lao People's Democratic Republic ",
    "1R": "Latvia",
    "M8": "Lebanon",
    "M9": "Lesotho",
    "N0": "Liberia",
    "N1": "Libyan Arab Jamahiriya",
    "N2": "Liechtenstein",
    "1Q": "Lithuania",
    "N4": "Luxembourg",
    "N5": "Macau",
    "1U": "Macedonia, the Former Yugoslav Republic of",
    "N6": "Madagascar",
    "N7": "Malawi",
    "N8": "Malaysia",
    "N9": "Maldives",
    "O0": "Mali",
    "O1": "Malta",
    "1T": "Marshall Islands",
    "O2": "Martinique",
    "O3": "Mauritania",
    "O4": "Mauritius",
    "2P": "Mayotte",
    "O5": "Mexico",
    "1K": "Micronesia, Federated States of",
    "1S": "Moldova, Republic of",
    "O9": "Monaco",
    "P0": "Mongolia",
    "Z5": "Montenegro",
    "P1": "Montserrat",
    "P2": "Morocco",
    "P3": "Mozambique",
    "E1": "Myanmar",
    "T6": "Namibia",
    "P5": "Nauru",
    "P6": "Nepal",
    "P7": "Netherlands",
    "P8": "Netherlands Antilles",
    "1W": "New Caledonia",
    "Q2": "New Zealand",
    "Q3": "Nicaragua",
    "Q4": "Niger",
    "Q5": "Nigeria",
    "Q6": "Niue",
    "Q7": "Norfolk Island",
    "1V": "Northern Mariana Islands",
    "Q8": "Norway",
    "P4": "Oman",
    "R0": "Pakistan",
    "1Y": "Palau",
    "1X": "Palestinian Territory, Occupied",
    "R1": "Panama",
    "R2": "Papua New Guinea",
    "R4": "Paraguay",
    "R5": "Peru",
    "R6": "Philippines",
    "R8": "Pitcairn",
    "R9": "Poland",
    "S1": "Portugal",
    "PR": "Puerto Rico",
    "S3": "Qatar",
    "S4": "Reunion",
    "S5": "Romania",
    "1Z": "Russian Federation",
    "S6": "Rwanda",
    "Z0": "Saint Barthelemy",
    "U8": "Saint Helena",
    "U7": "Saint Kitts and Nevis",
    "U9": "Saint Lucia",
    "Z1": "Saint Martin",
    "V0": "Saint Pierre and Miquelon",
    "V1": "Saint Vincent and the Grenadines",
    "Y0": "Samoa",
    "S8": "San Marino",
    "S9": "Sao Tome and Principe",
    "T0": "Saudi Arabia",
    "T1": "Senegal",
    "Z2": "Serbia",
    "T2": "Seychelles",
    "T8": "Sierra Leone",
    "U0": "Singapore",
    "2B": "Slovakia",
    "2A": "Slovenia",
    "D7": "Solomon Islands",
    "U1": "Somalia",
    "T3": "South Africa",
    "1L": "South Georgia and the South Sandwich Islands",
    "U3": "Spain",
    "F1": "Sri Lanka",
    "V2": "Sudan",
    "V3": "Suriname",
    "L9": "Svalbard and Jan Mayen",
    "V6": "Swaziland",
    "V7": "Sweden",
    "V8": "Switzerland",
    "V9": "Syrian Arab Republic",
    "F5": "Taiwan, Province of China",
    "2D": "Tajikistan",
    "W0": "Tanzania, United Republic of",
    "W1": "Thailand",
    "Z3": "Timor-leste",
    "W2": "Togo",
    "W3": "Tokelau",
    "W4": "Tonga",
    "W5": "Trinidad and Tobago",
    "W6": "Tunisia",
    "W8": "Turkey",
    "2E": "Turkmenistan",
    "W7": "Turks and Caicos Islands",
    "2G": "Tuvalu",
    "W9": "Uganda",
    "2H": "Ukraine",
    "C0": "United Arab Emirates",
    "X0": "United Kingdom",
    "2J": "United States Minor Outlying Islands",
    "X3": "Uruguay",
    "2K": "Uzbekistan",
    "2L": "Vanuatu",
    "X5": "Venezuela",
    "Q1": "Viet Nam",
    "D8": "Virgin Islands, British",
    "VI": "Virgin Islands, U.s.",
    "X8": "Wallis and Futuna",
    "U5": "Western Sahara",
    "T7": "Yemen",
    "Y4": "Zambia",
    "Y5": "Zimbabwe",
    "XX": "Unknown",
}

TEXT_SEARCH_FORM_MAPPING = {
    "4": {
        "description": "Statement of changes in beneficial ownership of securities",
        "title": "Insider trading report",
    },
    "8-K": {"description": "Current report", "title": "Current report"},
    "SC 13G": {
        "description": "Schedule filed to report acquisition of beneficial ownership of 5% or more of a class of equity securities by passive investors and certain institutions",
        "title": "Beneficial ownership report",
    },
    "D": {
        "description": "Notice of sales of securities on Form D (Regulation D)",
        "title": "Notice of sales of unregistered securities",
    },
    "3": {
        "description": "Initial statement of beneficial ownership of securities",
        "title": "Initial insider holdings report",
    },
    "10-Q": {
        "description": "Quarterly report pursuant to Section 13 or 15(d)",
        "title": "Quarterly report",
    },
    "424B2": {"description": "", "title": "Prospectus"},
    "6-K": {
        "description": "Current report of foreign issuer pursuant to Rules 13a-16 and 15d-16",
        "title": "Current report",
    },
    "497": {
        "description": "Definitive materials filed under paragraph (a), (b), (c), (d), (e) or (f) of Securities Act Rule 497",
        "title": "Prospectus",
    },
    "497K": {
        "description": "Summary prospectuses for open-end management investment companies registered on Form N-1A filed pursuant to Securities Act Rule 497(k)",
        "title": "Summary prospectus",
    },
    "13F-HR": {
        "description": "Further understand that each of 13F-HR, 13F-NT, and amendments thereto are mandatory electronic filings (hardship exemption exists to submit in paper; never used to the knowledge of IM staff);",
        "title": "Institutional investment manager holdings report",
    },
    "CORRESP": {"description": "", "title": "Correspondence"},
    "424B3": {"description": "", "title": "Prospectus"},
    "UPLOAD": {"description": "Upload Submission", "title": "Correspondence"},
    "SC 13D": {
        "description": "Schedule filed to report acquisition of beneficial ownership of 5% or more of a class of equity securities",
        "title": "Beneficial ownership report",
    },
    "FWP": {
        "description": "Filing under Securities Act Rule 163/433 of free writing prospectuses.",
        "title": "Prospectus",
    },
    "10-K": {
        "description": "Annual report pursuant to Section 13 or 15(d)",
        "title": "Annual report",
    },
    "EFFECT": {
        "description": "Effectiveness filing by commission order",
        "title": "SEC order",
    },
    "S-4": {
        "description": "Registration statement for securities to be issued in business combination transactions",
        "title": "Registration statement - business combination",
    },
    "485BPOS": {
        "description": "Post-effective amendment filed pursuant to Securities Act Rule 485(b) (this filing cannot be submitted as a 1940 Act only filing)",
        "title": "Prospectus materials",
    },
    "5": {
        "description": "Annual statement of changes in beneficial ownership of securities",
        "title": "Annual insider trading report",
    },
    "24F-2NT": {
        "description": "Rule 24f-2 notice filed on Form 24F-2",
        "title": "Annual notice of securities sold",
    },
    "N-Q": {
        "description": "Quarterly Schedule of Portfolio Holdings of Registered Management Investment Company filed on Form N-Q",
        "title": "Quarterly portolio holdings schedule",
    },
    "424B5": {"description": "", "title": "Prospectus"},
    "DEF 14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy statement",
    },
    "13F-NT": {
        "description": "Further understand that each of 13F-HR, 13F-NT, and amendments thereto are mandatory electronic filings (hardship exemption exists to submit in paper; never used to the knowledge of IM staff);",
        "title": "Institutional investment manager notice",
    },
    "497J": {
        "description": "Certification of no change in definitive materials under paragraph (j) of Securities Act Rule 497",
        "title": "Prospectus materials",
    },
    "10-D": {
        "description": "Asset-Backed Issuer Distribution Report Pursuant to Section 13 or 15(d) of the Securities Exchange Act of 1934",
        "title": "Distribution report",
    },
    "DEFA14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy materials",
    },
    "425": {
        "description": "Filing under Securities Act Rule 425 of certain prospectuses and communications in connection with business combination transactions.",
        "title": "Prospectus/communication re business combination",
    },
    "X-17A-5": {
        "description": "Annual audit report by brokers or dealers. To provide the Commission with audited statements of financial condition, income, and cash flows, and other financial materials.",
        "title": "",
    },
    "N-MFP": {
        "description": "Monthly Schedule of Portfolio Holdings of Money Market Funds on Form N-MFP",
        "title": "Monthly portfolio holdings schedule",
    },
    "S-1": {
        "description": "General form of registration statement for all companies including face-amount certificate companies",
        "title": "Registration statement",
    },
    "40-17G": {
        "description": "Fidelity bond filed pursuant to Rule 17g-1(g)(1) of the Investment Company Act of 1940.",
        "title": "",
    },
    "N-CSR": {
        "description": "Certified annual shareholder report of registered management investment companies filed on Form N-CSR",
        "title": "Annual shareholder report",
    },
    "N-CSRS": {
        "description": "Certified semi-annual shareholder report of registered management investment companies filed on Form N-CSR",
        "title": "Semi-annual shareholder report",
    },
    "N-PX": {
        "description": "Annual Report of Proxy Voting Record of Registered Management Investment Companies filed on Form N-PX",
        "title": "Annual proxy voting report",
    },
    "NSAR-B": {
        "description": "Annual report for management companies filed on Form N-SAR",
        "title": "",
    },
    "NSAR-A": {
        "description": "Semi-annual report for management companies filed on Form N-SAR",
        "title": "",
    },
    "NT 10-Q": {"description": "", "title": "Late filing notice"},
    "S-3ASR": {
        "description": "Automatic shelf registration statement of securities of well-known seasoned issuers",
        "title": "Registration statement",
    },
    "40-APP": {
        "description": "Application for an order of exemptive or other relief filed under the Investment Company Act of 1940",
        "title": "",
    },
    "S-3": {
        "description": "Registration statement for specified transactions by certain issuers including face-amount certificate companies",
        "title": "Registration statement",
    },
    "S-8": {
        "description": "Initial registration statement for securities to be offered to employees pursuant to employee benefit plans",
        "title": "Registration statement",
    },
    "19B-4E": {"description": "", "title": ""},
    "POSASR": {
        "description": "Post-effective amendment to an automatic shelf registration statement of Form S-3ASR or Form F-3ASR",
        "title": "Post-effective amendment",
    },
    "S-8 POS": {
        "description": "Post-effective amendment to a S-8 registration statement",
        "title": "Post-effective amendment",
    },
    "S-6": {
        "description": "Initial registration statement filed on Form S-6 for unit investment trusts",
        "title": "",
    },
    "FOCUSN": {"description": "", "title": ""},
    "485BXT": {
        "description": "Post-effective amendment filed pursuant to Securities Act Rule 485(b)(1)(iii) to designate a new effective date for a post-effective amendment previously filed pursuant to Securities Act Rule 485(a) (this filing cannot be submitted as a 1940 Act only fili",
        "title": "",
    },
    "POS AM": {
        "description": "Post-effective amendment to a registration statement that is not immediately effective upon filing",
        "title": "Post-effective amendment",
    },
    "N-MFP2": {
        "description": "Monthly Schedule of Portfolio Holdings of Money Market Funds on Form N-MFP",
        "title": "Monthly portfolio holdings schedule",
    },
    "MA-I": {
        "description": "Information Regarding Natural Persons Who Engage in Municipal Advisory Activities",
        "title": "",
    },
    "11-K": {
        "description": "Annual reports of employee stock purchase, savings and similar plans pursuant to Section 15(d)",
        "title": "Annual report",
    },
    "485APOS": {
        "description": "Post-effective amendment filed pursuant to Securities Act Rule 485(a) (this filing cannot be submitted as a 1940 Act only filing)",
        "title": "Prospectus materials",
    },
    "25-NSE": {"description": "", "title": ""},
    "NT 10-K": {"description": "", "title": "Late filing notice"},
    "CT ORDER": {"description": "", "title": "Confidential order"},
    "ARS": {
        "description": "Annual report to security holders. ",
        "title": "Annual report",
    },
    "SC TO-I": {
        "description": "Issuer tender offer statement",
        "title": "Tender offer statement",
    },
    "ABS-15G": {"description": "Asset-Backed Securitizer Report", "title": ""},
    "PRE 14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy statement (preliminary)",
    },
    "SC TO-T": {
        "description": "Third party tender offer statement",
        "title": "Tender offer statement",
    },
    "DFAN14A": {
        "description": "Definitive additional proxy soliciting materials filed by non-management including Rule 14(a)(12) material.",
        "title": "Proxy soliciting materials",
    },
    "487": {
        "description": "Pre-effective pricing amendments filed pursuant to Securities Act Rule 487",
        "title": "",
    },
    "8-A12B": {"description": "", "title": "Registration statement"},
    "20-F": {
        "description": "Registration statement under Section 12 of the Securities Exchange Act of 1934 or an annual or transition report filed under Section 13(a) or 15(d) of the Exchange Act for a  foreign private issuer.",
        "title": "Annual report - foreign issuer",
    },
    "F-6EF": {
        "description": "Auto effective registration statement for American Depositary Receipts representing securities of certain foreign private issuers",
        "title": "Registration statement",
    },
    "40-17F2": {
        "description": "Initial certificate of accounting of securities and similar investments in the custody of management investment companies filed pursuant to Rule 17f-2 of the Investment Company Act of 1940 filed on Form N-17F-2",
        "title": "",
    },
    "SD": {
        "description": "Specialized Disclosure Report",
        "title": "Specialized disclosure",
    },
    "144": {
        "description": "Filing for proposed sale of securities under Rule 144.",
        "title": "Sale of securities",
    },
    "NSAR-U": {
        "description": "Annual report for unit investment trusts filed on Form N-SAR",
        "title": "",
    },
    "ABS-EE": {
        "description": "Form for Submission of Electronic Exhibits in Asset-Backed Securities Offerings",
        "title": "",
    },
    "DEF 14C": {
        "description": "Information Statement Pursuant to Section 14(c) of the Securities Exchange Act of 1934",
        "title": "Information statement",
    },
    "15-15D": {"description": "", "title": "Suspension notice"},
    "SC 14D9": {
        "description": "Tender offer solicitation / recommendation statements filed under Rule 14-d9",
        "title": "Recommendation statement",
    },
    "RW": {"description": "Registration Withdrawal Request", "title": "Withdrawal"},
    "F-3": {
        "description": "Registration statement for specified transactions by certain foreign private issuers",
        "title": "Registration statement",
    },
    "F-4": {
        "description": "Registration statement for securities issued by foreign private issuers in certain business combination transactions",
        "title": "Registration statement",
    },
    "DRS": {"description": "", "title": "Draft registration statement"},
    "N-30B-2": {
        "description": "Periodic and interim reports mailed to investment company shareholders (other than annual and semi-annual reports mailed to shareholders pursuant to Rule 30e-1)",
        "title": "Shareholder reports",
    },
    "T-3": {
        "description": "Initial application for qualification of trust indentures",
        "title": "",
    },
    "REVOKED": {"description": "", "title": ""},
    "N-30D": {
        "description": "Initial annual and semi-annual reports mailed to investment company shareholders pursuant to Rule 30e-1 (other than those required to be submitted as part of Form N-CSR)",
        "title": "",
    },
    "N-2": {
        "description": "Filing of a registration statement on Form N-2 for closed-end investment companies",
        "title": "",
    },
    "PRE 14C": {
        "description": "Information Statement Pursuant to Section 14(c) of the Securities Exchange Act of 1934",
        "title": "Information statement (preliminary)",
    },
    "424B4": {"description": "", "title": "Prospectus"},
    "15-12G": {"description": "", "title": "Termination notice"},
    "NO ACT": {"description": "", "title": ""},
    "TA-2": {
        "description": "Annual report of transfer agent activities filed pursuant to the Securities Exchange Act of 1934. IN contains information necessary to monitor transfer agent registration",
        "title": "",
    },
    "N-CEN": {
        "description": "Form N-CEN will require annual reporting of certain census-type information in a structured XML format. Form N-CEN will replace Form N-SAR.  The compliance date for Form N-CEN filers – regardless of asset size – is June 1, 2018.",
        "title": "Annual report",
    },
    "N-MFP1": {
        "description": "Monthly Schedule of Portfolio Holdings of Money Market Funds on Form N-MFP",
        "title": "Monthly portfolio holdings schedule",
    },
    "SUPPL": {
        "description": "Voluntary supplemental material filed pursuant to Section 11(a) of the Securities Act of 1933 by foreign issuers",
        "title": "",
    },
    "C": {"description": "Offering Statement", "title": "Offering statement"},
    "SC TO-C": {
        "description": "Written communication relating to an issuer or third party tender offer",
        "title": "Tender offer communication",
    },
    "10-12G": {"description": "", "title": "Registration statement"},
    "POS EX": {
        "description": "Post-effective amendment filed solely to add exhibits to a registration statement",
        "title": "",
    },
    "F-6 POS": {
        "description": "Post-effective amendment to a F-6EF registration",
        "title": "Post-effective amendment",
    },
    "SC 13E3": {
        "description": "Schedule filed to report going private transactions",
        "title": "Going private transaction",
    },
    "40-24B2": {
        "description": "Filing of sales literature pursuant to Rule 24b-2 under the Investment Company Act of 1940.",
        "title": "",
    },
    "CERTNYS": {"description": "", "title": ""},
    "F-1": {
        "description": "Registration statement for certain foreign private issuers",
        "title": "Registration statement",
    },
    "NPORT-EX": {
        "description": "Portfolio holdings exhibit",
        "title": "Quarterly portfolio holdings schedule",
    },
    "NPORT-P": {"description": "", "title": ""},
    "NT NPORT-P": {"description": "", "title": ""},
    "NPORT-NP": {"description": "", "title": ""},
    "IRANNOTICE": {
        "description": "Notice of Iran-related disclosure filed pursuant to Section 13(r)(3) of the Exchange Act",
        "title": "",
    },
    "PRER14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy statement (preliminary)",
    },
    "1-A": {
        "description": "REGULATION A OFFERING STATEMENT UNDER THE SECURITIES ACT OF 1933",
        "title": "Offering statement",
    },
    "15-12B": {"description": "", "title": "Termination notice"},
    "497AD": {
        "description": "Filing by certain investment companies of Securities Act Rule 482 advertising in accordance with Securities Act Rule 497 and the Note to Rule 482(c).  ",
        "title": "",
    },
    "N-8F": {
        "description": "Application for deregistration made on Form N-8F",
        "title": "",
    },
    "PX14A6G": {"description": "", "title": ""},
    "POS AMI": {
        "description": "Amendment (for filings made under the1940 Act only)",
        "title": "",
    },
    "CB": {
        "description": "Notification form filed in connection with certain tender offers, business combinations and rights offerings, in which the subject company is a foreign private issuer of which less than 10% of its securities are held by U.S. persons.",
        "title": "",
    },
    "N-14": {
        "description": "Initial registration statement filed on Form N-14 for open-end investment company, including those filed with automatic effectiveness under Rule 488 (business combinations).",
        "title": "",
    },
    "F-6": {
        "description": "Registration statement for American Depositary Receipts representing securities of certain foreign private issuers",
        "title": "Registration statement (foreign issuer)",
    },
    "DRSLTR": {
        "description": "Correspondence Submission of a DRS filer. Correspondence is not publicly disseminated immediately. The SEC staff may publicly release all or portions of these documents.",
        "title": "",
    },
    "305B2": {
        "description": "Application for designation of a new trustee under the Trust Indenture Act",
        "title": "",
    },
    "CERTNAS": {"description": "", "title": ""},
    "424B7": {"description": "", "title": "Prospectus"},
    "DEFM14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy statement (business combination)",
    },
    "MA": {
        "description": "Application For Municipal Advisor Registration",
        "title": "",
    },
    "S-11": {
        "description": "Registration statement for securities to be issued by real estate companies",
        "title": "Registration statement",
    },
    "AW": {
        "description": "Withdrawal of amendment to a registration statement filed under the Securities Act",
        "title": "Withdrawal",
    },
    "TA-1": {
        "description": "Application for registration as a transfer agent filed pursuant to the Securities Exchange Act of 1934. It contains information necessary to consider the Transfer Agent registration",
        "title": "",
    },
    "F-X": {
        "description": "For appointment of agent for service of process by issuers registering securities (if filed on Form F-8, F-9, F-10 or F-80, or registering securities or filing periodic reports on Form 40-F, or by any person filing certain tender offer documents, or by an",
        "title": "",
    },
    "8-A12G": {"description": "", "title": "Registration statement"},
    "DEFR14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy statement",
    },
    "18-K": {
        "description": "Annual report for foreign governments and political subdivisions",
        "title": "Annual report",
    },
    "N-8F ORDR": {"description": "N-8F Order", "title": ""},
    "40-F": {
        "description": "Registration Statement Pursuant to Section 12 of the Securities Exchange Act of 1934 or Annual Report pursuant to Section 13(a) or 15(d) of the Securities Exchange Act of 1934",
        "title": "Registration statement",
    },
    "MA-A": {
        "description": "Annual Update of Municipal Advisor Registration",
        "title": "",
    },
    "PREC14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy statement (preliminary)",
    },
    "N-8F NTC": {"description": "N-8F Notice", "title": ""},
    "POS 8C": {
        "description": "Post-effective amendment filed under the 1933 Act only or under both the 1933 and 1940 Acts pursuant to Section 8(c) of the 1933 Act by closed-end investment companies (this filing cannot be submitted as a 1940 Act only filing)",
        "title": "",
    },
    "PREM14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy statement (preliminary)",
    },
    "PRRN14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy statement (preliminary)",
    },
    "N-4": {
        "description": "Initial registration statement on Form N-4 for separate accounts (unit investment trusts)",
        "title": "",
    },
    "N-8A": {
        "description": "Initial notification of registration under section 8(a) filed on Form N-8A",
        "title": "",
    },
    "424H": {"description": "", "title": ""},
    "N-1A": {
        "description": "Initial registration statement including amendments for open-end management investment companies",
        "title": "",
    },
    "CERT": {"description": "", "title": ""},
    "F-3ASR": {
        "description": "Automatic shelf registration statement of securities of well-known seasoned issuers",
        "title": "Registration statement",
    },
    "1": {"description": "", "title": ""},
    "DEFC14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy statement",
    },
    "424B1": {"description": "", "title": "Prospectus"},
    "10-12B": {"description": "", "title": "Registration statement"},
    "SC14D9C": {
        "description": "Written communication by the subject company relating to a third party tender offer",
        "title": "Tender offer communication",
    },
    "F-10": {
        "description": "Registration statement for securities of certain Canadian issuers under the Securities Act of 1933",
        "title": "Registration statement",
    },
    "APP NTC": {"description": "40-APP Notice", "title": ""},
    "N-23C3A": {"description": "", "title": ""},
    "40-OIP": {
        "description": "Application for an order of exemptive or other relief filed under the Investment Company Act of 1940",
        "title": "",
    },
    "25": {
        "description": "Notification of removal from listing and/or registration from a national securities exchange",
        "title": "Notice of listing removal",
    },
    "APP ORDR": {"description": "40-APP Order", "title": ""},
    "APP WD": {
        "description": "Withdrawal of an application for exemptive or other relief from the federal securities laws",
        "title": "",
    },
    "PRER14C": {
        "description": "Information Statement Pursuant to Section 14(c) of the Securities Exchange Act of 1934",
        "title": "Proxy statement (preliminary)",
    },
    "424B8": {"description": "", "title": "Prospectus"},
    "253G2": {"description": "", "title": ""},
    "1-U": {
        "description": "Current Report Pursuant to Regulation A",
        "title": "Current report",
    },
    "SC 14F1": {
        "description": "Statement regarding change in majority of directors pursuant to Rule 14f-1",
        "title": "Change in board majority",
    },
    "C-U": {"description": "Progress Update", "title": "Progess update"},
    "N-23C-2": {
        "description": "Notice by closed-end investment companies of intention to call or redeem their own securities under Investment Company Act Rule 23c-2",
        "title": "",
    },
    "S-1MEF": {
        "description": "A new registration statement filed under Rule 462(b) to add securities to a prior related effective registration statement filed on Form S-1",
        "title": "Registration statement",
    },
    "NT 20-F": {"description": "", "title": "Late filing notice"},
    "QUALIF": {"description": "", "title": "Qualification"},
    "C-AR": {"description": "Annual Report", "title": "Annual report"},
    "DEL AM": {
        "description": "Separately filed delaying amendment under Securities Act Rule 473 to delay effectiveness of a 1933 Act registration statement",
        "title": "Delaying amendment",
    },
    "1-A POS": {"description": "", "title": "Post-qualification amendment"},
    "NTN 10Q": {"description": "", "title": ""},
    "ADV-NR": {"description": "", "title": ""},
    "SF-3": {
        "description": "Shelf registration statement for qualified offerings of asset-backed securities",
        "title": "Registration statement",
    },
    "486BPOS": {
        "description": "Post-effective amendment to filing filed pursuant to Securities Act Rule 486(b)",
        "title": "",
    },
    "40-6B": {
        "description": "Application under the Investment Company Act of 1940 by an employees securities company",
        "title": "",
    },
    "CERTARCA": {"description": "", "title": ""},
    "10-KT": {"description": "", "title": "Transition report"},
    "NTN 10K": {"description": "", "title": ""},
    "DSTRBRPT": {
        "description": "Distribution of primary obligations Development Bank report",
        "title": "",
    },
    "40-17F1": {
        "description": "Initial certificate of accounting of securities and similar investments in the custody of management investment companies filed pursuant to Rule 17f-1 of the Investment Company Act of 1940 filed on Form N-17F-1",
        "title": "",
    },
    "N-14 8C": {
        "description": "Initial registration statement filed on Form N-14 by closed-end investment company (business combinations)",
        "title": "",
    },
    "ADV-E": {"description": "", "title": ""},
    "S-3MEF": {
        "description": "A new registration statement filed under Rule 462(b) to add securities to a prior related effective registration statement filed on Form S-3",
        "title": "Registration statement",
    },
    "40-33": {
        "description": "Copies of all stockholder derivative actions filed with a court against an investment company or an affiliate thereof pursuant to Section 33 of the Investment Company Act of 1940. ",
        "title": "",
    },
    "N-18F1": {
        "description": "Initial notification of election pursuant to Rule 18f-1 filed on Form N-18F-1 [under the Investment Company Act of 1940 by a registered open-end investment company].",
        "title": "",
    },
    "N-6": {
        "description": "Initial registration statement filed on Form N-6 for separate accounts (unit investment trusts)",
        "title": "",
    },
    "SE": {"description": "", "title": ""},
    "S-B": {
        "description": "Registration statement for securities of foreign governments and subdivisions thereof under the Securities Act of 1933 (Schedule b)",
        "title": "Registration statement",
    },
    "MA-W": {
        "description": "Notice of Withdrawal From Registration as a Municipal Advisor",
        "title": "",
    },
    "F-N": {
        "description": "Notification of the appointment of an agent for service by certain foreign institutions.",
        "title": "",
    },
    "DOS": {"description": "Persons who", "title": ""},
    "1-K": {"description": "Regulation A Annual Report", "title": "Annual report"},
    "1-SA": {
        "description": "SEMIANNUAL REPORT PURSUANT TO REGULATION A or SPECIAL FINANCIAL REPORT PURSUANT TO REGULATION A",
        "title": "Semiannual report",
    },
    "CFPORTAL": {
        "description": "It contains information to consider registration as a crowdfunding portal",
        "title": "",
    },
    "NT N-MFP": {
        "description": "EDGAR generated form type for late filing of  Monthly Schedule of Portfolio Holdings of Money Market Funds on Form N-MFP",
        "title": "",
    },
    "S-3D": {
        "description": "Automatically effective registration statement for securities issued pursuant to dividend or interest reinvestment plans",
        "title": "Registration statement",
    },
    "S-3DPOS": {
        "description": "Post-effective amendment to a S-3D registration statement",
        "title": "Post-effective amendment",
    },
    "MSD": {"description": "", "title": ""},
    "13FCONP": {"description": "", "title": ""},
    "NT 11-K": {"description": "", "title": "Late filing notice"},
    "20FR12G": {"description": "", "title": ""},
    "8-K12B": {"description": "", "title": ""},
    "NSAR-BT": {
        "description": "Transitional annual report filed on Form N-SAR",
        "title": "",
    },
    "TA-W": {
        "description": "Notice of withdrawal from registration as transfer agent filed pursuant to the Securities Exchange Act of 1934. IN contains information necessary to consider the Transfer Agent registration withdrawal",
        "title": "",
    },
    "RW WD": {
        "description": "Withdrawal of a request for withdrawal of a registration statement",
        "title": "Withdrawal",
    },
    "NT-NSAR": {
        "description": "Notice under Exchange Act Rule 12b-25 of inability to timely file Form N-SAR",
        "title": "",
    },
    "PREM14C": {
        "description": "Information Statement Pursuant to Section 14(c) of the Securities Exchange Act of 1934",
        "title": "Information statement (preliminary)",
    },
    "PREN14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy statement (preliminary)",
    },
    "OIP NTC": {"description": "40-OIP Notice", "title": ""},
    "DEFA14C": {
        "description": "Information Statement Pursuant to Section 14(c) of the Securities Exchange Act of 1934",
        "title": "Information statement materials",
    },
    "DFRN14A": {
        "description": "Revised definitive proxy statement filed by non-management",
        "title": "Proxy statement",
    },
    "N-6F": {
        "description": "Notice of intent by business development companies to elect to be subject to Sections 55 through 65 of the 1940 Act filed on Form N-6F",
        "title": "",
    },
    "OIP ORDR": {"description": "40-OIP Order", "title": ""},
    "C-W": {"description": "Offering Statement Withdrawal", "title": "Withdrawal"},
    "CERTPAC": {"description": "", "title": ""},
    "8-K12G3": {"description": "", "title": ""},
    "SC14D1F": {
        "description": "Third party tender offer statement filed pursuant to Rule 14d-1(b) by foreign issuers",
        "title": "Tender offer statement",
    },
    "DEFN14A": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Proxy statement",
    },
    "DEFM14C": {
        "description": "Information Statement Pursuant to Section 14(c) of the Securities Exchange Act of 1934",
        "title": "Information statement",
    },
    "1-A-W": {"description": "", "title": "Withdrawal"},
    "DEFR14C": {
        "description": "Information Statement Pursuant to Section 14(c) of the Securities Exchange Act of 1934",
        "title": "Information statement",
    },
    "G-FIN": {"description": "", "title": ""},
    "NRSRO-UPD": {
        "description": "Form NRSRO – Update of Registration for Nationally Recognized Statistical Rating Organizations",
        "title": "",
    },
    "NT-NCSR": {
        "description": "Notice under Exchange Act Rule 12b-25 of inability to timely file Form N-CSR (annual or semi-annual report)",
        "title": "",
    },
    "15F-12G": {"description": "", "title": "Termination notice"},
    "20FR12B": {"description": "", "title": "Registration statement"},
    "SEC STAFF ACTION": {"description": "", "title": ""},
    "DOSLTR": {"description": "", "title": ""},
    "40FR12B": {
        "description": "Registration of a class of securities of certain Canadian issuers pursuant to Section 12(b) of the 1934 Act",
        "title": "Registration statement",
    },
    "F-1MEF": {
        "description": "A new registration statement filed under Rule 462(b) to add securities to a prior related effective registration statement filed on Form F-1",
        "title": "Registration statement",
    },
    "N-54A": {
        "description": "Notification of election by business development companies to be subject to the provisions of sections 55 through 65 of the Investment Company Act",
        "title": "",
    },
    "15F-15D": {"description": "", "title": "Suspension notice"},
    "NT N-CEN": {"description": "", "title": ""},
    "15F-12B": {"description": "", "title": "Termination notice"},
    "486APOS": {
        "description": "Post-effective amendment to filing filed pursuant to Securities Act Rule 486(a)",
        "title": "",
    },
    "F-9": {
        "description": "Registration of securities of certain investment grade debt or investment grade preferred securities of certain Canadian issuers under the Securities Act of 1933",
        "title": "",
    },
    "QRTLYRPT": {
        "description": "Periodic Development Bank filing, submitted quarterly",
        "title": "",
    },
    "40-8B25": {
        "description": "Filing by investment company of application under Investment Company Act Rule 8b-25(a) requesting extension of time for filing certain information, document or report",
        "title": "",
    },
    "NT N-MFP2": {"description": "", "title": ""},
    "1-Z": {"description": "Exit Report Under Regulation A", "title": "Exit report"},
    "N-2MEF": {
        "description": "A new registration statement on Form N-2 filed under the Securities Act Rule 462(b) by closed-end investment companies to register up to an additional 20% of securities for an offering that was registered on Form N-2",
        "title": "",
    },
    "TACO": {"description": "", "title": ""},
    "CERTCBO": {"description": "", "title": ""},
    "10-QT": {"description": "", "title": "Transition report"},
    "CERTBATS": {"description": "", "title": ""},
    "S-4 POS": {
        "description": "Post-effective amendment to a S-4EF registration statement",
        "title": "Post-effective amendment",
    },
    "N-23C3B": {
        "description": "Notification of  discretionary repurchase offer [by registered closed-end investment companies or business development companies] pursuant Rule 23c-3(c) only",
        "title": "",
    },
    "40-206A": {"description": "", "title": ""},
    "NRSRO-CE": {
        "description": "Form NRSRO – Annual Certification for Nationally Recognized Statistical Rating Organizations",
        "title": "",
    },
    "APP WDG": {"description": "", "title": ""},
    "STOP ORDER": {"description": "", "title": ""},
    "424A": {"description": "", "title": "Prospectus"},
    "ANNLRPT": {
        "description": "Periodic Development Bank filing, submitted annually",
        "title": "",
    },
    "N-CR": {
        "description": "Current Report of Money Market Fund Material Events",
        "title": "",
    },
    "PX14A6N": {"description": "", "title": ""},
    "SEC STAFF LETTER": {"description": "", "title": ""},
    "N-54C": {
        "description": "Notification of withdrawal by business development companies of notification of election by business development companies to be subject to the provisions of sections 55 through 65 of the Investment Company Act",
        "title": "",
    },
    "NT-NCEN": {"description": "", "title": ""},
    "POS462B": {
        "description": "Post-effective amendment to Securities Act Rule 462(b) registration statement",
        "title": "Post-effective amendment",
    },
    "C-TR": {"description": "Termination of Reporting", "title": "Termination"},
    "2-A": {"description": "", "title": ""},
    "S-4MEF": {
        "description": "A new registration statement filed under Rule 462(b) to add securities to a prior related effective registration statement filed on Form S-4",
        "title": "Registration statement",
    },
    "ADV-H-T": {"description": "", "title": ""},
    "F-3D": {
        "description": "Registration statement for dividend or interest reinvestment plan securities of foreign private issuers",
        "title": "Registration statement",
    },
    "AW WD": {
        "description": "Withdrawal of a request for withdrawal of an amendment to a registration statement",
        "title": "Withdrawal",
    },
    "6B NTC": {"description": "40-6B Notice", "title": ""},
    "8-M": {"description": "", "title": ""},
    "NT N-MFP1": {"description": "", "title": ""},
    "N-8B-2": {
        "description": "Initial registration statement for unit investment trusts filed on Form N-8B-2",
        "title": "",
    },
    "REG-NR": {"description": "", "title": ""},
    "497H2": {
        "description": "Filings made pursuant to Securities Act Rule 497(h)(2)",
        "title": "",
    },
    "F-7": {
        "description": "Registration statement for securities of certain Canadian issuers offered for cash upon the exercise of rights granted to existing security holders under the Securities Act of 1933",
        "title": "Registration statement",
    },
    "S-11MEF": {
        "description": "A new registration statement filed under Rule 462(b) to add securities to a prior related effective registration statement filed on Form S-11",
        "title": "Registration statement",
    },
    "253G1": {"description": "", "title": "Disclosure"},
    "6B ORDR": {"description": "40-6B Order", "title": ""},
    "F-80": {
        "description": "Registration of securities of certain Canadian issuers to be issued in exchange offers or a business combination under the Securities Act of 1933",
        "title": "Registration statement",
    },
    "40-202A": {"description": "", "title": ""},
    "SC 14N": {
        "description": "Information to be included in statements filed pursuant to §240.14n-1 and amendments thereto filed pursuant to §240.14n-2.",
        "title": "",
    },
    "F-10POS": {
        "description": "Post-effective amendment to a F-10EF registration",
        "title": "Post-effective amendment",
    },
    "MSDW": {"description": "", "title": ""},
    "NSAR-AT": {
        "description": "Transitional semi-annual report filed on Form N-SAR",
        "title": "",
    },
    "SC14D9F": {
        "description": "Solicitation/recommendation statement pursuant to Section 14(d)(4) of the Securities Exchange Act of 1934 and Rules 14d-1(b) and 14e-2(c) by foreign issuers",
        "title": "Recommendation statement",
    },
    "486BXT": {"description": "", "title": ""},
    "F-8": {
        "description": "Registration statement for securities of certain Canadian issuers to be issued in exchange offers or a business combination under the Securities Act of 1933",
        "title": "Registration statement",
    },
    "PREC14C": {
        "description": "Proxy Statement Pursuant to Section 14(a) of the Securities Exchange Act of 1934",
        "title": "Information statement (preliminary)",
    },
    "MSDCO": {"description": "", "title": ""},
    "TTW": {"description": "", "title": ""},
    "WDL-REQ": {"description": "", "title": ""},
    "G-405": {"description": "", "title": ""},
    "NTFNCSR": {"description": "", "title": ""},
    "SF-1": {
        "description": "General form of registration statement for all issuers of asset-backed securities",
        "title": "Registration statement",
    },
    "G-405N": {"description": "", "title": ""},
    "F-80POS": {
        "description": "Post-effective amendment to a F-80 registration",
        "title": "Post-effective amendment",
    },
    "F-3MEF": {
        "description": "A new registration statement filed under Rule 462(b) to add securities to a prior related effective registration statement filed on Form F-3",
        "title": "Registration statement",
    },
    "SP 15D2": {
        "description": "Special Financial Report filed under Rule 15d-2",
        "title": "Special financial report",
    },
    "11-KT": {"description": "", "title": "Transition report"},
    "40-17GCS": {
        "description": "Filings of claim or settlement pursuant to rule 17g-1(g)(1)(2) or (3) of the Investment Company Act of 1940.",
        "title": "",
    },
    "40FR12G": {
        "description": "Registration of a class of securities of certain Canadian issuers pursuant to Section 12(g) of the 1934 Act",
        "title": "Registration statement",
    },
    "F-3DPOS": {
        "description": "Post-Effective amendment to a F-3D registration",
        "title": "Post-effective amendment",
    },
    "F-4 POS": {
        "description": "Post-Effective amendment to an F-4EF registration",
        "title": "Post-effective amendment",
    },
    "NTFNSAR": {"description": "", "title": ""},
    "1-E": {
        "description": "Notification under Regulation E by small business investment companies and business development companies",
        "title": "",
    },
    "40-8F-2": {
        "description": "Initial application for deregistration pursuant to Investment Company Act Rule 0-2",
        "title": "",
    },
    "8-K15D5": {"description": "", "title": ""},
    "G-FINW": {"description": "", "title": ""},
    "NTFNCEN": {"description": "", "title": ""},
    "2-AF": {"description": "", "title": ""},
    "N-23C3C": {
        "description": "Notification of periodic repurchase offer under paragraph (b) of Rule 23c-3 and a discretionary repurchase offer under paragraph (c) of Rule 23c-3. [by registered closed-end investment companies or business development companies] pursuant to Rule 23c-3(b)",
        "title": "",
    },
    "NTN 20F": {"description": "", "title": ""},
    "SC13E4F": {
        "description": "Issuer tender offer statement filed pursuant to Rule 13(e)(4) by foreign issuers",
        "title": "Tender offer statement",
    },
    "F-8 POS": {
        "description": "Post-effective amendment to a F-8 registration",
        "title": "Post-effective amendment",
    },
    "NT NPORT-EX": {"description": "", "title": ""},
    "TH": {"description": "", "title": ""},
    "ADN-MTL": {"description": "", "title": ""},
    "CFPORTAL-W": {"description": "", "title": ""},
    "DEFC14C": {
        "description": "Information Statement Pursuant to Section 14(c) of the Securities Exchange Act of 1934",
        "title": "Information statement",
    },
    "SC 13E1": {
        "description": "Schedule 13-E1 statement of issuer required by Rule 13e-1",
        "title": "Purchase of securities",
    },
    "SDR": {
        "description": "Swap Data Repository (in Edgar now). It contains information necessary to consider registration as a swap data repository",
        "title": "",
    },
    "2-E": {
        "description": "Report of sales of securities by small business investment companies and business development companies pursuant to Rule 609 (Regulation E) Securities Act of 1933",
        "title": "",
    },
    "9-M": {"description": "", "title": ""},
    "S-BMEF": {
        "description": "A new registration statement filed under Rule 462(b) to add securities to a prior related effective registration statement filed on Form S-B",
        "title": "Registration statement",
    },
    "253G3": {"description": "", "title": "Disclosure"},
    "34-12H": {"description": "", "title": ""},
    "F-7 POS": {
        "description": "Post-effective amendment to a F-7 registration",
        "title": "Post-effective amendment",
    },
    "N-5": {
        "description": "Initial registration statement on Form N-5 for small business investment companies",
        "title": "",
    },
    "POS462C": {
        "description": "Post-effective amendment to a registration statement filed under Securities Act Rule 462(c)",
        "title": "Post-effective amendment",
    },
    "8F-2 NTC": {"description": "40-8F-2 Notice", "title": ""},
    "ATS-N-C": {"description": "", "title": ""},
    "C-AR-W": {"description": "", "title": "Withdrawal"},
    "C-U-W": {"description": "Broker-Dealer Withdrawal", "title": "Withdrawal"},
    "F-10EF": {
        "description": "Auto effective registration statement for securities of certain Canadian issuers under the Securities Act of 1933",
        "title": "Registration statement",
    },
    "F-4MEF": {
        "description": "A new registration statement filed under Rule 462(b) to add securities to a prior related effective registration statement filed on Form F-4",
        "title": "Registration statement",
    },
    "F-9 POS": {
        "description": "Post-effective amendment to a F-9EF registration",
        "title": "",
    },
    "NT 10-D": {"description": "", "title": "Late filing notice"},
    "NTN 10D": {"description": "", "title": ""},
    "S-20": {
        "description": "Registration statement for standardized options",
        "title": "Registration statement",
    },
    "SL": {"description": "", "title": ""},
    "UNDER": {"description": "Initial undertaking to file reports", "title": ""},
    "1-E AD": {"description": "", "title": "Sales materials"},
    "1-Z-W": {"description": "", "title": "Withdrawal"},
    "18-12B": {"description": "", "title": "Registration statement"},
    "8F-2 ORDR": {"description": "40-8F-2 Order", "title": ""},
    "ADV-H-C": {"description": "", "title": ""},
    "N-14MEF": {
        "description": "A new registration statement filed on Form N-14 by closed end investment companies filed under Securities Act Rule 462(b) of up to an additional 20% of securities for an offering that was registered on Form N-14",
        "title": "",
    },
    "SEC ACTION": {"description": "", "title": ""},
    "253G4": {"description": "", "title": "Disclosure"},
    "40-203A": {"description": "", "title": ""},
    "ATS-N": {"description": "", "title": ""},
    "ATS-N/UA": {"description": "", "title": ""},
    "C-TR-W": {
        "description": "Termination of Reporting Withdrawal",
        "title": "Withdrawal",
    },
    "N-1": {
        "description": "Initial registration statement filed on Form N-1 for open-end management investment companies",
        "title": "",
    },
    "S-4EF": {
        "description": "Auto effective registration statement for securities issued in connection with the formation of a bank or savings and loan holding company in compliance with General Instruction G",
        "title": "Registration statement",
    },
    "SBSE": {
        "description": "Application for Registration of Security-based Swap Dealers and Major Security-based Swap Participants",
        "title": "SBSE Registration",
    },
    "SBSE-A": {
        "description": "Application for Registration of Security-based Swap Dealers and Major Security-based Swap Participants that are Registered or Registering with the Commodity Futures Trading Commission as a Swap Dealer or Major Swap Participant",
        "title": "SBSE Registration for Commodity Futures Trading Commission registrants",
    },
    "SBSE-BD": {
        "description": "Application for Registration of Security-based Swap Dealers and Major Security-based Swap Participants that are Registered Broker-dealers",
        "title": "SBSE Registration for Broker-Dealers",
    },
    "SBSE-C": {
        "description": "Certifications for Registration of Security-based Swap Dealers and Major Security-based Participants",
        "title": "SBSE Registration Certification",
    },
    "SBSE-W": {
        "description": "Request for Withdrawal from Registration as a Security-based Swap Dealer or Major Security-based Swap Participant",
        "title": "SBSE Registration Withdrawal",
    },
    "N-2ASR": {"description": "", "title": ""},
    "N-2 POSASR": {"description": "", "title": ""},
    "497VPI": {
        "description": "Initial summary prospectus for variable contracts filed pursuant to Securities Act Rule 497(k)",
        "title": "",
    },
    "497VPU": {
        "description": "Updating summary prospectus for variable contracts filed pursuant to Securities Act Rule 497(k)",
        "title": "",
    },
    "N-VP": {
        "description": "",
        "title": "Notice documents for certain variable contracts",
    },
    "N-VPFS": {
        "description": "",
        "title": "Financial statements for certain variable contracts",
    },
}

TEXT_SEARCH_CATEGORY_FORM_GROUPINGS = {
    #    "Exclude insider equity awards, transactions, and ownership (Section 16 Reports)": ["-3","-4","-5"], # todo: work out how to exclude these
    "All annual, quarterly, and current reports": [
        "1-K",
        "1-SA",
        "1-U",
        "1-Z",
        "1-Z-W",
        "10-D",
        "10-K",
        "10-KT",
        "10-Q",
        "10-QT",
        "11-K",
        "11-KT",
        "13F-HR",
        "13F-NT",
        "15-12B",
        "15-12G",
        "15-15D",
        "15F-12B",
        "15F-12G",
        "15F-15D",
        "18-K",
        "20-F",
        "24F-2NT",
        "25",
        "25-NSE",
        "40-17F2",
        "40-17G",
        "40-F",
        "6-K",
        "8-K",
        "8-K12G3",
        "8-K15D5",
        "ABS-15G",
        "ABS-EE",
        "ANNLRPT",
        "DSTRBRPT",
        "IRANNOTICE",
        "N-30B-2",
        "N-30D",
        "N-CEN",
        "N-CSR",
        "N-CSRS",
        "N-MFP",
        "N-MFP1",
        "N-MFP2",
        "N-PX",
        "N-Q",
        "NPORT-EX",
        "NSAR-A",
        "NSAR-B",
        "NSAR-U",
        "NT 10-D",
        "NT 10-K",
        "NT 10-Q",
        "NT 11-K",
        "NT 20-F",
        "QRTLYRPT",
        "SD",
        "SP 15D2",
    ],
    "Insider equity awards, transactions, and ownership (Section 16 Reports)": [
        "3",
        "4",
        "5",
    ],
    "Beneficial ownership reports": ["SC 13D", "SC 13G", "SC14D1F"],
    "Exempt offerings": [
        "1-A",
        "1-A POS",
        "1-A-W",
        "253G1",
        "253G2",
        "253G3",
        "253G4",
        "C",
        "D",
        "DOS",
    ],
    "Registration statements and prospectuses": [
        "10-12B",
        "10-12G",
        "18-12B",
        "20FR12B",
        "20FR12G",
        "40-24B2",
        "40FR12B",
        "40FR12G",
        "424A",
        "424B1",
        "424B2",
        "424B3",
        "424B4",
        "424B5",
        "424B7",
        "424B8",
        "424H",
        "425",
        "485APOS",
        "485BPOS",
        "485BXT",
        "487",
        "497",
        "497J",
        "497K",
        "8-A12B",
        "8-A12G",
        "AW",
        "AW WD",
        "DEL AM",
        "DRS",
        "F-1",
        "F-10",
        "F-10EF",
        "F-10POS",
        "F-3",
        "F-3ASR",
        "F-3D",
        "F-3DPOS",
        "F-3MEF",
        "F-4",
        "F-4 POS",
        "F-4MEF",
        "F-6",
        "F-6 POS",
        "F-6EF",
        "F-7",
        "F-7 POS",
        "F-8",
        "F-8 POS",
        "F-80",
        "F-80POS",
        "F-9",
        "F-9 POS",
        "F-N",
        "F-X",
        "FWP",
        "N-2",
        "POS AM",
        "POS EX",
        "POS462B",
        "POS462C",
        "POSASR",
        "RW",
        "RW WD",
        "S-1",
        "S-11",
        "S-11MEF",
        "S-1MEF",
        "S-20",
        "S-3",
        "S-3ASR",
        "S-3D",
        "S-3DPOS",
        "S-3MEF",
        "S-4",
        "S-4 POS",
        "S-4EF",
        "S-4MEF",
        "S-6",
        "S-8",
        "S-8 POS",
        "S-B",
        "S-BMEF",
        "SF-1",
        "SF-3",
        "SUPPL",
        "UNDER",
    ],
    "Filing review correspondence": ["CORRESP", "DOSLTR", "DRSLTR", "UPLOAD"],
    "SEC orders and notices": ["40-APP", "CT ORDER", "EFFECT", "QUALIF", "REVOKED"],
    "Proxy materials": [
        "ARS",
        "DEF 14A",
        "DEF 14C",
        "DEFA14A",
        "DEFA14C",
        "DEFC14A",
        "DEFC14C",
        "DEFM14A",
        "DEFM14C",
        "DEFN14A",
        "DEFR14A",
        "DEFR14C",
        "DFAN14A",
        "DFRN14A",
        "PRE 14A",
        "PRE 14C",
        "PREC14A",
        "PREC14C",
        "PREM14A",
        "PREM14C",
        "PREN14A",
        "PRER14A",
        "PRER14C",
        "PRRN14A",
        "PX14A6G",
        "PX14A6N",
        "SC 14N",
    ],
    "Tender offers and going private transactions": [
        "CB",
        "SC 13E1",
        "SC 13E3",
        "SC 14D9",
        "SC 14F1",
        "SC TO-C",
        "SC TO-I",
        "SC TO-T",
        "SC13E4F",
        "SC14D9C",
        "SC14D9F",
    ],
    "Trust indenture filings": ["305B2", "T-3"],
}
# These are the verbose descriptions of the categories that are used in the CLI,
TEXT_SEARCH_FILING_VS_MAPPING_CATEGORIES_MAPPING = {
    "all_annual_quarterly_and_current_reports": "All annual, quarterly, and current reports",
    "all_section_16": "Insider equity awards, transactions, and ownership (Section 16 Reports)",
    "beneficial_ownership_reports": "Beneficial ownership reports",
    "exempt_offerings": "Exempt offerings",
    "registration_statements": "Registration statements and prospectuses",
    "filing_review_correspondence": "Filing review correspondence",
    "sec_orders_and_notices": "SEC orders and notices",
    "proxy_materials": "Proxy materials",
    "tender_offers_and_going_private_tx": "Tender offers and going private transactions",
    "trust_indentures": "Trust indenture filings",
}

FilingCategoryLiteral = Literal[
    "View all",
    "Custom",
    "Exclude insider equity awards, transactions, and ownership (Section 16 Reports)",
    "All annual, quarterly, and current reports",
    "Insider equity awards, transactions, and ownership (Section 16 Reports)",
    "Beneficial Ownership Reports",
    "Exempt Offerings",
    "Registration statements and prospectuses",
    "Filing review correspondence",
    "SEC orders and notices",
    "Proxy materials",
    "Tender offers and going private transactions",
    "Trust indentures filings",
]

DateRangeLiteral = Literal["all", "10y", "5y", "1y", "30d", "custom"]

LocationLiteral = Literal[
    "AL",  # Alabama
    "AK",  # Alaska
    "AZ",  # Arizona
    "AR",  # Arkansas
    "CA",  # California
    "CO",  # Colorado
    "CT",  # Connecticut
    "DE",  # Delaware
    "DC",  # District of Columbia
    "FL",  # Florida
    "GA",  # Georgia
    "HI",  # Hawaii
    "ID",  # Idaho
    "IL",  # Illinois
    "IN",  # Indiana
    "IA",  # Iowa
    "KS",  # Kansas
    "KY",  # Kentucky
    "LA",  # Louisiana
    "ME",  # Maine
    "MD",  # Maryland
    "MA",  # Massachusetts
    "MI",  # Michigan
    "MN",  # Minnesota
    "MS",  # Mississippi
    "MO",  # Missouri
    "MT",  # Montana
    "NE",  # Nebraska
    "NV",  # Nevada
    "NH",  # New Hampshire
    "NJ",  # New Jersey
    "NM",  # New Mexico
    "NY",  # New York
    "NC",  # North Carolina
    "ND",  # North Dakota
    "OH",  # Ohio
    "OK",  # Oklahoma
    "OR",  # Oregon
    "PA",  # Pennsylvania
    "RI",  # Rhode Island
    "SC",  # South Carolina
    "SD",  # South Dakota
    "TN",  # Tennessee
    "TX",  # Texas
    "UT",  # Utah
    "VT",  # Vermont
    "VA",  # Virginia
    "WA",  # Washington
    "WV",  # West Virginia
    "WI",  # Wisconsin
    "WY",  # Wyoming
    "AB",  # Alberta
    "BC",  # British Columbia
    "CAN",  # Canada
    "MB",  # Manitoba
    "NB",  # New Brunswick
    "NL",  # Newfoundland and Labrador
    "NS",  # Nova Scotia
    "ON",  # Ontario
    "PE",  # Prince Edward Island
    "QC",  # Quebec
    "SK",  # Saskatchewan
    "YT",  # Yukon
    "AFG",  # Afghanistan
    "ALA",  # Åland Islands
    "ALB",  # Albania
    "DZA",  # Algeria
    "ASM",  # American Samoa
    "AND",  # Andorra
    "AGO",  # Angola
    "AIA",  # Anguilla
    "ATA",  # Antarctica
    "ATG",  # Antigua and Barbuda
    "ARG",  # Argentina
    "ARM",  # Armenia
    "ABW",  # Aruba
    "AUS",  # Australia
    "AUT",  # Austria
    "AZE",  # Azerbaijan
    "BHS",  # Bahamas
    "BHR",  # Bahrain
    "BGD",  # Bangladesh
    "BRB",  # Barbados
    "BLR",  # Belarus
    "BEL",  # Belgium
    "BLZ",  # Belize
    "BEN",  # Benin
    "BMU",  # Bermuda
    "BTN",  # Bhutan
    "BOL",  # Bolivia
    "BIH",  # Bosnia and Herzegovina
    "BWA",  # Botswana
    "BVT",  # Bouvet Island
    "BRA",  # Brazil
    "IOT",  # British Indian Ocean Territory
    "BRN",  # Brunei Darussalam
    "BGR",  # Bulgaria
    "BFA",  # Burkina Faso
    "BDI",  # Burundi
    "KHM",  # Cambodia
    "CMR",  # Cameroon
    "CPV",  # Cape Verde
    "CYM",  # Cayman Islands
    "CAF",  # Central African Republic
    "TCD",  # Chad
    "CHL",  # Chile
    "CHN",  # China
    "CXR",  # Christmas Island
    "CCK",  # Cocos (Keeling) Islands
    "COL",  # Colombia
    "COM",  # Comoros
    "COG",  # Congo
    "COD",  # Congo, the Democratic Republic of the
    "COK",  # Cook Islands
    "CRI",  # Costa Rica
    "CIV",  # Côte d'Ivoire
    "HRV",  # Croatia
    "CUB",  # Cuba
    "CYP",  # Cyprus
    "CZE",  # Czech Republic
    "DNK",  # Denmark
    "DJI",  # Djibouti
    "DMA",  # Dominica
    "DOM",  # Dominican Republic
    "ECU",  # Ecuador
    "EGY",  # Egypt
    "SLV",  # El Salvador
    "GNQ",  # Equatorial Guinea
    "ERI",  # Eritrea
    "EST",  # Estonia
    "ETH",  # Ethiopia
    "FLK",  # Falkland Islands (Malvinas)
    "FRO",  # Faroe Islands
    "FJI",  # Fiji
    "FIN",  # Finland
    "FRA",  # France
    "GUF",  # French Guiana
    "PYF",  # French Polynesia
    "ATF",  # French Southern Territories
    "GAB",  # Gabon
    "GMB",  # Gambia
    "GEO",  # Georgia
    "DEU",  # Germany
    "GHA",  # Ghana
    "GIB",  # Gibraltar
    "GRC",  # Greece
    "GRL",  # Greenland
    "GRD",  # Grenada
    "GLP",  # Guadeloupe
    "GUM",  # Guam
    "GTM",  # Guatemala
    "GGY",  # Guernsey
    "GIN",  # Guinea
    "GNB",  # Guinea-Bissau
    "GUY",  # Guyana
    "HTI",  # Haiti
    "HMD",  # Heard Island and McDonald Islands
    "VAT",  # Holy See (Vatican City State)
    "HND",  # Honduras
    "HKG",  # Hong Kong
    "HUN",  # Hungary
    "ISL",  # Iceland
    "IND",  # India
    "IDN",  # Indonesia
    "IRN",  # Iran, Islamic Republic of
    "IRQ",  # Iraq
    "IRL",  # Ireland
    "IMN",  # Isle of Man
    "ISR",  # Israel
    "ITA",  # Italy
    "JAM",  # Jamaica
    "JPN",  # Japan
    "JEY",  # Jersey
    "JOR",  # Jordan
    "KAZ",  # Kazakhstan
    "KEN",  # Kenya
    "KIR",  # Kiribati
    "PRK",  # Korea, Democratic People's Republic of
    "KOR",  # Korea, Republic of
    "KWT",  # Kuwait
    "KGZ",  # Kyrgyzstan
    "LAO",  # Lao People's Democratic Republic
    "LVA",  # Latvia
    "LBN",  # Lebanon
    "LSO",  # Lesotho
    "LBR",  # Liberia
    "LBY",  # Libya
    "LIE",  # Liechtenstein
    "LTU",  # Lithuania
    "LUX",  # Luxembourg
    "MAC",  # Macao
    "MKD",  # Macedonia, the former Yugoslav Republic of
    "MDG",  # Madagascar
    "MWI",  # Malawi
    "MYS",  # Malaysia
    "MDV",  # Maldives
    "MLI",  # Mali
    "MLT",  # Malta
    "MHL",  # Marshall Islands
    "MTQ",  # Martinique
    "MRT",  # Mauritania
    "MUS",  # Mauritius
    "MYT",  # Mayotte
    "MEX",  # Mexico
    "FSM",  # Micronesia, Federated States of
    "MDA",  # Moldova, Republic of
    "MCO",  # Monaco
    "MNG",  # Mongolia
    "MNE",  # Montenegro
    "MSR",  # Montserrat
    "MAR",  # Morocco
    "MOZ",  # Mozambique
    "MMR",  # Myanmar
    "NAM",  # Namibia
    "NRU",  # Nauru
    "NPL",  # Nepal
    "NLD",  # Netherlands
    "ANT",  # Netherlands Antilles
    "NCL",  # New Caledonia
    "NZL",  # New Zealand
    "NIC",  # Nicaragua
    "NER",  # Niger
    "NGA",  # Nigeria
    "NIU",  # Niue
    "NFK",  # Norfolk Island
    "MNP",  # Northern Mariana Islands
    "NOR",  # Norway
    "OMN",  # Oman
    "PAK",  # Pakistan
    "PLW",  # Palau
    "PSE",  # Palestine, State of
    "PAN",  # Panama
    "PNG",  # Papua New Guinea
    "PRY",  # Paraguay
    "PER",  # Peru
    "PHL",  # Philippines
    "PCN",  # Pitcairn
    "POL",  # Poland
    "PRT",  # Portugal
    "PRI",  # Puerto Rico
    "QAT",  # Qatar
    "REU",  # Réunion
    "ROU",  # Romania
    "RUS",  # Russian Federation
    "RWA",  # Rwanda
    "BLM",  # Saint Barthélemy
    "SHN",  # Saint Helena, Ascension and Tristan da Cunha
    "KNA",  # Saint Kitts and Nevis
    "LCA",  # Saint Lucia
    "MAF",  # Saint Martin (French part)
    "SPM",  # Saint Pierre and Miquelon
    "VCT",  # Saint Vincent and the Grenadines
    "WSM",  # Samoa
    "SMR",  # San Marino
    "STP",  # Sao Tome and Principe
    "SAU",  # Saudi Arabia
    "SEN",  # Senegal
    "SRB",  # Serbia
    "SYC",  # Seychelles
    "SLE",  # Sierra Leone
    "SGP",  # Singapore
    "SVK",  # Slovakia
    "SVN",  # Slovenia
    "SLB",  # Solomon Islands
    "SOM",  # Somalia
    "ZAF",  # South Africa
    "SGS",  # South Georgia and the South Sandwich Islands
    "ESP",  # Spain
    "LKA",  # Sri Lanka
    "SDN",  # Sudan
    "SUR",  # Suriname
    "SJM",  # Svalbard and Jan Mayen
    "SWZ",  # Swaziland
    "SWE",  # Sweden
    "CHE",  # Switzerland
    "SYR",  # Syrian Arab Republic
    "TWN",  # Taiwan, Province of China
    "TJK",  # Tajikistan
    "THA",  # Thailand
    "TLS",  # Timor-Leste
    "TGO",  # Togo
    "TKL",  # Tokelau
    "TON",  # Tonga
    "TTO",  # Trinidad and Tobago
    "TUN",  # Tunisia
    "TUR",  # Turkey
    "TKM",  # Turkmenistan
    "TCA",  # Turks and Caicos Islands
    "TUV",  # Tuvalu
    "UGA",  # Uganda
    "UKR",  # Ukraine
    "ARE",  # United Arab Emirates
    "GBR",  # United Kingdom
    "UMI",  # United States Minor Outlying Islands
    "URY",  # Uruguay
    "UZB",  # Uzbekistan
    "VUT",  # Vanuatu
    "VEN",  # Venezuela, Bolivarian Republic of
    "VNM",  # Viet Nam
    "VGB",  # Virgin Islands, British
    "VIR",  # Virgin Islands, U.S.
    "WLF",  # Wallis and Futuna
    "ESH",  # Western Sahara
    "YEM",  # Yemen
    "ZMB",  # Zambia
    "ZWE",  # Zimbabwe
    "XX",  # Unknown
]
