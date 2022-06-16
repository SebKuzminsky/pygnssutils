"""
Test NTRIP sourcetable
"""

TESTSRT = [
    [
        "AGSSIAAP",
        "Acheres",
        "RTCM 3.0",
        "1004(1),1006(13),1012(1),1033(31)",
        "2",
        "GPS+GLO",
        "SNIP",
        "FRA",
        "48.97",
        "2.17",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "2520",
        "",
    ],
    [
        "agtekrtk",
        "Helsinki",
        "RTCM 3.3",
        "1005(10),1008(10),1033(10),1071(1),1074(1),1077(1),1084(1),1087(1),1094(1),1097(1),1107(1),1114(1),1117(1),1127(1),1230(30)",
        "0",
        "GPS+GLO+GAL+BDS+QZS+SBS",
        "SNIP",
        "FIN",
        "60.22",
        "25.02",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "Agviser",
        "Rumsey",
        "RTCM 3.2",
        "1005(1),1008(5),1033(5),1074(1),1084(1),1124(1),1230(5)",
        "",
        "GPS+GLO+BDS",
        "SNIP",
        "CAN",
        "51.88",
        "-112.78",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "3060",
        "",
    ],
    [
        "Ahrensboek_01",
        "Ahrensboek",
        "RTCM 3.3",
        "1002(1),1006(10),1010(1),1097(1),1107(1),1117(1)",
        "1",
        "GPS+GAL+QZS",
        "SNIP",
        "DEU",
        "54.01",
        "10.58",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "AJanasz",
        "Przasnysz",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "POL",
        "53.06",
        "20.73",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "20380",
        "",
    ],
    [
        "AKASAKI-JF",
        "Tottori",
        "RTCM 3.3",
        "1005(10),1074(1),1084(1),1094(1),1124(1),1230(5)",
        "0",
        "GPS+GLO+GAL+BDS+QZS",
        "SNIP",
        "JPN",
        "35.51",
        "133.66",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "AkitaPrefUnivOgata",
        "Akita",
        "RTCM 3.2",
        "1005(10),1077(1),1087(1),1230(1)",
        "",
        "GPS+GLO",
        "SNIP",
        "JPN",
        "40.01",
        "139.96",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "2040",
        "",
    ],
    [
        "AkitaPrefUnivOgataMF",
        "Akita",
        "RTCM 3.2",
        "1005(10),1077(1),1087(1),1097(1),1127(1),1230(1)",
        "0",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "JPN",
        "40.01",
        "139.96",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "AlaAijala",
        "Laitila",
        "RTCM 3.2",
        "1005(10),1077(1),1087(1),1097(1),1127(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "FIN",
        "60.88",
        "21.72",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "6560",
        "",
    ],
    [
        "AlabamaSylacauga",
        "Sylacauga",
        "RTCM 3.2",
        "1005(1),1077(1),1087(1),1097(1),1127(1),1230(10),4072(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "USA",
        "33.22",
        "-86.31",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "6100",
        "",
    ],
    [
        "AMBER-P",
        "Yamato-Kanagawa",
        "RTCM 3.3",
        "1005(10),1019(1),1044(2),1046(1)",
        "",
        "GPS+GAL+QZS",
        "SNIP",
        "JPN",
        "35.50",
        "139.45",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "1320",
        "",
    ],
    [
        "ANDREJKOVICS",
        "Nyiregyhaza",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "0",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "HUN",
        "47.96",
        "21.62",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "AntiguaBarbuda1",
        "Saint John",
        "RTCM 3.2",
        "1006(10),1008(10),1013(10),1033(10),1074(1),1084(1),1230(10)",
        "0",
        "GPS+GLO",
        "SNIP",
        "ATG",
        "17.12",
        "-61.85",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "AntonioRTK_05",
        "Villanueva de los Infantes",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1087(1),1094(1),1230(1)",
        "",
        "GPS+GLO+GAL",
        "SNIP",
        "ESP",
        "38.74",
        "-3.01",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "5980",
        "",
    ],
    [
        "AOZORA",
        "Sakuragawa",
        "RTCM 3.2",
        "1005(10),1008(10),1074(1),1124(1)",
        "",
        "GPS+BDS",
        "SNIP",
        "JPN",
        "36.28",
        "140.08",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "2860",
        "",
    ],
    [
        "apinhal",
        "",
        "RTCM 3.2",
        "1006(1),1033(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "PRT",
        "41.06",
        "-8.65",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "7280",
        "",
    ],
    [
        "Aquafarm",
        "Rumsey",
        "RTCM 3.2",
        "1005(5),1008(90),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "0",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "CAN",
        "51.91",
        "-112.93",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "AR_CMS_02",
        "Bristol",
        "RTCM 3",
        "",
        "",
        "",
        "SNIP",
        "GBR",
        "51.48",
        "-2.63",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "AranyRTCM3",
        "Derecske",
        "RTCM 3.2",
        "1005(1),1033(10),1074(1),1084(1),1094(1),1124(1),1230(10)",
        "0",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "HUN",
        "47.32",
        "21.58",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "ares",
        "Zachpom",
        "RTCM 3.2",
        "1005(1),1033(10),1074(1),1084(1),1094(1),1124(1),1230(10)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "POL",
        "53.03",
        "14.85",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "3920",
        "",
    ],
    [
        "ARGOACU",
        "ACU",
        "RTCM 3.2",
        "1006(10),1008(10),1013(10),1033(10),1073(2),1083(2),1093(2),1123(2),1230(10)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "BRA",
        "-21.84",
        "-41.00",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "1680",
        "",
    ],
    [
        "ARL-RTK",
        "Mavis Enderby",
        "RTCM 3.2",
        "1005(1),1074(1),1077(1),1084(1),1087(1),1094(1),1097(1),1124(1),1127(1),1230(1),4072(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "GBR",
        "53.18",
        "0.03",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "27060",
        "",
    ],
    [
        "ARLINGTON-76017",
        "Arlington",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "USA",
        "32.67",
        "-97.18",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "18300",
        "",
    ],
    [
        "arnoldd",
        "Pludry",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "POL",
        "50.68",
        "18.47",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4360",
        "",
    ],
    [
        "ARSELECTRONICA",
        "Linz",
        "RTCM 3.2",
        "1005(1),1077(1),1087(1),1097(1),1127(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "AUT",
        "48.31",
        "14.28",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "7500",
        "",
    ],
    [
        "Ash_NZ",
        "",
        "RTCM 3.2",
        "1006(10),1074(1),1084(1),1094(1),1230(1)",
        "0",
        "GPS+GLO+GAL",
        "SNIP",
        "NZL",
        "-43.90",
        "171.76",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "ASTRUP-HEDEGAARD",
        "Skjern",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "0",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "DNK",
        "56.03",
        "8.60",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    ["AUADL", "Glenside", "RTCM 3.0", "1004(1),1006(10),1008(10),"],
    [
        "AUS_LOFT_GNSS",
        "Austin, Tx",
        "RTCM 3.2",
        "1005(1),1074(1),1077(1),1084(1),1087(1),1094(1),1097(1),1124(1),1127(1),1230(1),4072(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "USA",
        "30.28",
        "-97.69",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "10540",
        "",
    ],
    [
        "AUT_JOSRESRTK_ETRS89",
        "Wieselburg",
        "RTCM 3.2",
        "1005(1),1008(1),1074(1),1077(1),1084(1),1087(1),1094(1),1097(1),1124(1),1127(1),1230(1),4072(1)",
        "0",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "AUT",
        "48.13",
        "15.14",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "AUT_RAMETZHOFEN_MGI",
        "Bischofstetten",
        "RTCM 3.2",
        "1005(1),1008(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "0",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "AUT",
        "48.13",
        "15.48",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "AUTOMATO",
        "Ramat Gan",
        "RTCM 3.3",
        "1004(1),1005(30),1006(30),1012(1),1019(3),1020(3),1042(3),1046(4),1077(1),1087(1),1097(1),1107(1),1127(1),1230(30)",
        "2",
        "GPS+GLO+GAL+BDS+SBS",
        "SNIP",
        "ISR",
        "47.10",
        "-1.27",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "9540",
        "",
    ],
    [
        "AUTOMATO_ROBOTICS2",
        "Beit Yeoshua",
        "RTCM 3.3",
        "1004(1),1005(10),1008(10),1012(1),1019(3),1020(3),1033(10),1042(3),1046(5),1077(1),1087(1),1097(1),1107(1),1127(1),1230(30)",
        "2",
        "GPS+GLO+GAL+BDS+SBS",
        "SNIP",
        "ISR",
        "32.35",
        "34.90",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "9340",
        "",
    ],
    [
        "AVRIL",
        "Waterloo",
        "RTCM 3.0",
        "1004(1),1006(10),1008(10),1012(1),1033(10)",
        "2",
        "GPS+GLO",
        "SNIP",
        "CAN",
        "43.47",
        "-80.54",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "Avular",
        "Eindhoven",
        "RTCM 3",
        "PENDING",
        "0",
        "",
        "SNIP",
        "NLD",
        "51.45",
        "5.45",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "AZU1",
        "AZU1_RTCM3",
        "RTCM 3.0",
        "1004(1),1005(30),1007(30),1012(1),1019(900),1029(900),1033(30)",
        "2",
        "GPS+GLO",
        "UNAVCO",
        "USA",
        "34.13",
        "-117.90",
        "1",
        "0",
        "sNTRIP",
        "None",
        "N",
        "N",
        "2280",
        "",
    ],
    [
        "backbog",
        "Kankaanpaa",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1230(1)",
        "",
        "GPS+GLO+GAL",
        "SNIP",
        "FIN",
        "61.85",
        "22.41",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "7020",
        "",
    ],
    [
        "BalcarresSouthRTK",
        "Balcarres",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "CAN",
        "50.74",
        "-103.57",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4400",
        "",
    ],
    [
        "Balhelvie",
        "Newburgh, Fife",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1230(1)",
        "",
        "GPS+GLO+GAL",
        "SNIP",
        "GBR",
        "56.38",
        "-3.12",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4360",
        "",
    ],
    [
        "ballymagorry85",
        "Strabane",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1230(1)",
        "",
        "GPS+GLO+GAL",
        "SNIP",
        "IRL",
        "54.86",
        "-7.43",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "2880",
        "",
    ],
    [
        "Baltow",
        "",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "0",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "POL",
        "51.04",
        "21.52",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "Bant",
        "Bant",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1230(1)",
        "",
        "GPS+GLO+GAL",
        "SNIP",
        "NLD",
        "52.77",
        "5.79",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "3740",
        "",
    ],
    [
        "Baraki1",
        "Sochocin",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "0",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "POL",
        "52.77",
        "17.07",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "BarumHomeBase",
        "Barum",
        "RTCM 3.2",
        "1005(1),1077(1),1087(1),1097(1),1127(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "DEU",
        "53.05",
        "10.52",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "7000",
        "",
    ],
    [
        "Basisdepeel",
        "Evertsoord",
        "RTCM 3.3",
        "1004(1),1005(10),1008(10),1012(1),1019(2),1020(2),1033(10),1042(3),1046(3),1077(1),1087(1),1097(1),1107(1),1127(1),1230(30)",
        "2",
        "GPS+GLO+GAL+BDS+SBS",
        "SNIP",
        "NLD",
        "51.41",
        "5.95",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "BatuHijau",
        "Maluk",
        "RTCM 3.2",
        "1004(1),1006(14),1008(15),1012(1),1013(10),1033(15),1230(15)",
        "2",
        "GPS+GLO",
        "SNIP",
        "IDN",
        "-8.96",
        "116.86",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "2080",
        "",
    ],
    [
        "batuhijau",
        "Tongo, Sekongkang, W, Sumbawa",
        "RTCM 3.2",
        "1006(14),1008(15),1013(10),1033(15),1073(1),1083(1),1093(1),1123(1),1230(15)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "IDN",
        "-8.96",
        "116.86",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "5000",
        "",
    ],
    [
        "BAUER_HAUS",
        "Ballendorf",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "DEU",
        "48.56",
        "10.13",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4600",
        "",
    ],
    [
        "BBDS_Leica4G",
        "Bridgetown",
        "RTCM 3.2",
        "1006(15),1013(60),1020(129),1033(15),1045(150),1230(15),4092(1)",
        "",
        "GLO+GAL",
        "SNIP",
        "BRB",
        "13.17",
        "-59.52",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4840",
        "",
    ],
    [
        "BBDS_RTCM_MSM5",
        "Saint John",
        "RTCM 3.2",
        "1006(15),1008(15),1013(60),1033(15),1075(1),1085(1),1095(1),1125(1),1230(15)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "BRB",
        "13.17",
        "-59.52",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "6780",
        "",
    ],
    [
        "BBDS_RTCM_MSM7",
        "Bridgetown",
        "RTCM 3.2",
        "1006(15),1008(15),1013(60),1020(129),1033(15),1045(150),1077(1),1087(1),1097(1),1127(1),1230(15)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "BRB",
        "13.17",
        "-59.52",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "8100",
        "",
    ],
    [
        "BENNYGEE",
        "Perth",
        "RTCM 3.0",
        "1004(1),1006(10),1008(10),1012(1),1013(10),1033(10)",
        "2",
        "GPS+GLO",
        "SNIP",
        "AUS",
        "-31.86",
        "115.83",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "Berlicki",
        "Hrubieszow",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "POL",
        "50.87",
        "23.89",
        "1",
        "0",
        "",
    ],
    [
        "BH_Ref1",
        "",
        "RTCM 3.2",
        "1004(1),1006(10),1008(10),1012(1),1013(10),1033(10),1230(10)",
        "2",
        "GPS+GLO",
        "SNIP",
        "BRA",
        "41.69",
        "-8.85",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "2640",
        "",
    ],
    [
        "bie001",
        "Biervliet",
        "RTCM 3.3",
        "1004(1),1005(10),1008(10),1012(1),1019(2),1020(2),1033(10),1042(3),1046(3),1077(1),1087(1),1097(1),1107(1),1127(1),1230(30)",
        "2",
        "GPS+GLO+GAL+BDS+SBS",
        "SNIP",
        "NLD",
        "51.31",
        "3.68",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "BinsterFarming",
        "Bonchester Bridge",
        "RTCM 3.2",
        "1005(1),1007(1),1032(1),1077(1),1087(1)",
        "0",
        "GPS+GLO",
        "SNIP",
        "GBR",
        "55.43",
        "-2.62",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "BKBD5451",
        "",
        "RTCM 3.2",
        "1005(1),1074(1),1077(1),1084(1),1087(1),1094(1),1097(1),1230(1)",
        "",
        "GPS+GLO+GAL",
        "SNIP",
        "HUN",
        "46.89",
        "20.39",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "22640",
        "",
    ],
    [
        "bldr_SparkFun1",
        "Boulder, CO",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(5)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "USA",
        "40.09",
        "-105.19",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4540",
        "",
    ],
    [
        "Blijham",
        "Blijham",
        "RTCM 3.3",
        "1004(1),1005(10),1008(10),1012(1),1019(2),1020(2),1033(10),1042(3),1046(3),1077(1),1087(1),1097(1),1107(1),1127(1),1230(30)",
        "2",
        "GPS+GLO+GAL+BDS+SBS",
        "SNIP",
        "NLD",
        "53.11",
        "7.10",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "12200",
        "",
    ],
    [
        "BOBASL",
        "Slepcevic",
        "RTCM 3.2",
        "1005(30),1074(1),1084(1),1094(1)",
        "0",
        "GPS+GLO+GAL",
        "SNIP",
        "S",
        "44.75",
        "19.57",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "BogusLowin33",
        "Pruszcz",
        "RTCM 3.2",
        "1005(1),1074(1),1077(1),1084(1),1087(1),1094(1),1230(1)",
        "0",
        "GPS+GLO+GAL",
        "SNIP",
        "POL",
        "53.35",
        "18.17",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "bonertk",
        "Dalum",
        "RTCM 3.2",
        "1005(1),1077(1),1087(1),1097(1),1127(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "SWE",
        "57.88",
        "13.52",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "23820",
        "",
    ],
    [
        "Boomsight",
        "Hellevoetsluis",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "NLD",
        "51.85",
        "4.18",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4860",
        "",
    ],
    [
        "BPACA",
        "Blacka Palanka",
        "RTCM 3.2",
        "1005(31),1074(1),1084(1),1094(1)",
        "",
        "GPS+GLO+GAL",
        "SNIP",
        "SRB",
        "45.25",
        "19.41",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "3640",
        "",
    ],
    [
        "Broedershof",
        "Sint Philipsland",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1230(1)",
        "",
        "GPS+GLO+GAL",
        "SNIP",
        "NLD",
        "51.63",
        "4.15",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4440",
        "",
    ],
    [
        "Brzezie",
        "Sroda Wielkopolska",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1124(1),1230(1)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "POL",
        "52.23",
        "17.37",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4500",
        "",
    ],
    [
        "BUKKA_RTCM3",
        "Miskolc",
        "RTCM 3.0",
        "1002(1),1006(30),1008(30),1010(1),1019(3),1020(4),1033(30)",
        "1",
        "GPS+GLO",
        "SNIP",
        "HUN",
        "47.89",
        "20.68",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "2100",
        "",
    ],
    [
        "BUSSWIL",
        "Busswil",
        "RTCM 3.2",
        "1004(1),1005(10),1008(10),1012(1),1077(1),1087(1),1097(1),1127(1),1230(10)",
        "2",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "CHE",
        "47.10",
        "7.32",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "10820",
        "",
    ],
    [
        "CA_VXMT",
        "Santa Clara, CA",
        "RTCM 3.2",
        "1230(5)",
        "",
        "",
        "SNIP",
        "USA",
        "0.00",
        "0.00",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "20",
        "",
    ],
    [
        "campobueno",
        "Filadelfia",
        "RTCM 3.2",
        "1004(1),1005(30),1074(1),1077(1),1084(1),1087(1),1094(1),1097(1),1230(30)",
        "2",
        "GPS+GLO+GAL",
        "SNIP",
        "PRY",
        "-22.37",
        "-59.96",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "CAR",
        "Argamasilla de Alba",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1230(1)",
        "",
        "GPS+GLO+GAL",
        "SNIP",
        "ESP",
        "39.13",
        "-3.09",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4380",
        "",
    ],
    [
        "CavCastNet_ABLTER",
        "Oyster",
        "RTCM 3.2",
        "1006(10),1074(2),1084(2),1094(2),1124(2),1230(10)",
        "",
        "GPS+GLO+GAL+BDS",
        "SNIP",
        "USA",
        "37.29",
        "-75.93",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "2180",
        "",
    ],
    [
        "cbrookf9p",
        "Crystal Brook",
        "RTCM 3.3",
        "1004(1),1005(30),1006(30),1008(10),1012(1),1019(3),1020(2),1033(10),1046(8),1077(1),1087(1),1097(1),1107(1),1127(1),1230(30)",
        "2",
        "GPS+GLO+GAL+BDS+SBS",
        "SNIP",
        "AUS",
        "-33.35",
        "138.18",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "0",
        "",
    ],
    [
        "CCFarm3",
        "Inglis",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1230(1)",
        "",
        "GPS+GLO+GAL",
        "SNIP",
        "CAN",
        "50.94",
        "-101.14",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4060",
        "",
    ],
    [
        "CHELRTCM3",
        "Chelyabinsk",
        "RTCM 3.0",
        "1004(1),1006(10),1008(10),1012(1),1019(113),1020(113),1033(10)",
        "2",
        "GPS+GLO",
        "SNIP",
        "RUS",
        "53.79",
        "60.66",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "2480",
        "",
    ],
    ["CiochinaIL", "", "RTCM 3.3", "1004(1),1005(10),1008(10),1012(1),101"],
    [
        "ClagganRTK",
        "Culdaff",
        "RTCM 3.2",
        "1005(1),1074(1),1084(1),1094(1),1230(1)",
        "",
        "GPS+GLO+GAL",
        "SNIP",
        "IRL",
        "55.27",
        "-7.17",
        "1",
        "0",
        "sNTRIP",
        "none",
        "N",
        "N",
        "4220",
        "",
    ],
]