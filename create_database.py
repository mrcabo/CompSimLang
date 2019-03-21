import numpy as np


def write_block(f, block, block_num, num_examples):
    sInput = "I: {   1} "  # + "{}".format(0)
    sTarget = "T: {   1} "  # + "{}".format(0)
    f.write("name: Block" + "{}".format(block_num) + " {}".format(num_examples) + "\n")
    for _, x in enumerate(block):
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

    train_file = open(path, 'w')
    for i in range(6):
        np.random.shuffle(block)
        write_block(train_file, block, i, 432)

    np.random.shuffle(block_ungr)
    write_block(train_file, block_ungr, "-ungrammatical", 864)
    np.random.shuffle(block)
    write_block(train_file, block, "-recovery", 432)

    train_file.close()


    # Make the test set
    # TODO: test set