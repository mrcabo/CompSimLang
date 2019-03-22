import numpy as np


def write_block(f, block, block_num):
    sInput = "I: {   1} "  # + "{}".format(0)
    sTarget = "T: {   1} "  # + "{}".format(0)
    for i, x in enumerate(block):
        f.write("name: {" + "{}".format(i) + "_{}".format(block_num) + "} 2\n")
        f.write(sInput + "{}".format(x[0]) + '\n')
        f.write(sTarget + "{}".format(x[1]) + '\n')
        f.write(sInput + "{}".format(x[1]) + '\n')
        f.write(sTarget + "{}".format(x[2]) + '\n')
        f.write(";\n")


if __name__ == "__main__":
    np.random.seed(0)

    train_filename = "q5_train.txt"
    test_filename = "q5_test.txt"
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
        suf = np.reshape(np.repeat(suffix_arr[i], np.size(words_arr)), (np.size(words_arr), 1))
        block = np.vstack((block, np.hstack((np.hstack((pref, mid)), suf))))

    # Creating Ungrammatical
    pref = np.reshape(np.repeat(prefix_arr[0], np.size(words_arr)), (np.size(words_arr), 1))
    suf1 = np.reshape(np.repeat(suffix_arr[1], np.size(words_arr)), (np.size(words_arr), 1))
    suf2 = np.reshape(np.repeat(suffix_arr[2], np.size(words_arr)), (np.size(words_arr), 1))
    block_ungr = np.hstack((np.hstack((pref, mid)), suf1))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((pref, mid)), suf2))))
    pref = np.reshape(np.repeat(prefix_arr[1], np.size(words_arr)), (np.size(words_arr), 1))
    suf1 = np.reshape(np.repeat(suffix_arr[0], np.size(words_arr)), (np.size(words_arr), 1))
    suf2 = np.reshape(np.repeat(suffix_arr[2], np.size(words_arr)), (np.size(words_arr), 1))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((pref, mid)), suf1))))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((pref, mid)), suf2))))
    pref = np.reshape(np.repeat(prefix_arr[2], np.size(words_arr)), (np.size(words_arr), 1))
    suf1 = np.reshape(np.repeat(suffix_arr[0], np.size(words_arr)), (np.size(words_arr), 1))
    suf2 = np.reshape(np.repeat(suffix_arr[1], np.size(words_arr)), (np.size(words_arr), 1))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((pref, mid)), suf1))))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((pref, mid)), suf2))))

    train_file = open(train_filename, 'w')
    for i in range(6):
        np.random.shuffle(block)
        write_block(train_file, block, i)

    np.random.shuffle(block_ungr)
    write_block(train_file, block_ungr, "6")
    np.random.shuffle(block)
    write_block(train_file, block, "7")
    train_file.close()

    # Make the test set
    train_file = open(test_filename, 'w')
    np.random.shuffle(block)
    write_block(train_file, block[0:12], 8)
    train_file.close()
