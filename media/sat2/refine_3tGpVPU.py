#########
# CONAN #
#########

### File handling

directory = "/Users/samyakjain/Desktop/Conan"
import os
main_file_list = list()
for filename in os.listdir(directory):
    if filename[0] != ".":
        file = directory + "/" + filename
        # if "Episode-" in filename:
        #     new_name = filename.replace("Episode-","")
        #     opt_file = directory + "/" + new_name
        #     os.rename(file,opt_file)
        file_list = filename.split(".")[0].split("-")
        if len(file_list) == 3:
            main_file_list.append(int(file_list[-1]))
        if len(file_list) == 4:
            main_file_list.append(int(file_list[-2]))
            main_file_list.append(int(file_list[-1]))

miss_list = list()
for i in range(1,974):
    miss_list.append(i)
for j in main_file_list:
    miss_list.remove(j)

print(miss_list)

### Which Episodes are missing upto the number N

# directory = "/Users/samyakjain/Desktop/Conan"
# import os
#
# ep_list = list()
# for filename in os.listdir(directory):
#     if filename != ".DS_Store":
#         file_list = filename.split("-")
#         ep_list.append(int(file_list[-1].split(".")[0]))
# miss_list = list()
#
# for i in range(600,974):
#     miss_list.append(i)
# for j in ep_list:
#     if j >= 600:
#         miss_list.remove(j)
# print(miss_list)
# print(len(miss_list))





### StackOverflow

# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from http.client import RemoteDisconnected
# import time
#
#
# def get_browser():
#    chrome_options = Options()
#    chrome_options.add_argument("--disable-extensions")
#    chrome_options.add_argument('--disable-notifications')
#    chrome_options.add_argument('--incognito')
#    driver = webdriver.Chrome(options=chrome_options)
#    return driver
#
#
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# page_url = "https://www.kiss-anime.ws/Anime-detective-conan-1"
#
# try:
#    driver.set_page_load_timeout(40)
#    driver.get(page_url)
# except TimeoutException:
#    raise Exception(f"\t{page_url} - Timed out receiving message from renderer")
# except RemoteDisconnected:
#    raise Exception(f"\tError 404: {page_url} not found.")
#
# WebDriverWait(driver, timeout=40).until(EC.presence_of_element_located((By.ID, "selectEpisode")))
# driver.find_element_by_id("selectEpisode").click()
# soup = BeautifulSoup(driver.page_source, "html.parser")
#
# options = soup.find("select", attrs={"id": "selectEpisode"}).find_all("option")
# print(f"Found {len(options)} episodes...")

### Getting all the available epsiodes on the website

# main_ep_list = list()
# for i in options:
#     v = str(i['value']).split("-")
#     main_ep_list.append(v[-1])
#
# print(main_ep_list)

### Converting all to Integers

# for i in range(0,len(main_ep_list)):
#     main_ep_list[i] = int(main_ep_list[i])
#
# print(main_ep_list)
# print(len(main_ep_list))

### Main episode list

# main_ep_list =[973, 972, 971, 970, 969, 968, 967, 966, 965, 964, 963, 962, 960, 959, 958, 957, 956, 955, 954, 953, 952, 951, 950, 949, 948, 947, 946, 945, 944, 943, 942, 941, 940, 939, 938, 937, 936, 935, 934, 933, 932, 931, 930, 929, 928, 927, 926, 925, 924, 923, 922, 921, 920, 919, 918, 917, 916, 915, 914, 913, 912, 911, 910, 909, 908, 907, 906, 905, 904, 903, 902, 901, 900, 899, 898, 897, 896, 895, 894, 893, 892, 891, 890, 889, 888, 887, 886, 885, 884, 883, 882, 881, 880, 879, 878, 877, 876, 875, 874, 873, 872, 871, 870, 869, 868, 867, 866, 865, 864, 863, 862, 861, 860, 859, 858, 857, 856, 855, 854, 853, 852, 851, 850, 849, 848, 847, 846, 845, 844, 843, 842, 841, 840, 839, 838, 837, 836, 835, 834, 833, 832, 831, 830, 829, 828, 827, 826, 825, 824, 823, 822, 821, 820, 819, 818, 817, 816, 815, 814, 813, 812, 811, 810, 809, 808, 807, 806, 805, 804, 803, 802, 801, 800, 799, 798, 797, 796, 795, 794, 793, 792, 791, 790, 789, 788, 787, 786, 785, 784, 783, 782, 781, 780, 779, 778, 777, 776, 775, 774, 773, 772, 771, 770, 769, 768, 767, 766, 765, 764, 763, 762, 761, 760, 759, 752, 758, 757, 756, 755, 754, 751, 750, 749, 748, 747, 738, 737, 735, 734, 732, 731, 729, 726, 724, 723, 720, 719, 718, 717, 716, 715, 714, 713, 712, 711, 710, 709, 708, 707, 706, 704, 703, 702, 701, 700, 699, 698, 697, 696, 695, 694, 693, 692, 691, 690, 689, 688, 687, 686, 685, 684, 683, 682, 681, 680, 678, 679, 677, 676, 675, 674, 673, 672, 671, 670, 669, 668, 667, 666, 665, 664, 663, 662, 661, 660, 659, 658, 657, 656, 655, 654, 653, 652, 651, 650, 649, 648, 647, 646, 645, 644, 643, 642, 641, 640, 639, 638, 637, 636, 635, 634, 633, 632, 631, 630, 629, 628, 627, 626, 625, 624, 623, 622, 621, 620, 619, 618, 617, 616, 615, 614, 613, 612, 611, 610, 609, 608, 607, 606, 605, 604, 603, 602, 601, 600, 599, 598, 597, 596, 595, 594, 593, 592, 591, 590, 589, 588, 587, 586, 585, 584, 583, 582, 581, 580, 579, 578, 577, 576, 575, 574, 573, 572, 571, 569, 568, 567, 566, 565, 564, 563, 562, 561, 560, 559, 558, 557, 556, 555, 553, 552, 551, 550, 549, 548, 547, 546, 545, 544, 543, 542, 541, 540, 539, 538, 537, 536, 535, 534, 533, 532, 531, 530, 529, 528, 527, 526, 525, 524, 523, 522, 521, 520, 519, 518, 517, 516, 515, 514, 513, 512, 511, 510, 509, 508, 507, 506, 505, 504, 503, 502, 501, 500, 499, 498, 497, 496, 495, 494, 492, 491, 490, 489, 487, 485, 484, 479, 478, 477, 476, 474, 473, 472, 471, 470, 469, 468, 467, 466, 465, 464, 463, 462, 460, 459, 458, 457, 456, 455, 454, 453, 452, 451, 450, 449, 448, 447, 446, 445, 444, 443, 438, 436, 435, 432, 431, 430, 429, 426, 425, 424, 418, 417, 416, 415, 412, 411, 408, 407, 406, 402, 401, 400, 399, 398, 396, 395, 394, 391, 390, 387, 386, 385, 383, 382, 381, 378, 377, 376, 375, 374, 373, 372, 371, 370, 369, 368, 367, 366, 365, 364, 363, 362, 361, 359, 358, 356, 345, 334, 333, 324, 323, 314, 311, 310, 309, 308, 307, 304, 302, 301, 293, 292, 291, 288, 287, 286, 285, 284, 283, 282, 278, 277, 276, 275, 274, 272, 271, 263, 259, 258, 254, 253, 242, 241, 240, 239, 238, 231, 230, 227, 226, 223, 222, 219, 208, 206, 205, 204, 202, 201, 200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164, 163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 144, 143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 130, 129, 128, 127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

### Creating Main missing list

# main_missing_list = list()
# for i in range(0,974):
#     main_missing_list.append(i)
#
# for j in main_ep_list:
#     main_missing_list.remove(j)
#
# print(main_missing_list)
# print(len(main_missing_list))

### Main missing list

# main_missing_list = [ 131, 145, 203, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 220, 221, 224, 225, 228, 229, 232, 233, 234, 235, 236, 237, 243, 244, 245, 246, 247
# , 248, 249, 250, 251, 252, 255, 256, 257, 260, 261, 262, 264, 265, 266, 267, 268, 269, 270, 273, 279, 280, 281, 289, 290, 294, 295, 296, 297, 298, 299, 300, 303, 305, 306, 312
# , 313, 315, 316, 317, 318, 319, 320, 321, 322, 325, 326, 327, 328, 329, 330, 331, 332, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 346, 347, 348, 349, 350, 351, 352, 353
# , 354, 355, 357, 360, 379, 380, 384, 388, 389, 392, 393, 397, 403, 404, 405, 409, 410, 413, 414, 419, 420, 421, 422, 423, 427, 428, 433, 434, 437, 439, 440, 441, 442, 461, 475
# , 480, 481, 482, 483, 486, 488, 493, 554, 570, 705, 721, 722, 725, 727, 728, 730, 733, 736, 739, 740, 741, 742, 743, 744, 745, 746, 753, 961]

### Special list

### Updating miss_list list

# for k in special:
#     miss_list.remove(k)
# lim = max(miss_list)
# count = 0
# while True:
#     if main_missing_list[count] > lim:
#         break
#     else:
#         if main_missing_list[count] not in special:
#
#             miss_list.remove(main_missing_list[count])
#     count += 1
#
#
# print(miss_list)
# print(len(miss_list))

### Creating Temp List

# temp_list = list()
# # for q in special:

# miss_list.remove(721)
# miss_list.remove(730)
# miss_list.remove(753)

# for q in miss_list:
#    temp_list.append(options[main_ep_list.index(q)])
#
# print(temp_list)

### StackOverflow

# n = 250
# for idx, option in enumerate(options[25+108+61:n]):
# for idx, option in enumerate(temp_list):
#     # print(f"Downloading {idx+1} of {len(options[0:809-n])}...")
#     print(f"Downloading {idx+1} of {len(temp_list)}...")
#     page_url = option['value']
#
#     try:
#         driver.set_page_load_timeout(40)
#         driver.get(page_url)
#     except TimeoutException:
#         print(f"\t{page_url} - Timed out receiving message from renderer")
#         continue
#     except RemoteDisconnected:
#         print(f"\tError 404: {page_url} not found.")
#         continue
#
#     WebDriverWait(driver, timeout=40).until(EC.presence_of_element_located((By.ID, "divDownload")))
#     driver.find_element_by_id("divDownload").click()
#     print(f"\t Downloading...")
#     time.sleep(360)
#
#
# driver.quit()
# print("done")
