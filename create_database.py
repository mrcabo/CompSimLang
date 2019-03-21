import numpy as np


def write_block(f, block, block_num):
    sInput = "I: {   1} "  # + "{}".format(0)
    sTarget = "T: {   1} "  # + "{}".format(0)
    f.write("name: Block" + "{}".format(block_num) + " 432\n")
    for i, x in enumerate(block):
        f.write(sInput + "{}".format(x[0]) + '\n')
        f.write(sTarget + "{}".format(0) + '\n')
        f.write(sInput + "{}".format(x[1]) + '\n')
        f.write(sTarget + "{}".format(0) + '\n')
        f.write(sInput + "{}".format(x[2]) + '\n')
        f.write(sTarget + "{}".format(x[2]) + '\n')
    f.write(";\n")


if __name__ == "__main__":
    np.random.seed(0)

    path = "q5_train.txt"
    num_prefixes = 3
    num_middle_words = 24
    num_suffixes = 3

    prefix_arr = np.arange(num_prefixes)
    words_arr = np.arange(num_prefixes, num_prefixes+num_middle_words)
    suffix_arr = np.arange(num_prefixes+num_middle_words, num_prefixes+num_middle_words+num_suffixes)

    pref = np.reshape(np.repeat(prefix_arr[0], np.size(words_arr)), (np.size(words_arr), 1))
    mid = np.reshape(words_arr, (np.size(words_arr), 1))
    suf = np.reshape(np.repeat(suffix_arr[0], np.size(words_arr)), (np.size(words_arr), 1))
    block = np.hstack((np.hstack((pref, mid)), suf))

    for i in range(1, 3):
        pref = np.reshape(np.repeat(prefix_arr[i], np.size(words_arr)), (np.size(words_arr), 1))
        mid = np.reshape(words_arr, (np.size(words_arr), 1))
        suf = np.reshape(np.repeat(suffix_arr[i], np.size(words_arr)), (np.size(words_arr), 1))
        block = np.vstack((block, np.hstack((np.hstack((pref, mid)), suf))))

    train_file = open(path, 'w')
    for i in range(6):
        np.random.shuffle(block)
        write_block(train_file, block, i)
    train_file.close()