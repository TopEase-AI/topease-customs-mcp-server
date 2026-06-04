"""国家数据模块。

提供全球国家/地区数据的查询功能，支持按中文名、英文名、国家ID、ISO编码检索。
"""

from __future__ import annotations

from typing import TypedDict


class CountryInfo(TypedDict):
    """国家信息结构。"""
    name: str
    enName: str
    countryId: int
    code2: str
    code3: str


COUNTRYS: list[CountryInfo] = [
    {"name": "布基纳法索", "enName": "Burkina Faso", "countryId": 31, "code2": "BF", "code3": "BFA"},
    {"name": "多米尼克", "enName": "Dominica", "countryId": 10634564, "code2": "DM", "code3": "DMA"},
    {"name": "南苏丹", "enName": "South Sudan", "countryId": 10980617, "code2": "SS", "code3": "SSD"},
    {"name": "刚果（布）", "enName": "The Republic of Congo", "countryId": 10634552, "code2": "CG", "code3": "COG"},
    {"name": "几内亚比绍", "enName": "Guinea-Bissau", "countryId": 10980086, "code2": "GW", "code3": "GNB"},
    {"name": "圣马力诺", "enName": "San Marino", "countryId": 174, "code2": "SM", "code3": "SMR"},
    {"name": "奥地利", "enName": "Austria", "countryId": 12, "code2": "AT", "code3": "AUT"},
    {"name": "安提瓜和巴布达", "enName": "Antigua and Barbuda", "countryId": 154, "code2": "AG", "code3": "ATG"},
    {"name": "基里巴斯", "enName": "Kiribati", "countryId": 108, "code2": "KI", "code3": "KIR"},
    {"name": "法罗群岛", "enName": "Faroe Islands", "countryId": 466, "code2": "FO", "code3": "FRO"},
    {"name": "东帝汶", "enName": "East Timor", "countryId": 59, "code2": "TL", "code3": "TLS"},
    {"name": "俄罗斯联邦", "enName": "Russia", "countryId": 171, "code2": "RU", "code3": "RUS"},
    {"name": "玻利维亚", "enName": "Bolivia", "countryId": 23, "code2": "BO", "code3": "BOL"},
    {"name": "利比亚", "enName": "Libya", "countryId": 116, "code2": "LY", "code3": "LBY"},
    {"name": "法属波利尼西亚", "enName": "French Polynesia", "countryId": 511, "code2": "PF", "code3": "PYF"},
    {"name": "圭亚那", "enName": "Guyana", "countryId": 87, "code2": "GY", "code3": "GUY"},
    {"name": "突尼斯", "enName": "Tunisia", "countryId": 205, "code2": "TN", "code3": "TUN"},
    {"name": "圣基茨和尼维斯", "enName": "Saint Kitts and Nevis", "countryId": 551521, "code2": "KN", "code3": "KNA"},
    {"name": "美国", "enName": "United States", "countryId": 214, "code2": "US", "code3": "USA"},
    {"name": "阿尔及利亚", "enName": "Algeria", "countryId": 4, "code2": "DZ", "code3": "DZA"},
    {"name": "斐济", "enName": "Fiji", "countryId": 67, "code2": "FJ", "code3": "FJI"},
    {"name": "叙利亚", "enName": "Syria", "countryId": 196, "code2": "SY", "code3": "SYR"},
    {"name": "阿尔巴尼亚", "enName": "Albania", "countryId": 3, "code2": "AL", "code3": "ALB"},
    {"name": "马其顿", "enName": "Macedonia", "countryId": 576261, "code2": "MK", "code3": "MKD"},
    {"name": "中国", "enName": "China", "countryId": 43, "code2": "CN", "code3": "CHN"},
    {"name": "西撒哈拉", "enName": "Western Sahara", "countryId": 224, "code2": "EH", "code3": "ESH"},
    {"name": "安道尔", "enName": "Andorra", "countryId": 5, "code2": "AD", "code3": "AND"},
    {"name": "马来西亚", "enName": "Malaysia", "countryId": 124, "code2": "MY", "code3": "MYS"},
    {"name": "乌克兰", "enName": "Ukraine", "countryId": 211, "code2": "UA", "code3": "UKR"},
    {"name": "卢森堡", "enName": "Luxembourg", "countryId": 119, "code2": "LU", "code3": "LUX"},
    {"name": "瓜德罗普", "enName": "Guadeloupe", "countryId": 83, "code2": "GP", "code3": "GLP"},
    {"name": "立陶宛", "enName": "Lithuania", "countryId": 118, "code2": "LT", "code3": "LTU"},
    {"name": "特立尼达和多巴哥", "enName": "Trinidad and Tobago", "countryId": 204, "code2": "TT", "code3": "TTO"},
    {"name": "也门", "enName": "Yemen", "countryId": 225, "code2": "YE", "code3": "YEM"},
    {"name": "阿曼", "enName": "Oman", "countryId": 155, "code2": "OM", "code3": "OMN"},
    {"name": "摩洛哥", "enName": "Morocco", "countryId": 138, "code2": "MA", "code3": "MAR"},
    {"name": "澳大利亚", "enName": "Australia", "countryId": 11, "code2": "AU", "code3": "AUS"},
    {"name": "蒙古", "enName": "Mongolia", "countryId": 136, "code2": "MN", "code3": "MNG"},
    {"name": "梵蒂冈", "enName": "Vatican City", "countryId": 218, "code2": "VA", "code3": "VAT"},
    {"name": "不丹", "enName": "Bhutan", "countryId": 22, "code2": "BT", "code3": "BTN"},
    {"name": "墨西哥", "enName": "Mexico", "countryId": 131, "code2": "MX", "code3": "MEX"},
    {"name": "阿富汗", "enName": "Afghanistan", "countryId": 2, "code2": "AF", "code3": "AFG"},
    {"name": "孟加拉国", "enName": "Bangladesh", "countryId": 16, "code2": "BD", "code3": "BGD"},
    {"name": "希腊", "enName": "Greece", "countryId": 80, "code2": "GR", "code3": "GRC"},
    {"name": "乌兹别克斯坦", "enName": "Uzbekistan", "countryId": 217, "code2": "UZ", "code3": "UZB"},
    {"name": "新喀里多尼亚", "enName": "New Caledonia", "countryId": 145, "code2": "NC", "code3": "NCL"},
    {"name": "皮特凯恩群岛", "enName": "Pitcairn Islands", "countryId": 275, "code2": "PN", "code3": "PCN"},
    {"name": "古巴", "enName": "Cuba", "countryId": 52, "code2": "CU", "code3": "CUB"},
    {"name": "保加利亚", "enName": "Bulgaria", "countryId": 30, "code2": "BG", "code3": "BGR"},
    {"name": "科特迪瓦", "enName": "Cote D'Ivoire", "countryId": 578445, "code2": "CI", "code3": "CIV"},
    {"name": "印度尼西亚", "enName": "Indonesia", "countryId": 96, "code2": "ID", "code3": "IDN"},
    {"name": "斯洛伐克", "enName": "Slovakia", "countryId": 181, "code2": "SK", "code3": "SVK"},
    {"name": "东萨摩亚/美属萨摩亚", "enName": "American Samoa", "countryId": 296, "code2": "AS", "code3": "ASM"},
    {"name": "厄立特里亚", "enName": "Eritrea", "countryId": 465, "code2": "ER", "code3": "ERI"},
    {"name": "黎巴嫩", "enName": "Lebanon", "countryId": 113, "code2": "LB", "code3": "LBN"},
    {"name": "科索沃", "enName": "Kosovo", "countryId": 548146, "code2": "XK", "code3": "XKX"},
    {"name": "蒙特塞拉特", "enName": "Montserrat", "countryId": 137, "code2": "MS", "code3": "MSR"},
    {"name": "托克劳群岛", "enName": "Tokelau", "countryId": 202, "code2": "TK", "code3": "TKL"},
    {"name": "芬兰", "enName": "Finland", "countryId": 68, "code2": "FI", "code3": "FIN"},
    {"name": "伯利兹", "enName": "Belize", "countryId": 19, "code2": "BZ", "code3": "BLZ"},
    {"name": "乌拉圭", "enName": "Uruguay", "countryId": 215, "code2": "UY", "code3": "URY"},
    {"name": "土库曼斯坦", "enName": "Turkmenistan", "countryId": 207, "code2": "TM", "code3": "TKM"},
    {"name": "乌干达", "enName": "Uganda", "countryId": 210, "code2": "UG", "code3": "UGA"},
    {"name": "吉尔吉斯斯坦", "enName": "Kyrgyzstan", "countryId": 110, "code2": "KG", "code3": "KGZ"},
    {"name": "文莱", "enName": "Brunei", "countryId": 29, "code2": "BN", "code3": "BRN"},
    {"name": "瑞士", "enName": "Switzerland", "countryId": 195, "code2": "CH", "code3": "CHE"},
    {"name": "加拿大", "enName": "Canada", "countryId": 37, "code2": "CA", "code3": "CAN"},
    {"name": "缅甸", "enName": "Burma", "countryId": 32, "code2": "MM", "code3": "MMR"},
    {"name": "阿鲁巴", "enName": "Aruba", "countryId": 10, "code2": "AW", "code3": "ABW"},
    {"name": "塞尔维亚", "enName": "Serbia", "countryId": 278, "code2": "RS", "code3": "SRB"},
    {"name": "马拉维", "enName": "Malawi", "countryId": 123, "code2": "MW", "code3": "MWI"},
    {"name": "波黑", "enName": "Bosnia - Herzegovina", "countryId": 24, "code2": "BA", "code3": "BIH"},
    {"name": "瓦努阿图", "enName": "Vanuatu", "countryId": 315, "code2": "VU", "code3": "VUT"},
    {"name": "肯尼亚", "enName": "Kenya", "countryId": 107, "code2": "KE", "code3": "KEN"},
    {"name": "荷兰", "enName": "Netherlands", "countryId": 143, "code2": "NL", "code3": "NLD"},
    {"name": "塔吉克斯坦", "enName": "Tajikistan", "countryId": 197, "code2": "TJ", "code3": "TJK"},
    {"name": "圣诞岛", "enName": "Christmas Island", "countryId": 44, "code2": "CX", "code3": "CXR"},
    {"name": "以色列", "enName": "Israel", "countryId": 100, "code2": "IL", "code3": "ISR"},
    {"name": "萨尔瓦多", "enName": "El Salvador", "countryId": 62, "code2": "SV", "code3": "SLV"},
    {"name": "毛里求斯", "enName": "Mauritius", "countryId": 130, "code2": "MU", "code3": "MUS"},
    {"name": "前苏联", "enName": "USSR(formerly)", "countryId": 216, "code2": "", "code3": ""},
    {"name": "扎伊尔", "enName": "Zaire", "countryId": 227, "code2": "", "code3": ""},
    {"name": "开曼群岛", "enName": "Cayman Islands", "countryId": 39, "code2": "KY", "code3": "CYM"},
    {"name": "葡萄牙", "enName": "Portugal", "countryId": 167, "code2": "PT", "code3": "PRT"},
    {"name": "巴林", "enName": "Bahrain", "countryId": 15, "code2": "BH", "code3": "BHR"},
    {"name": "哥伦比亚", "enName": "Colombia", "countryId": 46, "code2": "CO", "code3": "COL"},
    {"name": "马里", "enName": "Mali", "countryId": 126, "code2": "ML", "code3": "MLI"},
    {"name": "中非共和国", "enName": "Central African", "countryId": 40, "code2": "CF", "code3": "CAF"},
    {"name": "特克斯和凯科斯群岛", "enName": "Turks and Caicos Islands", "countryId": 554226, "code2": "TC", "code3": "TCA"},
    {"name": "关岛", "enName": "Guam", "countryId": 84, "code2": "GU", "code3": "GUM"},
    {"name": "智利", "enName": "Chile", "countryId": 42, "code2": "CL", "code3": "CHL"},
    {"name": "库克群岛", "enName": "Cook Is.", "countryId": 49, "code2": "CK", "code3": "COK"},
    {"name": "中国香港", "enName": "Hong Kong(China)", "countryId": 90, "code2": "HK", "code3": "HKG"},
    {"name": "尼泊尔", "enName": "Nepal", "countryId": 142, "code2": "NP", "code3": "NPL"},
    {"name": "几内亚", "enName": "Guinea", "countryId": 86, "code2": "GN", "code3": "GIN"},
    {"name": "马提尼克岛", "enName": "Martinique", "countryId": 400, "code2": "MQ", "code3": "MTQ"},
    {"name": "瓦利斯和富图纳群岛", "enName": "Wallis And Futuna Islands", "countryId": 480, "code2": "WF", "code3": "WLF"},
    {"name": "塞浦路斯", "enName": "Cyprus", "countryId": 53, "code2": "CY", "code3": "CYP"},
    {"name": "英属印度洋领地", "enName": "British Indian Ocean Territory", "countryId": 302, "code2": "IO", "code3": "IOT"},
    {"name": "马恩岛", "enName": "Isle of man", "countryId": 603, "code2": "IM", "code3": "IMN"},
    {"name": "斯里兰卡", "enName": "Sri Lanka", "countryId": 188, "code2": "LK", "code3": "LKA"},
    {"name": "列支敦士登", "enName": "Liechtenstein", "countryId": 117, "code2": "LI", "code3": "LIE"},
    {"name": "圣卢西亚", "enName": "Saint Lucia", "countryId": 551538, "code2": "LC", "code3": "LCA"},
    {"name": "新西兰", "enName": "New Zealand", "countryId": 146, "code2": "NZ", "code3": "NZL"},
    {"name": "亚美尼亚", "enName": "Armenia", "countryId": 9, "code2": "AM", "code3": "ARM"},
    {"name": "马达加斯加", "enName": "Madagascar", "countryId": 122, "code2": "MG", "code3": "MDG"},
    {"name": "朝鲜", "enName": "D.P.R.Korea", "countryId": 55, "code2": "KP", "code3": "PRK"},
    {"name": "南非", "enName": "South Africa", "countryId": 185, "code2": "ZA", "code3": "ZAF"},
    {"name": "巴布亚新几内亚", "enName": "Papua New Guinea", "countryId": 161, "code2": "PG", "code3": "PNG"},
    {"name": "摩尔多瓦", "enName": "Moldova", "countryId": 134, "code2": "MD", "code3": "MDA"},
    {"name": "罗马尼亚", "enName": "Romania", "countryId": 170, "code2": "RO", "code3": "ROU"},
    {"name": "匈牙利", "enName": "Hungary", "countryId": 92, "code2": "HU", "code3": "HUN"},
    {"name": "柬埔寨", "enName": "Cambodia", "countryId": 35, "code2": "KH", "code3": "KHM"},
    {"name": "瑙鲁", "enName": "Nauru", "countryId": 141, "code2": "NR", "code3": "NRU"},
    {"name": "波多黎各", "enName": "Puerto Rico", "countryId": 168, "code2": "PR", "code3": "PRI"},
    {"name": "巴基斯坦", "enName": "Pakistan", "countryId": 156, "code2": "PK", "code3": "PAK"},
    {"name": "巴西", "enName": "Brazil", "countryId": 27, "code2": "BR", "code3": "BRA"},
    {"name": "科摩罗", "enName": "Comoros", "countryId": 47, "code2": "KM", "code3": "COM"},
    {"name": "南斯拉夫", "enName": "Yugoslavia", "countryId": 226, "code2": "", "code3": ""},
    {"name": "土耳其", "enName": "Turkey", "countryId": 206, "code2": "TR", "code3": "TUR"},
    {"name": "西班牙", "enName": "Spain", "countryId": 186, "code2": "ES", "code3": "ESP"},
    {"name": "委内瑞拉", "enName": "Venezuela", "countryId": 219, "code2": "VE", "code3": "VEN"},
    {"name": "赤道几内亚", "enName": "Equatorial Guinea", "countryId": 63, "code2": "GQ", "code3": "GNQ"},
    {"name": "安哥拉", "enName": "Angola", "countryId": 6, "code2": "AO", "code3": "AGO"},
    {"name": "诺福克岛", "enName": "Norfolk Island", "countryId": 939493, "code2": "NF", "code3": "NFK"},
    {"name": "埃塞俄比亚", "enName": "Ethiopia", "countryId": 65, "code2": "ET", "code3": "ETH"},
    {"name": "冰岛", "enName": "Iceland", "countryId": 93, "code2": "IS", "code3": "ISL"},
    {"name": "英属维尔京群岛", "enName": "British Virgin Islands", "countryId": 222, "code2": "VG", "code3": "VGB"},
    {"name": "科威特", "enName": "Kuwait", "countryId": 109, "code2": "KW", "code3": "KWT"},
    {"name": "吉布提", "enName": "Djibouti", "countryId": 57, "code2": "DJ", "code3": "DJI"},
    {"name": "欧盟", "enName": "european union", "countryId": 550, "code2": "", "code3": ""},
    {"name": "冈比亚", "enName": "Gambia", "countryId": 74, "code2": "GM", "code3": "GMB"},
    {"name": "喀麦隆", "enName": "Cameroon", "countryId": 36, "code2": "CM", "code3": "CMR"},
    {"name": "佛得角", "enName": "The Republic of Cabo Verde", "countryId": 38, "code2": "CV", "code3": "CPV"},
    {"name": "拉脱维亚", "enName": "Latvia", "countryId": 112, "code2": "LV", "code3": "LVA"},
    {"name": "哈萨克斯坦", "enName": "Kazakhstan", "countryId": 106, "code2": "KZ", "code3": "KAZ"},
    {"name": "法属南部领地", "enName": "French Southern Territoties", "countryId": 72, "code2": "TF", "code3": "ATF"},
    {"name": "捷克共和国", "enName": "Czech Republic", "countryId": 54, "code2": "CZ", "code3": "CZE"},
    {"name": "中国澳门", "enName": "Macao(China)", "countryId": 121, "code2": "MO", "code3": "MAC"},
    {"name": "刚果（金）", "enName": "The Democratic Republic of the Congo", "countryId": 48, "code2": "CD", "code3": "COD"},
    {"name": "黑山共和国", "enName": "Republic of Montenegro", "countryId": 5670871, "code2": "ME", "code3": "MNE"},
    {"name": "留尼汪岛", "enName": "Reunion", "countryId": 427, "code2": "RE", "code3": "REU"},
    {"name": "博茨瓦纳", "enName": "Botswana", "countryId": 25, "code2": "BW", "code3": "BWA"},
    {"name": "阿拉伯联盟", "enName": "Arab League", "countryId": 10980628, "code2": "", "code3": ""},
    {"name": "津巴布韦", "enName": "Zimbabwe", "countryId": 229, "code2": "ZW", "code3": "ZWE"},
    {"name": "福克兰群岛", "enName": "Falkland Islands", "countryId": 485, "code2": "FK", "code3": "FLK"},
    {"name": "塞舌尔", "enName": "Seychelles", "countryId": 178, "code2": "SC", "code3": "SYC"},
    {"name": "莱索托", "enName": "Lesotho", "countryId": 114, "code2": "LS", "code3": "LSO"},
    {"name": "埃及", "enName": "Egypt", "countryId": 61, "code2": "EG", "code3": "EGY"},
    {"name": "马绍尔群岛", "enName": "Marshall Islands", "countryId": 128, "code2": "MH", "code3": "MHL"},
    {"name": "爱尔兰", "enName": "Ireland", "countryId": 99, "code2": "IE", "code3": "IRL"},
    {"name": "洪都拉斯", "enName": "Honduras", "countryId": 89, "code2": "HN", "code3": "HND"},
    {"name": "美属维尔京群岛", "enName": "Virgin Islands (U.S.)", "countryId": 221, "code2": "VI", "code3": "VIR"},
    {"name": "苏里南", "enName": "Surinam", "countryId": 192, "code2": "SR", "code3": "SUR"},
    {"name": "马尔代夫", "enName": "Maldives", "countryId": 125, "code2": "MV", "code3": "MDV"},
    {"name": "德国", "enName": "Germany", "countryId": 76, "code2": "DE", "code3": "DEU"},
    {"name": "帕劳", "enName": "Palau", "countryId": 158, "code2": "PW", "code3": "PLW"},
    {"name": "直布罗陀", "enName": "Gibraltar", "countryId": 78, "code2": "GI", "code3": "GIB"},
    {"name": "海地", "enName": "Haiti", "countryId": 88, "code2": "HT", "code3": "HTI"},
    {"name": "菲律宾", "enName": "Philippines", "countryId": 164, "code2": "PH", "code3": "PHL"},
    {"name": "伊拉克", "enName": "Iraq", "countryId": 98, "code2": "IQ", "code3": "IRQ"},
    {"name": "巴勒斯坦", "enName": "Palestine", "countryId": 159, "code2": "PS", "code3": "PSE"},
    {"name": "加蓬", "enName": "Gabon", "countryId": 73, "code2": "GA", "code3": "GAB"},
    {"name": "约旦", "enName": "Jordan", "countryId": 104, "code2": "JO", "code3": "JOR"},
    {"name": "马耳他", "enName": "Malta", "countryId": 127, "code2": "MT", "code3": "MLT"},
    {"name": "塞拉利昂", "enName": "Sierra Leone", "countryId": 179, "code2": "SL", "code3": "SLE"},
    {"name": "所罗门群岛", "enName": "Solomon Islands", "countryId": 183, "code2": "SB", "code3": "SLB"},
    {"name": "瑞典", "enName": "Sweden", "countryId": 194, "code2": "SE", "code3": "SWE"},
    {"name": "白俄罗斯", "enName": "Belarus", "countryId": 34, "code2": "BY", "code3": "BLR"},
    {"name": "意大利", "enName": "Italy", "countryId": 101, "code2": "IT", "code3": "ITA"},
    {"name": "贝宁", "enName": "Benin", "countryId": 20, "code2": "BJ", "code3": "BEN"},
    {"name": "克罗地亚", "enName": "Croatia", "countryId": 51, "code2": "HR", "code3": "HRV"},
    {"name": "乍得", "enName": "Chad", "countryId": 41, "code2": "TD", "code3": "TCD"},
    {"name": "爱沙尼亚", "enName": "Estonia", "countryId": 64, "code2": "EE", "code3": "EST"},
    {"name": "阿联酋", "enName": "United Arab Emirates", "countryId": 212, "code2": "AE", "code3": "ARE"},
    {"name": "巴拿马", "enName": "Panama", "countryId": 160, "code2": "PA", "code3": "PAN"},
    {"name": "老挝", "enName": "Laos", "countryId": 111, "code2": "LA", "code3": "LAO"},
    {"name": "北马里亚纳群岛", "enName": "Northern Mariana Islands", "countryId": 383, "code2": "MP", "code3": "MNP"},
    {"name": "危地马拉", "enName": "Guatemala", "countryId": 85, "code2": "GT", "code3": "GTM"},
    {"name": "毛里塔尼亚", "enName": "Mauritania", "countryId": 129, "code2": "MR", "code3": "MRT"},
    {"name": "圣文森特和格林纳丁斯", "enName": "Saint Vincent And The Grenadines", "countryId": 7283469, "code2": "VC", "code3": "VCT"},
    {"name": "苏丹", "enName": "Sudan", "countryId": 191, "code2": "SD", "code3": "SDN"},
    {"name": "巴拉圭", "enName": "Paraguay", "countryId": 162, "code2": "PY", "code3": "PRY"},
    {"name": "印度", "enName": "India", "countryId": 94, "code2": "IN", "code3": "IND"},
    {"name": "尼日尔", "enName": "Niger", "countryId": 148, "code2": "NE", "code3": "NER"},
    {"name": "利比里亚", "enName": "Liberia", "countryId": 115, "code2": "LR", "code3": "LBR"},
    {"name": "法国", "enName": "France", "countryId": 69, "code2": "FR", "code3": "FRA"},
    {"name": "秘鲁", "enName": "Peru", "countryId": 163, "code2": "PE", "code3": "PER"},
    {"name": "斯洛文尼亚", "enName": "Slovenia", "countryId": 182, "code2": "SI", "code3": "SVN"},
    {"name": "挪威", "enName": "Norway", "countryId": 153, "code2": "NO", "code3": "NOR"},
    {"name": "比利时", "enName": "Belgium", "countryId": 18, "code2": "BE", "code3": "BEL"},
    {"name": "坦桑尼亚", "enName": "Tanzania", "countryId": 199, "code2": "TZ", "code3": "TZA"},
    {"name": "卢旺达", "enName": "Rwanda", "countryId": 173, "code2": "RW", "code3": "RWA"},
    {"name": "新加坡", "enName": "Singapore", "countryId": 180, "code2": "SG", "code3": "SGP"},
    {"name": "加纳", "enName": "Ghana", "countryId": 77, "code2": "GH", "code3": "GHA"},
    {"name": "英国", "enName": "United Kingdom", "countryId": 213, "code2": "GB", "code3": "GBR"},
    {"name": "格陵兰", "enName": "Greenland", "countryId": 81, "code2": "GL", "code3": "GRL"},
    {"name": "多哥", "enName": "Togo", "countryId": 201, "code2": "TG", "code3": "TGO"},
    {"name": "伊朗", "enName": "Iran", "countryId": 97, "code2": "IR", "code3": "IRN"},
    {"name": "巴哈马", "enName": "Bahamas", "countryId": 14, "code2": "BS", "code3": "BHS"},
    {"name": "厄瓜多尔", "enName": "Ecuador", "countryId": 60, "code2": "EC", "code3": "ECU"},
    {"name": "阿塞拜疆", "enName": "Azerbaijan", "countryId": 13, "code2": "AZ", "code3": "AZE"},
    {"name": "尼日利亚", "enName": "Nigeria", "countryId": 149, "code2": "NG", "code3": "NGA"},
    {"name": "塞内加尔", "enName": "Senegal", "countryId": 177, "code2": "SN", "code3": "SEN"},
    {"name": "格鲁吉亚", "enName": "Georgia", "countryId": 75, "code2": "GE", "code3": "GEO"},
    {"name": "牙买加", "enName": "Jamaica", "countryId": 102, "code2": "JM", "code3": "JAM"},
    {"name": "哥斯达黎加", "enName": "Costa Rica", "countryId": 50, "code2": "CR", "code3": "CRI"},
    {"name": "图瓦卢", "enName": "Tuvalu", "countryId": 209, "code2": "TV", "code3": "TUV"},
    {"name": "泰国", "enName": "Thailand", "countryId": 200, "code2": "TH", "code3": "THA"},
    {"name": "格林纳达", "enName": "Grenada", "countryId": 82, "code2": "GD", "code3": "GRD"},
    {"name": "密克罗尼西亚", "enName": "Micronesia", "countryId": 132, "code2": "FM", "code3": "FSM"},
    {"name": "安圭拉", "enName": "Anguilla", "countryId": 992793, "code2": "AI", "code3": "AIA"},
    {"name": "纳米比亚", "enName": "Namibia", "countryId": 140, "code2": "NA", "code3": "NAM"},
    {"name": "纽埃", "enName": "Niue", "countryId": 150, "code2": "NU", "code3": "NIU"},
    {"name": "卡塔尔", "enName": "Qatar", "countryId": 169, "code2": "QA", "code3": "QAT"},
    {"name": "斯威士兰", "enName": "Swaziland", "countryId": 193, "code2": "SZ", "code3": "SWZ"},
    {"name": "百慕大", "enName": "Bermuda", "countryId": 21, "code2": "BM", "code3": "BMU"},
    {"name": "韩国", "enName": "Korea", "countryId": 105, "code2": "KR", "code3": "KOR"},
    {"name": "索马里", "enName": "Somalia", "countryId": 184, "code2": "SO", "code3": "SOM"},
    {"name": "莫桑比克", "enName": "Mozambique", "countryId": 139, "code2": "MZ", "code3": "MOZ"},
    {"name": "日本", "enName": "Japan", "countryId": 103, "code2": "JP", "code3": "JPN"},
    {"name": "丹麦", "enName": "Denmark", "countryId": 56, "code2": "DK", "code3": "DNK"},
    {"name": "尼加拉瓜", "enName": "Nicaragua", "countryId": 147, "code2": "NI", "code3": "NIC"},
    {"name": "沙特阿拉伯", "enName": "Saudi Arabia", "countryId": 176, "code2": "SA", "code3": "SAU"},
    {"name": "布隆迪", "enName": "Burundi", "countryId": 33, "code2": "BI", "code3": "BDI"},
    {"name": "圣多美和普林西比", "enName": "Sao Tome and Principe", "countryId": 983620, "code2": "ST", "code3": "STP"},
    {"name": "摩纳哥", "enName": "Monaco", "countryId": 135, "code2": "MC", "code3": "MCO"},
    {"name": "越南", "enName": "Vietnam", "countryId": 220, "code2": "VN", "code3": "VNM"},
    {"name": "法属圭亚那", "enName": "French Guiana", "countryId": 70, "code2": "GF", "code3": "GUF"},
    {"name": "巴巴多斯", "enName": "Barbados", "countryId": 17, "code2": "BB", "code3": "BRB"},
    {"name": "波兰", "enName": "Poland", "countryId": 166, "code2": "PL", "code3": "POL"},
    {"name": "阿根廷", "enName": "Argentina", "countryId": 8, "code2": "AR", "code3": "ARG"},
    {"name": "多米尼加", "enName": "The Dominican Rep.", "countryId": 58, "code2": "DO", "code3": "DOM"},
    {"name": "中国台湾", "enName": "Taiwan(China)", "countryId": 198, "code2": "TW", "code3": "TWN"},
    {"name": "马约特岛", "enName": "Mayotte", "countryId": 307, "code2": "YT", "code3": "MYT"},
    {"name": "汤加", "enName": "Tonga", "countryId": 203, "code2": "TO", "code3": "TON"},
    {"name": "欧亚经济联盟", "enName": "Eurasian Economic Union", "countryId": 10980625, "code2": "", "code3": ""},
    {"name": "赞比亚", "enName": "Zambia", "countryId": 228, "code2": "ZM", "code3": "ZMB"},
]


def find_by_name(name: str) -> CountryInfo | None:
    """按中文名称精确查找国家。"""
    for country in COUNTRYS:
        if country["name"] == name:
            return country
    return None


def find_by_enname(enname: str) -> CountryInfo | None:
    """按英文名称精确查找国家。"""
    for country in COUNTRYS:
        if country["enName"].lower() == enname.lower():
            return country
    return None


def find_by_id(country_id: int) -> CountryInfo | None:
    """按国家ID查找。"""
    for country in COUNTRYS:
        if country["countryId"] == country_id:
            return country
    return None


def find_by_code2(code2: str) -> CountryInfo | None:
    """按ISO 3166-1 alpha-2（2位编码）查找国家。"""
    for country in COUNTRYS:
        if country["code2"] and country["code2"].upper() == code2.upper():
            return country
    return None


def find_by_code3(code3: str) -> CountryInfo | None:
    """按ISO 3166-1 alpha-3（3位编码）查找国家。"""
    for country in COUNTRYS:
        if country["code3"] and country["code3"].upper() == code3.upper():
            return country
    return None


def search_by_name(keyword: str) -> list[CountryInfo]:
    """按关键词模糊搜索国家（匹配中文名和英文名）。"""
    results: list[CountryInfo] = []
    keyword_lower = keyword.lower()
    for country in COUNTRYS:
        if keyword_lower in country["name"].lower() or keyword_lower in country["enName"].lower():
            results.append(country)
    return results


def find_country(keyword: str) -> int | 0:
    """统一查找国家，依次按 name、enName、code2、code3 精确匹配。

    匹配顺序：
        1. 中文名称精确匹配 (name)
        2. 英文名称精确匹配，不区分大小写 (enName)
        3. ISO 3166-1 alpha-2 编码精确匹配，不区分大小写 (code2)
        4. ISO 3166-1 alpha-3 编码精确匹配，不区分大小写 (code3)

    Args:
        keyword: 查找关键词，可以是中文名、英文名、2位或3位 ISO 编码

    Returns:
        匹配的国家信息，未找到返回 None
    """
    country = find_by_name(keyword)
    if country:
        return int(country["countryId"])
    country = find_by_enname(keyword)
    if country:
        return int(country["countryId"])
    if len(keyword.strip()) == 2:
        country = find_by_code2(keyword)
        if country:
            return int(country["countryId"])
    if len(keyword.strip()) == 3:
        country = find_by_code3(keyword)
        if country:
            return int(country["countryId"]) 
    return 0


def get_country_id(name_or_enname: str) -> int | None:
    """根据中文名或英文名获取国家ID，优先精确匹配。"""
    country = find_by_name(name_or_enname)
    if country:
        return country["countryId"]
    country = find_by_enname(name_or_enname)
    if country:
        return country["countryId"]
    return None


def get_all_country_names() -> list[str]:
    """获取所有国家中文名称列表。"""
    return [c["name"] for c in COUNTRYS]


def get_all_en_names() -> list[str]:
    """获取所有国家英文名称列表。"""
    return [c["enName"] for c in COUNTRYS]


__all__ = [
    "CountryInfo",
    "COUNTRYS",
    "find_by_name",
    "find_by_enname",
    "find_by_id",
    "find_by_code2",
    "find_by_code3",
    "find_country",
    "search_by_name",
    "get_country_id",
    "get_all_country_names",
    "get_all_en_names",
]